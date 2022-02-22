from typing import Tuple
from . import ArgFlag, ArgOption, ArgValsEnum, UserError

class ArgsParser:
  """Represents a parser of command line arguments."""

  def __init__(self) -> None:
    """Initialize a new arguments parser with no options."""
    self.__options = []
    """An array of parseable options."""

  def __longOpt(self, opts: dict, i: int, *args: str) -> int:
    """
    Parses a long option at a given index, and adds the fitting option object
    paired with a list of arguments it requires, to the options dictionary.

    param `opts`: A dictionary of options paired with their respective
      additional arguments.
    param `i`: The index of the option that is currently being parsed.
    param `args`: The arguments being parsed.
    return: The index of the next option to parse.
    """
    name = args[i][2:] #Without the `--`.
    opt = None

    for option in self.__options:
      if option.long == name:
        opt = option
        break
    if opt == None: raise UserError.unknownLOpt(name)

    #The i+1 is to move to the arguments of the option.
    return self.__opt(opts, opt, i + 1, *args)
  
  def __shortOptArg(self, opts: dict, i: int, *args: str) -> int:
    """
    Parses a group of short options at a given index, and adds the fitting
    option objects paired with a list of arguments each option requires, to
    the options dictionary.

    param `opts`: A dictionary of options paired with their respective
      additional arguments.
    param `i`: The index of the option group that is currently being parsed.
    param `args`: The arguments being parsed.
    return: The index of the next option to parse.
    """
    for shorti in range(1, len(args[i])):
      index = self.__shortOpt(opts, i, shorti, *args)
    return index
  
  def __shortOpt(self, opts: dict, i: int, shorti: int, *args: str) -> int:
    """
    Parses a short option at a given index, and adds the fitting option object
    paired with a list of arguments it requires, to the options dictionary.

    param `opts`: A dictionary of options paired with their respective
      additional arguments.
    param `i`: The index of the option that is currently being parsed.
    param `shorti`: The index of the option inside the group.
    param `args`: The arguments being parsed.
    return: The index of the next option to parse.
    """
    arg = args[i]
    letter = arg[shorti]
    opt = None

    for option in self.__options:
      if option.short == letter:
        opt = option
        break
    if opt == None: raise UserError.unknownSOpt(letter)

    if opt.valuesRequired != ArgValsEnum.NONE and not arg.endswith(letter):
      raise UserError.argOptMiddle(letter, arg)
    return self.__opt(opts, opt, i + 1, *args)

  def __opt(self, opts: dict, opt: ArgOption, i: int, *args: str) -> int:
    """
    Hadles an Option object and ads it to the options dictionary, together
    with the arguments it requires.

    param `opts`: A dictionary of options paired with their respective
      additional arguments.
    param `opt`: The option that is currently being handled.
    param `i`: The index of the arguments the option requires.
    param `args`: The arguments being parsed.
    return: The index of the next option to parse.
    """
    optArgs = opts[opt.long] if opt.long in opts else []

    if opt.valuesRequired == ArgValsEnum.ONE:
      if i >= len(args) or args[i].startswith("-"):
        raise UserError.argsRequired(opt.long)
      if len(optArgs) >= 1:
        raise UserError(f"Option `--{opt.long}` only requires ONE argument.")
      optArgs.append(args[i])
      i += 1
    elif opt.valuesRequired == ArgValsEnum.MANY:
      while not args[i].startswith("-"):
        optArgs.append(args[i])
        i += 1
      if len(optArgs) == 0: raise UserError.argsRequired(opt.long)
    
    opts[opt.long] = optArgs
    return i

  
  def addOption(self, long: str, short: str = ""
  , required: ArgValsEnum = ArgValsEnum.ONE) -> "ArgsParser":
    """
    Add an option to the list of known options.
    
    param `long`: The long version of the option. Without `--`.
    param `short`: Optional. The short version of the option. Without `-`.
    param `required`: Optional. The amount of aditional arguments required by
      the option.
    """
    opt = ArgOption().setLong(long).setValuesRequired(required)
    if (short != ""): opt.setShort(short)
    self.__options.append(opt)
    return self
  
  def addFlag(self, long: str, short: str = None) -> "ArgsParser":
    """
    Add a flag to the list of known options.
    
    param `long`: The long version of the option. Without `--`.
    param `short`: Optional. The short version of the option. Without `-`.
    """
    opt = ArgFlag().setLong(long)
    if (short != ""): opt.setShort(short)
    self.__options.append(opt)
    return self

  def parse(self, *args: str) -> Tuple[dict, list]:
    """
    Parse the arguments of a command.
    
    param `args`: The arguments to parse.
    return: A pair of a dictionary and a list. The dictionary is all the
      options paired with their respective additional arguments. The list is
      all the remaining arguments that don't belong to any option.
      The options in the dictionary are strings of the long version of the
      option.
    """
    rest = []
    opts = {}
    i = 0
    while (i < len(args)):
      if args[i].startswith("--"):
        i = self.__longOpt(opts, i, *args)
      elif args[i].startswith("-"):
        i = self.__shortOptArg(opts, i, *args)
      else:
        rest.append(args[i])
        i += 1
    return (opts, rest)
