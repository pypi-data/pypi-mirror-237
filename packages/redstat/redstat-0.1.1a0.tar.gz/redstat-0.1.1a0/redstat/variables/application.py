from importlib.metadata import version, PackageNotFoundError

APPLICATION_NAME = 'redstat'

try:
    APPLICATION_VERSION = version(APPLICATION_NAME)
except PackageNotFoundError as e:
    APPLICATION_VERSION = '0.0.0'
