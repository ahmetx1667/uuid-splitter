import argparse
import sys
from uuidparser.core import parse_uuid, uuid_from_high_low, uuid_from_raw_string

def print_result(res, output="uuid"):
    if output == "uuid":
        print(res["uuid"])
    elif output == "bits":
        print(f"High Bits : {res['high_bits_hex']} (dec: {res['high_bits_dec']})")
        print(f"Low  Bits : {res['low_bits_hex']} (dec: {res['low_bits_dec']})")
    elif output == "raw":
        print(f"Raw String (latin1): {res['raw_string']}")
        print(f"Raw Bytes (hex)   : {res['raw_bytes'].hex()}")
    elif output == "all":
        print(f"UUID             : {res['uuid']}")
        print(f"High Bits (hex)  : {res['high_bits_hex']} (dec: {res['high_bits_dec']})")
        print(f"Low  Bits (hex)  : {res['low_bits_hex']} (dec: {res['low_bits_dec']})")
        print(f"Raw String (latin1): {res['raw_string']}")
        print(f"Raw Bytes (hex)   : {res['raw_bytes'].hex()}")

def main():
    parser = argparse.ArgumentParser(
        description="UUID parser & converter supporting various input/output formats."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-u", "--uuid",
        help="UUID string (with or without dashes, 32 hex chars)"
    )
    group.add_argument(
        "-hl", "--highlow", nargs=2, metavar=('HIGHBITS', 'LOWBITS'), type=str,
        help="HighBits and LowBits as decimal or hex"
    )
    group.add_argument(
        "-r", "--raw", type=str,
        help="Raw 16-character latin1 string"
    )

    parser.add_argument(
        "-o", "--output", choices=["uuid", "bits", "raw", "all"],
        help="Output format (default 'all' for -u, 'uuid' for -hl and -r)."
    )

    args = parser.parse_args()

    try:
        if args.uuid:
            res = parse_uuid(args.uuid)
            output = args.output if args.output else "all"
            print_result(res, output)
        elif args.highlow:
            res = uuid_from_high_low(args.highlow[0], args.highlow[1])
            output = args.output if args.output else "uuid"
            print_result(res, output)
        elif args.raw:
            res = uuid_from_raw_string(args.raw)
            output = args.output if args.output else "uuid"
            print_result(res, output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
