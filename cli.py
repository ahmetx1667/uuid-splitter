import argparse
import sys
import re
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

    # Burada pozisyonel args olarak alalım:
    parser.add_argument(
        "inputs", nargs="*", 
        help="Input arguments: either one UUID string or two high/low bits"
    )

    parser.add_argument(
        "-u", "--uuid",
        help="UUID string (with or without dashes, 32 hex chars)"
    )
    parser.add_argument(
        "-hl", "--highlow", nargs=2, metavar=('HIGHBITS', 'LOWBITS'), type=str,
        help="HighBits and LowBits as decimal or hex"
    )
    parser.add_argument(
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
        else:
            if len(args.inputs) == 1:
                input_str = args.inputs[0]
                is_valid_uuid_pattern = re.compile(r'^[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{12}$')
                if bool(is_valid_uuid_pattern.match(input_str)):
                    res = parse_uuid(input_str)
                    output = args.output if args.output else "all"
                    print_result(res, output)
                else:
                    print(f"Input '{input_str}' is not a valid UUID.", file=sys.stderr)
                    sys.exit(1)

            elif len(args.inputs) == 2:
                def parse_int(value: str) -> int:
                    value = value.lower().strip()
                    try:
                        if value.startswith("0x"):
                            return int(value, 16)
                        else:
                            return int(value, 10)
                    except ValueError:
                        try:
                            return int(value, 16)
                        except ValueError:
                            raise ValueError(f"Invalid integer value: {value}")

                high = parse_int(args.inputs[0])
                low = parse_int(args.inputs[1])
                res = uuid_from_high_low(high, low)
                output = args.output if args.output else "uuid"
                print_result(res, output)

            else:
                parser.print_help()
                sys.exit(1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()