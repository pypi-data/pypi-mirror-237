from elemental_tools.logger import Logger
from cloudant.client import CouchDB
from datetime import datetime
from fastapi.exceptions import HTTPException

from scriptize.config import envi, log_path, db_pass, db_user, db
from scriptize.exceptions import SettingMissing

logger = Logger(app_name='scriptize', owner='couch-db', log_path=log_path).log


class TaskDB:
    collection_name = f'scriptize_tasks_{envi}'
    server = CouchDB(db_user, db_pass, url=db, connect=True, auto_renew=True)
    views = {}

    def __init__(self):
        self.create_db()

    def create_db(self):
        self.views['not_processed_loops'] = {
            "_id": "_design/tasks",
            "views": {
                "not_processed_loops": {
                    "map": """function(doc) {
                      if (doc.last_execution && doc.loops && doc.timer) {
                        var lastExecution = new Date(doc.last_execution);
                        var timer = doc.timer;
                        var timeDifference = new Date().getTime() - lastExecution.getTime();
                        if (timeDifference >= timer) {
                          emit('loop_count_function', doc);
                        }
                      } else if (doc.loops == undefined && doc.last_execution) {
                        var lastExecution = new Date(doc.last_execution);
                        var timer = doc.timer;
                        var timeDifference = new Date().getTime() - lastExecution.getTime();
                        if (timeDifference >= timer) {
                        emit('infinite_function', doc);
                      }
                        
                      }
                    }"""
                }
            }
        }

        try:
            if self.collection_name not in self.server:
                self.server.create_database(self.collection_name)

            for title, view in self.views.items():
                self.server[self.collection_name].create_document(self.views[title])

        except Exception as e:
            logger('error', f'Cannot create CouchDB database: {self.collection_name} because of exception: {str(e)}')

    def add(self, doc: dict):
        try:
            db = self.server[self.collection_name]
            db.create_document(doc)
            return True

        except Exception as e:
            logger('error', f'Failed to store user because of exception: {str(e)}')

        return False

    def set_status(self, contact_title: str, status: bool):
        db = self.server[self.collection_name]

        doc = self.query(contact_title)

        doc['status'] = status
        try:
            result = db.bulk_docs([doc])
            if all([execution_result['ok'] for execution_result in result]):
                return True

        except Exception as e:
            logger('error', f'Cannot set status for user because of exception: {str(e)}')

        return False

    def get_status(self, contact_title):
        db = self.server[self.collection_name]
        try:
            return self.query(contact_title)['status']
        except Exception as e:
            logger('error', f'Cannot get user status for user because of exception: {str(e)}')

        return None

    def set_loop_count(self, _id: str, loops: int):
        logger('info', f'Setting loop count: {loops} for task _id: {str(_id)} ')
        db = self.server[self.collection_name]
        selector = {'_id': _id}
        task_by_id = db.get_query_result(selector)
        try:
            if task_by_id[0]:
                task_by_id = dict(task_by_id[0][0])
            else:
                raise HTTPException(detail='Cannot find the task id informed on set loop count', status_code=500)

            task_by_id['loops'] = loops
            logger('info', f'Bulking docs...')
            result = db.bulk_docs([task_by_id])
            if all([execution_result['ok'] for execution_result in result]):
                logger('success', f'Loop count updated!')
                return True

        except Exception as e:
            logger('error', f'Cannot set loop count for task because of exception: {str(e)}')

        logger('error', f'Loop count was not updated for some reason')

    def set_last_execution(self, _id: str):
        logger('info', f'Setting last execution for task _id: {str(_id)}')
        db = self.server[self.collection_name]
        selector = {'_id': {"$eq": _id}}
        task_by_id = db.get_query_result(selector)
        try:

            if task_by_id[0]:
                task_by_id = dict(task_by_id[0][0])
            else:
                raise HTTPException(detail='Cannot find the task id informed on set last execution', status_code=500)

            task_by_id['last_execution'] = str(datetime.now().isoformat())
            logger('info', f'Bulking docs... {task_by_id}')
            result = db.bulk_docs([task_by_id])
            if all([execution_result['ok'] for execution_result in result]):
                db.update()
                logger('success', f'Last execution updated!')
                return True

        except Exception as e:
            logger('error', f'Cannot set last execution for task because of exception: {str(e)}')

        logger('error', f'Last execution was not updated for some reason')

    def query(self, selector):
        result = None
        db = self.server[self.collection_name]
        query_result = db.get_query_result(selector)
        if query_result[0]:
            return dict(query_result[0][0])
        return result

    def query_not_processed_loops(self):
        db = self.server[self.collection_name]
        result = db.get_view_result(self.views['not_processed_loops']["_id"], "not_processed_loops", startkey=0)  # Adjust the query parameters as needed

        return [result['value'] for result in list(result)]


class SettingsDB:
    title = "settings"
    server = CouchDB(db_user, db_pass, url=db, connect=True, auto_renew=True)
    views = {}

    class Default:
        pass

    def __init__(self, app_name):
        self.collection_name = f"{app_name}_{self.title}_{envi}"
        self.create_db()

    def create_db(self):

        try:
            if self.collection_name not in self.server:
                self.server.create_database(self.collection_name)

            for title, view in self.views.items():
                self.server[self.collection_name].create_document(self.views[title])

        except Exception as e:
            logger('error', f'Cannot create CouchDB database: {self.collection_name} because of exception: {str(e)}')

    def add(self, name: str, value: str):
        try:
            db = self.server[self.collection_name]
            db.create_document({"_id": name, "value": value})
            return True

        except Exception as e:
            logger('error', f'Failed to store user because of exception: {str(e)}')

        return False

    def get(self, name, *args):
        result = None

        try:
            result = args[0]
        except IndexError:
            pass

        try:
            selector = {"_id": {"$eq": name}}

            db = self.server[self.collection_name]
            query_result = db.get_query_result(selector)
            if query_result[0]:
                return dict(query_result[0][0])['value']
            return result
        except:
            try:
                result = getattr(self.Default, name)
            except:
                if not [*args]:

                    raise SettingMissing(name)

        return result


