from . import ArgValsEnum

class ArgOption:
  """Represents a command line option/flag."""

  def __init__(self) -> None:
    """Initializes a new argument."""
    self.__short = ''
    """
    The short version of the option. Without `-`.
    Type: `str`.
    """
    self.__long = ''
    """
    The long version of the option. Without `--`.
    Type: `str`.
    """
    self.__require = ArgValsEnum.NONE
    """
    Whether the option requires extra arguments.
    Type: `ArgValsEnum`.
    """
  
  @property
  def short(self) -> str:
    """The short verion of the option."""
    return self.__short

  @property
  def long(self) -> str:
    """The long version of the option."""
    return self.__long

  @property
  def valuesRequired(self) -> ArgValsEnum:
    """The amount of values required by the argument."""
    return self.__require

  def setShort(self, short: str) -> "ArgOption":
    """Set the short version of the option."""
    if not isinstance(short, str):
      raise TypeError(short)
    if len(short) != 1:
      raise ValueError(f"Length of 'short' is {short.length}," + \
        " expected a single character.")
    self.__short = short
    return self

  def setLong(self, long: str) -> "ArgOption":
    """Set the long version of the option."""
    if not isinstance(long, str):
      raise TypeError(long)
    self.__long = long
    return self

  def setValuesRequired(self, required: ArgValsEnum) -> "ArgOption":
    """Set the amount of values required by the argument."""
    if not isinstance(required, ArgValsEnum):
      raise TypeError(required)
    self.__require = required
    return self

class ArgFlag(ArgOption):
  """Represents a command line flag."""

  def __init__(self) -> None:
    """Initializes a new flag."""
    super().__init__()
    self.__require = ArgValsEnum.NONE