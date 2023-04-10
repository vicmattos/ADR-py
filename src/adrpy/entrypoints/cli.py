from pathlib import Path
from typing import Optional

import typer
from adrpy.injection import injector
from adrpy.shared_kernel.dtos import CreateADRDTO, InitializeADRDTO
from adrpy.use_cases.creating import CreatingADR
from adrpy.use_cases.initializing import InitializingADR

app = typer.Typer()


@app.command()
def init(path: Optional[Path] = typer.Argument(None)) -> None:
    use_case = injector.get(InitializingADR)
    dto = InitializeADRDTO(path=path)
    use_case.execute(dto=dto)


@app.command()
def new(name: str) -> None:
    use_case = injector.get(CreatingADR)
    dto = CreateADRDTO(name=name)
    use_case.execute(dto=dto)


def cli_entrypoint() -> None:
    app()
