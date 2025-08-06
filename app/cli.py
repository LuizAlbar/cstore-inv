import typer
import uvicorn 
from rich.table import Table
from rich.console import Console
from sqlalchemy.orm import Session
from app.database import Base, engine
from app.models import Store, PhoneNumber

cli = typer.Typer()

@cli.command()
def api():
    """Run the api"""
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload= True)

@cli.command()
def storelist():
    """Lists all stores"""
    table = Table(title= "List of Stores")
    fields = ['name','id']
    for header in fields:
        table.add_column(header, style= 'magenta')

    with Session(engine) as session:
        stores = session.query(Store).all()
        for store in stores:
            table.add_row(store.name, str(store.id))

    Console().print(table)

@cli.command()
def phonelist():
    """Lists all phone numbers"""
    table = Table(title= "List of Phone Numbers")
    fields = ['id', 'cc', 'ac', 'number']
    for header in fields:
        table.add_column(header, style= 'magenta')

    with Session(engine) as session:
        numbers = session.query(PhoneNumber).all()
        for num in numbers:
            table.add_row(str(num.id), str(num.cc), str(num.ac), str(num.number))

    Console().print(table)




