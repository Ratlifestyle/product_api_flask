class BadRequestException(Exception):
    def __init__(self, message='Bad Request Exception'):
        self.message = message
        super().__init__(self.message)