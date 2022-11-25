class ExistingProductException(Exception):
    def __init__(self, message='Product already exist'):
        self.message = message
        super().__init__(self.message)

class NonExistingProductException(Exception):
    def __init__(self, message='Product does not exist'):
        self.message = message
        super().__init__(self.message)