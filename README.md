# 0x00. AirBnB clone - The console
### Group project	Python	OOP
### Project Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

-put in place a parent class (called BaseModel) to take care of the
initialization, serialization and deserialization of your future instances
-create a simple flow of serialization/deserialization:
Instance <-> Dictionary <-> JSON string <-> file
-create all classes used for AirBnB (User, State, City, Place…)
that inherit from BaseModel
-create the first abstracted storage engine of the project: File storage.
-create all unittests to validate all our classes and storage engine
### Installation
You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
'''https://github.com/Mesele9/AirBnB_clone'''
### Testing
Unittests for the AirBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:
'''$ python3 unittest -m discover tests'''
Alternatively, you can specify a single test file to run at a time:
'''$ python3 unittest -m tests/test_console.py'''
### How to Use It
It can work in two different modes:
Interactive and Non-interactive.
#### - Interactive Mode
In Interactive mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.
'''$ ./console.py
(hbnb) help

###### Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$'''
#### - Non-Interactive Mode
.In Non-interactive mode, the shell will need to be run with a command input
piped into its execution so that the command is run as soon as the Shell starts.
In this mode no prompt will appear, and no further input will be expected from
the user.
'''$ echo "help" | ./console.py
(hbnb)

###### Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

###### Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$...
### Examples
