def string_to_16_bytes(s):
    # Convert the string to bytes
    byte_data = s.encode('utf-8')
    # Pad with null bytes if the length is less than 16
    if len(byte_data) < 16:
        byte_data = byte_data.ljust(16, b'\0')
    # Truncate if the length is more than 16
    elif len(byte_data) > 16:
        byte_data = byte_data[:16]
    return byte_data

def bytes_to_string(b):
    # Strip the null bytes and convert back to string
    s = b.rstrip(b'\0').decode('utf-8')
    return s

# Example usage
original_string = "172.16.134.16"
byte_data = string_to_16_bytes(original_string)
print(byte_data)  # Output will be: b'172.16.134.16\x00\x00\x00'
print(len(byte_data))  # Output will be: 16
reconstructed_string = bytes_to_string(byte_data)
print(reconstructed_string)  # Output will be: 172.16.134.16