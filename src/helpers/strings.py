import binascii

def are_texts_equals(old: str, new) -> bool:
    encoding = 'utf8'
    old_text = binascii.crc32(old.encode(encoding))
    new_text = binascii.crc32(new.encode(encoding))
    return old_text == new_text