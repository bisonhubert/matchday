import sys

from matchday.service_objects import MatchRecordParser, MatchdayInterface


def handle_stdin():
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
    args = sys.argv[1:]
    if len(args) == 0:
        handle_stdin()
    else:
        filepath = args[0]
        handle_filepath(filepath)


if __name__ == "__main__":
    main()
