from .db import SessionLocal
from .models import Contact
from sqlalchemy import or_, select

def add_contact(**kwargs):
    with SessionLocal() as session:
        c = Contact(**kwargs)
        session.add(c)
        session.commit()
        session.refresh(c)
        return c

def get_contact(contact_id):
    with SessionLocal() as session:
        return session.get(Contact, contact_id)

def list_contacts(limit=100, offset=0):
    with SessionLocal() as session:
        stmt = select(Contact).limit(limit).offset(offset)
        return session.execute(stmt).scalars().all()

def update_contact(contact_id, **fields):
    with SessionLocal() as session:
        c = session.get(Contact, contact_id)
        if not c:
            return None
        for k, v in fields.items():
            if v is not None:
                setattr(c, k, v)
        session.add(c)
        session.commit()
        session.refresh(c)
        return c

def delete_contact(contact_id):
    with SessionLocal() as session:
        c = session.get(Contact, contact_id)
        if not c:
            return False
        session.delete(c)
        session.commit()
        return True

def search_contacts(q, limit=100):
    with SessionLocal() as session:
        stmt = select(Contact).where(
            or_(
                Contact.first_name.ilike(f"%{q}%"),
                Contact.last_name.ilike(f"%{q}%"),
                Contact.email.ilike(f"%{q}%"),
                Contact.phone.ilike(f"%{q}%")
            )
        ).limit(limit)
        return session.execute(stmt).scalars().all()
