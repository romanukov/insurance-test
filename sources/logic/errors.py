from logic.constants import ErrorCodes


class LogicError(BaseException):
    def __init__(self, error_code: ErrorCodes, data=None):
        self.error_code = error_code
        self.data = data
