import uuid
import re

UUID_REGEX = re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)

def validate_uuid_string(uuid_string):
    clean_str = uuid_string.replace('-', '').lower()
    return bool(UUID_REGEX.fullmatch(clean_str))

def parse_numeric_input(value):
    if isinstance(value, int):
        return value
    value_str = str(value).lower()
    if value_str.startswith('0x'):
        return int(value_str, 16)
    if len(value_str) == 16 and all(c in '0123456789abcdef' for c in value_str):
        return int(value_str, 16)
    return int(value_str)

def extract_uuid_info(uuid_obj):
    full_int_value = uuid_obj.int
    high_bits = (full_int_value >> 64) & ((1 << 64) - 1)
    low_bits = full_int_value & ((1 << 64) - 1)
    raw_bytes = uuid_obj.bytes
    raw_string = raw_bytes.decode('latin1', errors='replace')
    return {
        "uuid": str(uuid_obj),
        "high_bits_hex": f"{high_bits:016x}",
        "high_bits_dec": high_bits,
        "low_bits_hex": f"{low_bits:016x}",
        "low_bits_dec": low_bits,
        "raw_bytes": raw_bytes,
        "raw_string": raw_string
    }

def parse_uuid(uuid_string):
    if not validate_uuid_string(uuid_string):
        raise ValueError("Invalid UUID format. Expected 32 hexadecimal characters.")
    return extract_uuid_info(uuid.UUID(hex=uuid_string))

def uuid_from_high_low(high_input, low_input):
    high_bits = parse_numeric_input(high_input)
    low_bits = parse_numeric_input(low_input)
    for name, value in [("High", high_bits), ("Low", low_bits)]:
        if not (0 <= value < 2**64):
            raise ValueError(f"{name} bits must be a 64-bit unsigned integer.")
    full_int_value = (high_bits << 64) | low_bits
    return extract_uuid_info(uuid.UUID(int=full_int_value))

def uuid_from_raw_string(raw_string):
    if not isinstance(raw_string, str):
        raise TypeError("Raw input must be a string.")
    if len(raw_string) != 16:
        raise ValueError("Raw string must be exactly 16 characters.")
    raw_bytes = raw_string.encode('latin1', errors='replace')
    return extract_uuid_info(uuid.UUID(bytes=raw_bytes))