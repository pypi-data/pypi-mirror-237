"""A cli interface for the linker."""
import mmap
from typing import IO

import click
from monistode_binutils_shared import ExecutableFile, ObjectManager

from .linker import Linker


@click.group()
def cli():
    """The main cli group."""
    pass


@cli.command()
@click.option(
    "--input", "-i", help="The input file.", multiple=True, type=click.Path(exists=True)
)
@click.option(
    "--output", "-o", help="The output file.", required=True, type=click.File("rb+")
)
@click.option(
    "--harvard/--no-harvard",
    "-h",
    help="Whether to use harvard architecture.",
    default=False,
)
@click.option(
    "--max-merge-distance",
    "-m",
    help="The maximum distance between two mergeable sections.",
    default=0x100,
)
def link(
    input: tuple[str, ...], output: IO[bytes], harvard: bool, max_merge_distance: int
) -> None:
    """Link the input files into the output file."""
    linker = Linker()
    output.write(bytes(ExecutableFile.empty()))
    output.flush()

    for file in input:
        with open(file, "rb") as f:
            linker.add_object(ObjectManager.from_bytes(f.read()))

    linker.link(
        ExecutableFile(mmap.mmap(output.fileno(), 0)),
        harvard=harvard,
        max_merge_distance=max_merge_distance,
    )


if __name__ == "__main__":
    cli()
