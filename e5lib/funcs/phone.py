def phone_purge(phone: str) -> str | None:
    """
    Purge phone number from all non-digit symbols  
    Convert 8XXXXXXXXXX to 7XXXXXXXXXX  
    Add 7 to the beginning of the number has 10 digits  
    Support only Russian ans Kazakhstan phone numbers
    """
    if not phone or not isinstance(phone, str):
        return None
    phone = ''.join(filter(str.isdigit, phone))
    l = len(phone)
    if l > 11 or l < 10:
        return None
    if l == 10 and phone[0] == "9":
        phone = "7" + phone
    if phone[0] == "8":
        phone = "7" + phone[1:]
    return phone

def create_phone_vars(phone: str, formats: str) -> list[str] | None:
    """
    Create number format conbinations based on origin phone

    :param phone: Phone number
    :param formats: List of phone number formats. Supports '*' key. Examples: '1234', '245', '*'

    Formats
    -------
    - 7XXXXXXXXXX - base format
    - `1`: +7XXXXXXXXXX
    - `2`: +7 (XXX) XXX-XXXX
    - `3`: +7 (XXX) XXX-XX-XX
    - `4`: 8XXXXXXXXXX
    - `5`: XXXXXXXXXX
    """
    if not formats or not isinstance(formats, str):
        raise ValueError("formats is empty or not a string")
    phone = phone_purge(phone)
    if not phone:
        return None
    phones = [phone]
    if '*' in formats:
        formats = '12345'
    if '1' in formats:
        phones.append(f"+{phone}")
    if '2' in formats:
        phones.append(f"+{phone[:1]} ({phone[1:4]}) {phone[4:7]}-{phone[7:11]}")
    if '3' in formats:
        phones.append(f"+{phone[:1]} ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9:11]}")
    if '4' in formats:
        phones.append(f"8{phone[1:]}")
    if '5' in formats:
        phones.append(phone[1:])
    return phones