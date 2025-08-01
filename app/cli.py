import typer
import uvicorn 

cli = typer.Typer()

@cli.command()
def api():
    """Run the api"""
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload= True)
