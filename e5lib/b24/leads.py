import re
from au_b24.funcs import get_leads, get_contacts
from e5lib.funcs import phone_purge


def get_phone_vars(phone: str | int, variants: str = "*"):
    """Return selected Russian-style formats for *p*.

    Variant map:
      1  71234567890
      2  +71234567890
      3  +7 (123) 456-7890
      4  +7 (123) 456-78-90
      5  81234567890
      6  1234567890

    *variants* accepts:
      • '*' → all six (default)
      • any string of digits/comma-separated list, e.g. '13', '1,3,5'
        (order in output is always 1→6)
    """
    phone = re.sub(r"\D", "", str(phone))
    if len(phone) == 11 and phone[0] == "8":
        phone = "7" + phone[1:]
    if len(phone) != 11:
        return []

    c, a, b, l = phone[0], phone[1:4], phone[4:7], phone[7:]
    forms = [
        phone,
        f"+{phone}",
        f"+{c} ({a}) {b}-{l}",
        f"+{c} ({a}) {b}-{l[:2]}-{l[2:]}",
        f"8{phone[1:]}",
        phone[1:],
    ]

    if variants == "*":
        return forms

    wanted = {int(d) - 1 for d in re.findall(r"\d", variants) if "1" <= d <= "6"}
    return [forms[i] for i in range(6) if i in wanted]


def get_leads_by_phone(
    phone: str | int,
    filters: dict,
    select: list,
    variants: str = "*",
    search_by_contacts: bool = False,
) -> list[dict] | None:
    if not isinstance(filters, dict):
        raise ValueError(f"filters must be dict, not {type(filters)}")
    filters = filters.copy()
    leads_result = []
    phone_list = get_phone_vars(phone=phone, variants=variants)
    for entry in phone_list:
        filters["PHONE"] = entry
        leads = get_leads(filters=filters, select=select, order="DESC")
        if leads:
            leads_result.extend(leads)

    if search_by_contacts:
        del filters["PHONE"]
        for entry in phone_list:
            contact_filters = {"PHONE": entry}
            contact_select = ["ID"]
            contacts = get_contacts(
                filters=contact_filters, select=contact_select, order="DESC"
            )
            for contact in contacts:
                contact_id = contact.get("ID")
                if contact_id:
                    filters["CONTACT_ID"] = contact_id
                    leads = get_leads(filters=filters, select=select, order="DESC")
                    if leads:
                        leads_result.extend(leads)
    result = {}
    for lead in leads_result:
        lead_id = lead.get("ID")
        if lead_id and lead_id not in result:
            result[lead_id] = lead
    return sorted(list(result.values()), key=lambda x: x["ID"], reverse=True)
