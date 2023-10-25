class ScriptModuleMissing:

    def __init__(self, title):
        print(f'Script module missing when validating: {title}')


class ParameterMissing(Exception):

    def __init__(self, title):
        Exception.__init__(self, f"The function {title} cannot be executed.")


class SettingMissing(Exception):

    def __init__(self, title):
        Exception.__init__(self, f"The function {title} cannot be executed.")