from loggerDO import LoggerDO

class logit:
  def __init__(self, function) -> None:
    self.function = function

  def __call__(self, *args: any, **kwargs: any) -> any:
    with LoggerDO() as db:
      db.LogMethodCall(self.function.__name__, kwargs["user"])
    
    return self.function(*args, **kwargs)
