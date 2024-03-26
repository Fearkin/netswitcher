import typer


app = typer.Typer()


@app.command("show")
def show_config(interface_name: str):
    '''Shows current configuration of interface'''
    pass

#TODO: consider adding this as an option to "show"
@app.command("mac")
def find_by_mac(mac: str):
    '''Find interface by MAC'''
    pass


@app.command("lacp")
def show_all_lacp(lacp_name: str):
    '''Shows active LACP with given name and all created LACP'''
    pass


@app.command("int")
def show_status(interface_name: str):
    '''Shows current state of interface'''
    pass


if __name__ == "__main__":
    app()