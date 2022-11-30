#/bin/bash

# This script will:

# 1. Run all tests
# $ ./test.sh

# 2. Run a directory of tests
# $ ./test.sh tests/service_objects/

# 3. Run a test file 
# $ ./test.sh tests/test_sample_input.py

# 4. Run a single test
# $ ./test.sh tests/service_objects/test_matchday_interface.py::test_matchday_interface_init

pytest "$@"
