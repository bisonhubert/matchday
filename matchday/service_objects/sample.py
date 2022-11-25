class Sample:
    def __init__(self):
        self.name = "sample service object"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"
