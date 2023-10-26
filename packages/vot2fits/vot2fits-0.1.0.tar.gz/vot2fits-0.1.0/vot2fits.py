#!/usr/bin/env python3
"""Convert VOTable to FITS"""
from dask import delayed, compute
from dask.delayed import Delayed
from pathlib import Path
from typing import List

import click
from astropy.table import Table

VOT_EXTENSIONS = (
    ".vot",
    ".xml",
    ".votable",
)

@delayed
def convert_table(
        file_path: Path,
        overwrite: bool = False,
) -> None:
    if file_path.suffix not in VOT_EXTENSIONS:
        print(f"Skipping {file_path} as it is not a VOTable")
        return
    print(f"Reading {file_path}")
    table = Table.read(file_path)
    fits_name = file_path.with_suffix(".fits")
    print(f"Writing {fits_name}")
    table.write(fits_name, overwrite=overwrite)
    print(f"Wrote {fits_name}")

@click.command()
@click.argument("file_names", nargs=-1)
@click.option(
    "--overwrite",
    "-o",
    is_flag=True,
    help="Overwrite existing files",
)
def main(
    file_names: List[str],
    overwrite: bool = False,
):
    tasks: List[Delayed] = []
    for file_name in file_names:
            file_path = Path(file_name)
            task = convert_table(file_path, overwrite=overwrite)
            tasks.append(task)
    
    compute(*tasks)
    print("Done!")


if __name__ == "__main__":
    main()
