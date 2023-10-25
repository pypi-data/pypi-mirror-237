import inspect, os, re
import subprocess

from pydantic import BaseModel
import importlib.util
from scriptize.exceptions import ScriptModuleMissing
from scriptize.config import log_path
from elemental_tools.logger import Logger

logger = Logger(app_name='scriptize', owner='pydantic-tools', log_path=log_path).log


# Function to generate Pydantic models for script functions
def generate_pydantic_model_from_function(function):
    class Model(BaseModel):
        _: str = None
        class Config:
            arbitrary_types_allowed = True

    argspec = inspect.signature(function)
    for param_name, param in argspec.parameters.items():
        if param_name in ('self', 'cls'):
            continue
        param_type = param.annotation if param.annotation != param.empty else None
        Model.__annotations__[param_name] = (param_type, param.default)

    return Model


def generate_pydantic_model_from_path(path: str):
    result = None
    logger('info', f"Generating models from path {path}")
    scripts_root_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), path)
    script_functions = {}
    # Load scripts from the scripts directory
    try:
        for current_script_dir in os.listdir(scripts_root_path):
            abs_path = os.path.join(scripts_root_path, current_script_dir)
            for script_file in os.listdir(abs_path):
                if script_file.endswith('main.py'):
                    script_name = os.path.splitext(script_file)[0]
                    try:
                        script_path = os.path.join(abs_path, script_file)

                        spec = importlib.util.spec_from_file_location(script_name, script_path)
                        module = importlib.util.module_from_spec(spec)
                        try:
                            spec.loader.exec_module(module)
                        except:
                            pass
                        script_functions[current_script_dir] = module.start
                    except ModuleNotFoundError as e:
                        # Extract the package name from the exception message (if available)
                        package_name_match = re.search(r"'(.*?)'", str(e))
                        if package_name_match:
                            package_name = package_name_match.group(1)
                            try:
                                # Attempt to install the missing package
                                subprocess.run(["pip", "install", package_name])
                            except Exception as install_error:
                                print(f"Error installing {package_name}: {install_error}")
                            else:
                                # Retry importing the script after successful installation
                                try:
                                    module = importlib.util.module_from_spec(spec)
                                    spec.loader.exec_module(module)
                                    script_functions[current_script_dir] = module.start
                                except ModuleNotFoundError:
                                    ScriptModuleMissing(f"{current_script_dir}\nModuleNotFoundError: {str(e)}")
                        else:
                            # ScriptModuleMissing(f"{current_script_dir}\nModuleNotFoundError: {str(e)}")
                            pass

        result = {script_name: {'pydantic_model': generate_pydantic_model_from_function(func), 'function': func} for script_name, func in script_functions.items()}
        logger('success', f"Pydantic models loaded successfully: {script_functions.items()}")

    except Exception as e:
        logger('alert', f"No script addons found! Because of the exception {e} the script functions were left this way: {script_functions.items()}")

    return result


def generate_script_information_from_pydantic_models(script_pydantic_models=None):
    if script_pydantic_models is None:
        return None
    logger('info', f"Generating script information from pydantic models: {script_pydantic_models}")
    scripts_information = {}
    for script_name, parameters_specs in script_pydantic_models.items():
        logger('info', f"Processing: {script_name} script")
        pydantic_model = parameters_specs['pydantic_model']
        scripts_information[script_name] = {}
        scripts_information[script_name]['required'] = []
        scripts_information[script_name]['parameters'] = {}
        for parameter_name, parameter_spec in pydantic_model.__annotations__.items():
            if isinstance(parameter_spec, tuple):
                logger('info', f"Parameter: {parameter_name} was found in {script_name}")
                try:
                    logger('info', f"Parameter: Attempting to retrieve parameter type...")
                    scripts_information[script_name]['parameters'][parameter_name] = {'type': parameter_spec[0].__name__}
                    logger('success', f"Parameter: Type found for {parameter_name} is {parameter_spec[0].__name__}")

                except Exception as e:
                    logger('alert', f"Parameter: type was not found in {script_name} start method")

                try:
                    if parameter_spec[1].__name__ == '_empty':
                        scripts_information[script_name]['required'].append(parameter_name)
                except:
                    scripts_information[script_name]['parameters'][parameter_name]['default_value'] = parameter_spec[1]
                continue
            scripts_information[script_name]['parameters'][parameter_name] = {'type': parameter_spec.__name__}
    logger('success', f"Scripts information: {scripts_information}")
    return scripts_information

