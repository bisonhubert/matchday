import sys

from matchday.service_objects import MatchRecordParser, MatchdayInterface


def handle_stdin():
    """
    Method that executes the matchday program from input provided by stdin.
    Sample script execution: $ cat tests/mock_data/sample-input.txt | matchday
    """
    interface = MatchdayInterface()
    while 1:
        match_record = sys.stdin.readline()
        is_stream_done = not match_record
        if is_stream_done:
            interface.run([], is_stream_done)
            break
        parser = MatchRecordParser(match_record).run()
        interface.run(parser.get_teams(), is_stream_done)


def handle_filepath(filepath):
    """
    Method that executes the matchday program from input provided by an argument to a filepath.
    Sample script execution: $ matchday tests/mock_data/sample-input.txt
    """
    file = open(filepath, "r")
    interface = MatchdayInterface()
    while 1:
        match_record = file.readline()
        is_stream_done = not match_record
        if is_stream_done:
            interface.run([], is_stream_done)
            break
        parser = MatchRecordParser(match_record).run()
        interface.run(parser.get_teams(), is_stream_done)


def main():
    """
    Main runner function that handles which type of input to stream.
    """
    args = sys.argv[1:]
    if len(args) == 0:
        handle_stdin()
    else:
        filepath = args[0]
        handle_filepath(filepath)


if __name__ == "__main__":
    main()
