from enum import Enum, unique

@unique
class ArgValsEnum(Enum):
  """
  An enum representing how many additional values an argument requires.
  """
  NONE = 0
  """The argument requires no additional values."""
  ONE = 1
  """The argument requires one additional value."""
  MANY = 2
  """
  The argument requires all values until the next argument or
  the end of the command.
  """