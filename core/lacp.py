import typer


app = typer.Typer()


# TODO: check if both interfaces have same speed
@app.command()
def create(
    port: int, description: str,
    first_interface: str, second_interface: str
    ):
    '''Create LACP'''
    pass


@app.command()
def delete(lacp_name: str):
    '''Delete LACP'''
    pass


@app.command()
def remove(interface_name: str):
    '''Remove interface from LACP'''
    pass


if __name__ == "__main__":
    app()