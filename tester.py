from argsparser import ArgValsEnum, ArgsParser
from argsparser.UserError import UserError

def main():
  args = ["hello", "-d", "dir1", "dir2", "dir3", "-hcf", "file.py",
    "--go", "order", "cheese"]
  parser = ArgsParser().addOption("dirs", "d", ArgValsEnum.MANY) \
    .addFlag("help", "h").addFlag("cart", "c") \
    .addOption("file", "f", ArgValsEnum.ONE).addFlag("go", "g")
  tup = parser.parse(*args)
  print(tup)

  try:
    args = ["hello", "-d", "dir1", "dir2", "dir3", "-hfc", "file.py",
      "--go", "order", "cheese"]
    tup = parser.parse(*args)
    print(tup)
  except UserError as err:
    print(err)

  try:
    args = ["hello", "-d", "-hcf", "file.py",
      "--go", "order", "cheese"]
    tup = parser.parse(*args)
    print(tup)
  except UserError as err:
    print(err)

  try:
    args = ["hello", "-d", "dir1", "dir2", "dir3", "--file", "file", "-hcf",
    "file.py", "--go", "order", "cheese"]
    tup = parser.parse(*args)
    print(tup)
  except UserError as err:
    print(err)

  try:
    args = ["hello", "-t", "-d", "dir1", "dir2", "dir3", "-hcf", "file.py",
    "--go", "order", "cheese"]
    tup = parser.parse(*args)
    print(tup)
  except UserError as err:
    print(err)

  try:
    args = ["hello", "-d", "dir1", "dir2", "dir3", "-hcf", "file.py",
    "--go", "order", "cheese"]
    tup = parser.parse(*args)
    print(tup)
  except UserError as err:
    print(err)


if __name__ == "__main__":
  main()