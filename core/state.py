import typer


app = typer.Typer()


@app.command("on")
def turn_on(interface_name: str):
    '''Changes state of interface to ON'''
    pass


@app.command("off")
def turn_off(interface_item: str):
    '''Changes state of interface to OFF'''
    pass


if __name__ == "__main__":
    app()