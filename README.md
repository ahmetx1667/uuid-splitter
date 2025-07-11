# UUID Splitter

A powerful Python CLI tool and library to parse and convert UUIDs into high and low 64-bit parts, raw Latin1 string representation, and back. Perfect for developers needing detailed UUID manipulation and analysis.

---

## Features

- Parse UUID strings (with or without dashes) into:
  - High 64 bits (hex and decimal)
  - Low 64 bits (hex and decimal)
  - Raw 16-byte Latin1 string and byte array
- Construct UUID from high and low 64-bit integers
- Convert raw Latin1 string back to UUID and its parts
- Flexible CLI interface with multiple input/output formats

---

## Installation

Clone this repository and install dependencies (if any):

```bash
git clone https://github.com/ahmetx1667/uuid-splitter.git
cd uuid-splitter
# No external dependencies currently
````

You can run the CLI tool directly using Python:

```bash
python cli.py -u 98aaf3ac-5960-4674-8f7a-3d05c9d9e7ed -o all
```

---

## Usage

### CLI Options

```bash
usage: cli.py [-h] (-u UUID | -hl HIGHBITS LOWBITS | -r RAW) [-o {uuid,bits,raw,all}]

UUID parser & converter supporting various input/output formats.

optional arguments:
  -h, --help            show this help message and exit
  -u UUID, --uuid UUID  UUID string (with or without dashes, 32 hex chars)
  -hl HIGHBITS LOWBITS, --highlow HIGHBITS LOWBITS
                        HighBits and LowBits as decimal or hex
  -r RAW, --raw RAW     Raw 16-character latin1 string
  -o {uuid,bits,raw,all}, --output {uuid,bits,raw,all}
                        Output format (default 'all' for -u, 'uuid' for -hl and -r).
```

### Examples

* Parse UUID string and show all details:

```bash
python cli.py -u 98aaf3ac-5960-4674-8f7a-3d05c9d9e7ed
```

* Convert high and low bits back to UUID:

```bash
python cli.py -hl 11000872961365263988 10338642989653026797 -o uuid
```

* Show raw Latin1 string from UUID:

```bash
python cli.py -u 98aaf3ac-5960-4674-8f7a-3d05c9d9e7ed -o raw
```

---

## Library Usage

Import functions from `uuidparser.core` in your Python code:

```python
from uuidparser.core import parse_uuid, uuid_from_high_low, uuid_from_raw_string

res = parse_uuid("98aaf3ac-5960-4674-8f7a-3d05c9d9e7ed")
print(res["high_bits_hex"])
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
