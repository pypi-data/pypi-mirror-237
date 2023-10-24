from redstat.variables import application


def get_version(namespace):
    name = application.APPLICATION_NAME
    version = application.APPLICATION_VERSION
    if namespace.name_only:
        print(name)
    elif namespace.digit_only:
        print(version)
    else:
        print(f'{name} {version}')
