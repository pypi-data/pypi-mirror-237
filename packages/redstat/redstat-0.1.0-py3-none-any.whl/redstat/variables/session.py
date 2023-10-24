from requests import Session

from redstat.variables.application import APPLICATION_NAME, APPLICATION_VERSION

BASE_HEADERS = {'user-agent': f'{APPLICATION_NAME} {APPLICATION_VERSION}'}
BASE_SESSION = Session()
BASE_SESSION.headers.update(BASE_HEADERS)
