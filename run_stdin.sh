#/bin/bash
FILEPATH=${1:-tests/mock_data/sample-input.txt}
cat $FILEPATH | matchday
