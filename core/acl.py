import typer

app = typer.Typer()


@app.command()
def create(name: str, ip: str):
    '''Creates ACL rule with given name'''
    pass


@app.command()
def delete(name: str):
    '''Deletes ACL rule with given name'''
    pass


@app.command()
def find(name: str):
    '''Shows ACL with given name'''
    pass


@app.command()
def add(acl_name: str, interface_name: str):
    '''Adds ACL rule with given name to interface'''
    pass

@app.command()
def remove(acl_name: str, interface_name: str):
    '''Removes ACL rule with given name from interface'''
    pass



if __name__ == "__main__":
    app()