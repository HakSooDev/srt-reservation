from srt_reservation.main import SRT
from srt_reservation.cli_parser import parse_cli_args
from srt_reservation.validation import validate_args

if __name__ == "__main__":
    try:
        args = parse_cli_args()
        validate_args(args)
        srt = SRT(args)
        srt.run()

    except Exception as e:
        print(e)
        exit(1)
