import typer

import core.status as status
import core.speed as speed
import core.lacp as lacp
import core.state as state
import core.acl as acl

app = typer.Typer()
app.add_typer(status.app, name="status")
app.add_typer(speed.app, name="speed")
app.add_typer(lacp.app, name="lacp")
app.add_typer(state.app, name="state")
app.add_typer(acl.app, name="acl")

# TODO: add separate command for committing changes
# TODO: add seprate command to check pending changes


if __name__ == "__main__":
    app()