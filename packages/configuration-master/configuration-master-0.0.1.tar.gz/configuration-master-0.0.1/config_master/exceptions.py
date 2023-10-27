class ConfigMasterException(Exception):
    def __init__(self, msg: str):
        super(ConfigMasterException, self).__init__(msg)


class LoadJsonFileException(ConfigMasterException):
    def __init__(self, msg: str):
        super(LoadJsonFileException, self).__init__(msg=msg)


class ConfigException(ConfigMasterException):
    def __init__(self, msg: str):
        super(ConfigException, self).__init__(msg=msg)
