class CommandNotFoundError(Exception):
    def __init__(self):
        super().__init__('정의되지 않은 명령어입니다.')

class CommandParseError(Exception):
    def __init__(self):
        super().__init__('명령 구문이 올바르지 않습니다.')

class PermissionDenied(Exception):
    def __init__(self):
        super().__init__('Permission denied:\n명령어를 사용할 수 있는 권한이 없습니다.')