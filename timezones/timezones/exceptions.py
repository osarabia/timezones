

class DoesNotExists(Exception):
    """Does Not Exists"""

    def __init__(self, message="Does Not Exists"):
        self.message = message

    def to_dict(self):
        return {
                   "message": self.message
               }

class MissingField(Exception):
    """Missing Field"""

    def __init__(self, message="Missing Field"):
        self.message = message

    def to_dict(self):
        return {
                   "message": self.message
               }

class UnExpectedType(Exception):
    """UnExpectedType"""

    def __init__(self, message="UnExpectedType"):
        self.message = message

    def to_dict(self):
        return {
                   "message": self.message
               }

class ServiceFailed(Exception):
    """Service Failed"""

    def __init__(self, message="Service Failed"):
        self.message = message

    def to_dict(self):
        return {
                   "message": self.message
               }


