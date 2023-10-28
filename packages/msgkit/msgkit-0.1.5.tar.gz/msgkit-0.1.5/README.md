## MSGKIT

MsgKit is a Python library that provides you with in-code solutions to your bugs. It utilizes the OpenAI API by feeding in your code, the error, and getting a response at run-time.

## Features

- Import the logger object and use any of the documented functions

## Installation

All that is needed to use MsgKit is:
```sh
pip install msgkit
```

## Example usage:
```
from msgkit.logging import logger as l

l.giveCode(['directory']) #Gives the name of the directory which contains the files of the code.
l.debuglog('The DFS is not working correctly') #Give it the bug
```
Result:
`The bug in the code for testfile.py is that the print statement in line 15, intended to add the node to the visited set, is placed inside the "if" statement instead of outside. To fix the bug, move line 15 outside the "if" statement.`

## Development

Want to contribute? Create a new issue and/or make a pull request.

## License

MIT
