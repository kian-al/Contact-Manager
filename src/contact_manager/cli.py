import click
from .db import init_db
from .repository import add_contact, list_contacts, get_contact, update_contact, delete_contact, search_contacts

@click.group()
def cli():
    pass

@cli.command()
@click.option("--first", required=True)
@click.option("--last", required=True)
@click.option("--email")
@click.option("--phone")
@click.option("--address")
@click.option("--notes")
def add(first,last,email,phone,address,notes):
    c=add_contact(first_name=first,last_name=last,email=email,phone=phone,address=address,notes=notes)
    click.echo(f"Added: {c.id}")

@cli.command(name="list")
def list_cmd():
    for c in list_contacts():
        click.echo(f"{c.id} {c.first_name} {c.last_name}")

@cli.command()
@click.argument("contact_id", type=int)
def get(contact_id):
    c=get_contact(contact_id)
    if not c: click.echo("Not found"); return
    click.echo(f"{c.id} {c.first_name} {c.last_name} {c.email}")

@cli.command()
@click.argument("contact_id", type=int)
@click.option("--first")
@click.option("--last")
@click.option("--email")
@click.option("--phone")
@click.option("--address")
@click.option("--notes")
def update(contact_id,first,last,email,phone,address,notes):
    c=update_contact(contact_id, first_name=first,last_name=last,email=email,phone=phone,address=address,notes=notes)
    if not c: click.echo("Not found"); return
    click.echo("Updated")

@cli.command()
@click.argument("contact_id", type=int)
def delete(contact_id):
    ok=delete_contact(contact_id)
    click.echo("Deleted" if ok else "Not found")

@cli.command()
@click.argument("q")
def search(q):
    for c in search_contacts(q):
        click.echo(f"{c.id} {c.first_name} {c.last_name}")

@cli.command()
@click.argument("path")
def import_csv(path):
    a,e=import_from_csv(path)
    click.echo(f"Imported {len(a)}")

@cli.command()
@click.argument("path")
def export_csv(path):
    n=export_to_csv(path)
    click.echo(f"Exported {n}")

@cli.command()
def init():
    init_db()
    click.echo("DB initialized")
