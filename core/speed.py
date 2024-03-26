import typer


app = typer.Typer()


@app.command("set")
def set_speed(interface_name: str, speed: str):
    '''Set speed for interface'''
    pass


@app.command("desc")
def set_description(interface_name: str, description: str):
    '''Set description for interface'''
    pass

if __name__ == "__main__":
    app()