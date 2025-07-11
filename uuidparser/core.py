import uuid
import re

UUID_REGEX = re.compile(r'^[0-9a-f]{32}$', re.I)

def validate_uuid_string(u_str: str) -> bool:
    clean = u_str.replace('-', '').lower()
    return bool(UUID_REGEX.fullmatch(clean))

def parse_uuid(u_str: str):
    clean = u_str.replace('-', '').lower()
    if not validate_uuid_string(clean):
        raise ValueError("Invalid UUID format! Expected 32 hex digits.")
    u = uuid.UUID(hex=clean)
    full_int = u.int
    high_bits = (full_int >> 64) & ((1 << 64) - 1)
    low_bits = full_int & ((1 << 64) - 1)
    raw_bytes = u.bytes
    raw_string = raw_bytes.decode('latin1', errors='replace')
    return {
        "uuid": str(u),
        "high_bits_hex": f"{high_bits:016x}",
        "high_bits_dec": high_bits,
        "low_bits_hex": f"{low_bits:016x}",
        "low_bits_dec": low_bits,
        "raw_bytes": raw_bytes,
        "raw_string": raw_string
    }

def parse_num(x):
    if isinstance(x, int):
        return x
    x = str(x).lower()
    if x.startswith('0x'):
        return int(x, 16)
    elif len(x) == 16 and all(c in '0123456789abcdef' for c in x):
        return int(x, 16)
    else:
        return int(x, 10)

def uuid_from_high_low(high_bits_input, low_bits_input):
    high_bits = parse_num(high_bits_input)
    low_bits = parse_num(low_bits_input)
    if not (0 <= high_bits < 2**64):
        raise ValueError("HighBits must be a 64-bit unsigned integer.")
    if not (0 <= low_bits < 2**64):
        raise ValueError("LowBits must be a 64-bit unsigned integer.")
    full_int = (high_bits << 64) | low_bits
    u = uuid.UUID(int=full_int)
    raw_bytes = u.bytes
    raw_string = raw_bytes.decode('latin1', errors='replace')
    return {
        "uuid": str(u),
        "high_bits_hex": f"{high_bits:016x}",
        "high_bits_dec": high_bits,
        "low_bits_hex": f"{low_bits:016x}",
        "low_bits_dec": low_bits,
        "raw_bytes": raw_bytes,
        "raw_string": raw_string
    }

def uuid_from_raw_string(raw_string):
    if not isinstance(raw_string, str):
        raise TypeError("Raw string input must be a string.")
    if len(raw_string) != 16:
        raise ValueError("Raw string input must be exactly 16 characters.")
    raw_bytes = raw_string.encode('latin1', errors='replace')
    u = uuid.UUID(bytes=raw_bytes)
    full_int = u.int
    high_bits = (full_int >> 64) & ((1 << 64) - 1)
    low_bits = full_int & ((1 << 64) - 1)
    return {
        "uuid": str(u),
        "high_bits_hex": f"{high_bits:016x}",
        "high_bits_dec": high_bits,
        "low_bits_hex": f"{low_bits:016x}",
        "low_bits_dec": low_bits,
        "raw_bytes": raw_bytes,
        "raw_string": raw_string
    }
