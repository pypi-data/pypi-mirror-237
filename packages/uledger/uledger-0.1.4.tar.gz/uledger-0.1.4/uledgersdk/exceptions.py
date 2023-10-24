class InvalidSeedException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidWordCount(Exception):
    def __init__(self, message):
        super().__init__(message)
