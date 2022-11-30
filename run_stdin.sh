#/bin/bash

# This script will:

# Run the matchday application with sample input
# Example: $ ./run_stdin.sh

# Or it will run the matchday application using a file provided as input
# Example: $ ./run_stdin.sh <path-to-file>

FILEPATH=${1:-tests/mock_data/sample-input.txt}
cat $FILEPATH | matchday
