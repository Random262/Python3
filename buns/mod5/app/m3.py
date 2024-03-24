class BlockErrors:
    def __init__(self, ignored):
        self.ignored = ignored

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.ignored):
            return True
        return False
