import csv
from .repository import add_contact, list_contacts

CSV_HEADER = ["first_name","last_name","email","phone","address","notes"]

def import_from_csv(path):
    added=[]
    errors=[]
    with open(path, newline='', encoding='utf-8') as f:
        reader=csv.DictReader(f)
        for i,row in enumerate(reader, start=1):
            try:
                data={k:(row.get(k) or None) for k in CSV_HEADER}
                if not data.get("first_name") or not data.get("last_name"):
                    raise ValueError("first_name and last_name are required")
                c=add_contact(**data)
                added.append(c)
            except Exception as e:
                errors.append((i,str(e)))
    return added,errors

def export_to_csv(path):
    contacts=list_contacts(limit=10000)
    with open(path,"w",newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(CSV_HEADER)
        for c in contacts:
            writer.writerow([c.first_name,c.last_name,c.email or "",c.phone or "",c.address or "",c.notes or ""])
    return len(contacts)
