# Matchday Results

A command-line application that reads a stream of match results for a soccer league. At the end of each matchday, the application prints the top 3 teams in the league.

## Table of Contents
* [System Requirements](#system-requirements)
* [Getting Started](#getting-started)
* [Program Execution](#program-execution)
* [Running the Tests](#running-the-tests)
* [Demo](#demo)
* [Resources](#resources)

## System Requirements <a name="system-requirements"></a>
`matchday` was built and tested in an OS X environment running Python 3.8.4. It requires Python 3.

## Getting Started <a name="getting-started"></a>
Clone the repo and install dependencies.
```
git clone https://github.com/bisonhubert/matchday.git && cd matchday && ./install.sh
```

## Program Execution <a name="program-execution"></a>
There are two ways to supply input to the `matchday` command. You can pipe the contents of a file as input, or supply a path to a file as an argument to the command.

For convenience, there are two scripts to handle running the program. If no file or filepath is provided, the program will run with sample input.

1a. Pipe to stdin using sample file
```
./run_stdin.sh
```

1b. Pipe to stdin using your own file 
```
./run_stdin.sh <path-to-file>
```

1c. Run with the command, bypassing the script
```
cat <path-to-file> | matchday
```

2a. Filepath script using sample file
```
./run_filepath.sh
```
2b. Filepath script using your own file
```
./run_filepath.sh <path-to-file>
```

2c. Run with the command, bypassing the script
```
matchday <path-to-file>
```

## Running the Tests <a name="running-the-tests"></a>
Tests are written using `pytest`, which is included in the install script. If you see an error complaining that `pytest` is missing, make sure you have installed the dependency using `./install.sh`.

You can run the tests with a command script, using the `pytest` command, or selecting fiels and tests to run individually.

1a. Using the test script
```
./test.sh
```

1b. Running a particular file
```
./test.sh tests/test_sample_input.py
```

1c. Running a single test within a file
```
./test.sh tests/service_objects/test_matchday_interface.py::test_matchday_interface_init
```

1d. You can also just use `pytest`
```
pytest
pytest tests/test_sample_input.py
pytest tests/service_objects/test_matchday_interface.py::test_matchday_interface_init
```

## Demo <a name="demo"></a>

![program-demo](./assets/demo.gif)

## Resources <a name="resources"></a>
* [Project Requirements](./PROMPT.md)
* [Design Doc](./DESIGN_DOC.md)
* [Whiteboard](https://github.com/bisonhubert/matchday/blob/main/DESIGN_DOC.md#whiteboard)
* [Python's dataclasses library](https://docs.python.org/3.8/library/dataclasses.html)
* [Rubular](https://rubular.com/), a regex editor
* [Black](https://github.com/psf/black), a Python code formatter
