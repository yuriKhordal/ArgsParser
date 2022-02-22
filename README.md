# ArgsParser
A python library for parsing command line like arguments.

# Usage
To use the library copy the `argsparser` directory into your project. to use any of the class use
```Python
from argsparser import [ClassName]
```

## Parsing
Let's imagine a copy command that shows a help message with the `--help` or `-h` flag, can specify a single
source directory with the `--source` or `-s` option, and multiple target directories with the `--dirs` or `-d`
option, and the rest of the arguments are treated as files to copy.
To parse the arguments the command can take, first you need to create a parser and add the options to it.  
```python
from argsparser import ArgsParser

# The methods return `self` and thus can be chained infinitely.
parser = ArgsParser().addFlag("help", "h").addOption("source", "s", ArgValsEnum.ONE).addOption("dirs", "d", ArgValsEnum.MANY)
```

After creating the parser we can use it to parse a command string and find out which options were specified and what
arguments those options hold. Let's say we want to parse the following command:  
`copy file1.txt file2.py file3.png --source /path/to/files -d ./dir1 ./dir2`
```python
command = "copy file1.txt file2.py file3.png --source /path/to/files -d ./dir1 ./dir2"
argList = command.split()[1:] # Drop the command name to get the list of arguments.
(options, arguments) = parser.parse(*argList)

if "help" in options:
  # Print help message.

source = "./"
if "source" in options:
  source = options["source"][0] # Only requires one argument so it's the first and only item in the list.

dirs = ["./"]
if "dirs" in options:
  dirs = options["dirs"]

for fileName in arguments:
  for dir in dirs:
    filePath = path.join(source, fileName)
    copy(filePath, dir)
```

The `parse` method returns two values. The first is a dictionary that maps the options found in command string to the arguments
each option requires, and the second is a list of all the rest of the arguments which are arguments to the command itself.  
For the afforementioned copy command the return value of parse would be:
```python
options = {
  "source": ["/path/to/files"],
  "dirs": ["./dir1", "./dir2"]
}
arguments = ["file1.txt", "file2.py", "file3.png"]
```
* Note: Notice the lack of a "help" key in `options`. Since a `--help` of `-h` flag wasn't specified it was not added to the dictionary.
