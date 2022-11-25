import sys
from matchday.dataclasses import SoccerMatch
from matchday.service_objects import Sample


def main():
    print("in main")
    args = sys.argv[1:]
    print("count of args :: {}".format(len(args)))
    for arg in args:
        print("passed argument :: {}".format(arg))

    match = SoccerMatch(original_record="original record")
    print("match", match)

    sample = Sample()
    print("sample", sample)


if __name__ == "__main__":
    main()
