class DBError(ValueError):
    def __init__(self, detail: str):
        self.detail = detail
