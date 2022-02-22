class UserError(BaseException):
  """Represents an error in the input of a command."""

  def __init__(self, message: str) -> None:
    """Initializes a new user error with a message."""
    self.__message = message
    """The message of the error."""
  
  @property
  def message(self) -> str:
    """The message of the error."""
    return self.__message
  
  @staticmethod
  def wrongArgNumber() -> "UserError":
    """Generate a user error about an incorrect number of arguments."""
    return UserError("Wrong number of arguments.")

  @staticmethod
  def argsRequired(opt: str) -> "UserError":
    """
    Generate a user error about a lack of arguments.

    param `opt`: The option that requires arguments.
    """
    return UserError(f"Option `--{opt}` requires arguments.")
  
  @staticmethod
  def unknownSOpt(opt: str) -> "UserError":
    """Generate a user error about an unknown short option."""
    return UserError(f"Unknown option `-{opt}`.")
  
  @staticmethod
  def unknownLOpt(opt: str) -> "UserError":
    """Generate a user error about an unknown long option."""
    return UserError(f"Unknown option `--{opt}`.")
  
  @staticmethod
  def argOptMiddle(opt: str, arg: str) -> "UserError":
    """
    Generate a user error about a short option that requires arguments being
    in the middle of a option group. Example: option `-dfn` where `-f` requires
    an argument.

    param `opt`: The option that was in the middle.
    param `arg`: The entire argument.

    In the above example 'f' would be `opt` and 'dfh' would be `arg`.
    """
    return UserError(f"Option `-{opt}` requires arguments," + \
      f"but is in the middle of the options: `{arg}`.")