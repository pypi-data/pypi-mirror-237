import os
import sys


from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
import random
import string
from elemental_tools.logger import Logger

module_name = 'config'

envi = os.environ.get('environment', None)

# load cache into class
cache_file = './.cache'
if envi is None:
	if sys.platform == "darwin" or sys.platform == "win32":
		envi = 'debug'
	else:
		envi = 'production'

log_path = str(os.environ.get("LOG_PATH", './log') + "_" + envi)
logger = Logger(app_name='scriptize', owner='configs', log_path=log_path).log

logger('info', 'Setting Environment (debug, production) based on platform')
if envi is None:
	if sys.platform == "darwin" or sys.platform == "win32":
		envi = 'debug'
	else:
		envi = 'production'
logger('success', 'The current environment is set to ' + envi)


class Cache:

	def __init__(self, file: str =cache_file):
		self.cache_file = file

		if not os.path.isdir(os.path.dirname(os.path.abspath(cache_file))):
			os.makedirs(os.path.dirname(os.path.abspath(cache_file)), exist_ok=True)

		self.cache_file_content = open(cache_file, 'a+')
		if self.cache_file_content.readlines():
			self.cache_file_content = self.load()
			try:
				data = eval(self.cache_file_content.read())
				for cache_item in data:
					for title, value in cache_item.items():
						setattr(self, title, value)

			except SyntaxError:
				raise Exception("Failed to parse the cache file!")

	def save(self):
		self.cache_file_content.write(str([{title: value for title, value in self.__dict__.items() if not title.startswith('__')}]))
		self.cache_file_content.close()
		return open(cache_file, 'a+')

	def load(self):
		return open(self.cache_file, 'a+')

	def get(self, prop):
		return getattr(self, prop, None)


cache = Cache()


logger('info', 'Loading .env file...')
load_dotenv()
logger('success', '.env file loaded successfully!')
webdriver_url = os.environ.get('WEBDRIVER_URL', 'http://localhost:4444/')


def default_tax():
	logger('info', 'Retrieving tax information...')
	load_dotenv()
	tax = float(os.environ.get('TAX'))
	logger('success', f'The defined tax is: {tax}')
	return tax


logger('info', 'Setting up configuration variables...')

db = os.environ.get('DB', 'http://localhost:5984')
db_user = os.environ.get('DB_USERNAME', 'admin')
db_pass = os.environ.get('DB_PASSWORD', 'admin')

host = os.environ.get('HOST', 'http://localhost')
port = os.environ.get('PORT', 7001)

scripts_root_path = os.environ.get('SCRIPTS_ROOT', './scripts')

logger('success', 'The configuration variables were successfully set.')

logger('info', 'Initializing Chrome Webdriver configuration')

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-gpu")  # Disable GPU
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-dev-shm-usage")

logger('success', 'Chrome Webdriver was configured successfully!')



