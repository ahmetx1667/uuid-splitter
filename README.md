# UUID Splitter

A powerful Python CLI tool and library to parse and convert UUIDs into high and low 64-bit parts, raw Latin1 string representation, and back. Perfect for developers needing detailed UUID manipulation and analysis.

---

## Features

* Parse UUID strings (with or without dashes) into:

  * High 64 bits (hex and decimal)
  * Low 64 bits (hex and decimal)
  * Raw 16-byte Latin1 string and byte array
* Construct UUID from high and low 64-bit integers (decimal or hex inputs)
* Convert raw Latin1 string back to UUID and its parts
* Validate UUID format precisely (32 hex chars, dash optional)
* Flexible CLI interface supporting multiple input and output formats
* Error handling with clear messages for invalid inputs

---

## Installation

Clone this repository and install dependencies (none currently):

```bash
git clone https://github.com/ahmetx1667/uuid-splitter.git
cd uuid-splitter
# No external dependencies currently
```

Run the CLI tool directly using Python:

```bash
python cli.py -u 98aaf3ac-5960-4674-8f7a-3d05c9d9e7ed -o all
```

---

## Usage

### CLI Options

```bash
usage: cli.py [-h] [-u UUID] [-hl HIGHBITS LOWBITS] [-r RAW] [-o {uuid,bits,raw,all}] [inputs ...]

UUID parser & converter supporting various input/output formats.

positional arguments:
  inputs                One UUID string or two high/low bits (alternative to flags)

optional arguments:
  -h, --help            show this help message and exit
  -u UUID, --uuid UUID  UUID string (with or without dashes)
  -hl HIGHBITS LOWBITS, --highlow HIGHBITS LOWBITS
                        HighBits and LowBits as decimal or hex
  -r RAW, --raw RAW     Raw 16-character Latin1 string
  -o {uuid,bits,raw,all}, --output {uuid,bits,raw,all}
                        Output format (default 'all' for UUID input, 'uuid' otherwise)
```

---

### Examples

You can use the tool with explicit flags:

```bash
python cli.py -u 98aaf3ac-5960-4674-8f7a-3d05c9d9e7ed
python cli.py -hl 11000872961365263988 10338642989653026797 -o uuid
python cli.py -r "raw_latin1_string_here" -o all
```

Or simply by passing positional arguments without flags:

```bash
python cli.py 98aaf3ac596046748f7a3d05c9d9e7ed
python cli.py 11000872961365263988 10338642989653026797
```

The tool intelligently detects whether you provided a UUID string or high/low bits based on the number and format of the positional arguments.

---

## Library Usage

Import functions from `uuidparser.core` in your Python code:

```python
from uuidparser.core import parse_uuid, uuid_from_high_low, uuid_from_raw_string

result = parse_uuid("98aaf3ac-5960-4674-8f7a-3d05c9d9e7ed")
print(result["high_bits_hex"])
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---