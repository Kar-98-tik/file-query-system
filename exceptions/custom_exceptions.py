class CustomException(Exception):
    def __init__(self, error_message: str, system_error: str):
        self.error_message = error_message
        self.system_error = system_error
        super().__init__(self.error_message)
