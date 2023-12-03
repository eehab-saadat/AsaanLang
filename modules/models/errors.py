class Error:
    def __init__(self, name, message):
        self.name = name
        self.message = message
    def to_dict(self):
        return {"name": self.name, "message": self.message}