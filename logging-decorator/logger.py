class logit:
    def __init__(self, function) -> None:
        self.function = function

    def __call__(self, *args: any, **kwargs: any) -> any:

        return self.function(*args, **kwargs)
