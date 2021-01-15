""" Generate some fragments. """

from typing import TextIO, List
from pathlib import Path
import random


def read_sequence(input: TextIO) -> str:
    """ Read sequence data. """
    return "".join([s.strip() for s in input.readlines()])

def genfrags(sequence: str, number: int, size: int) -> List[str]:
    """
    Generate `number` fragments all of equal length: `size`, from `sequence`.

    Ensure that there is a fragment covering the very beginning
    and end of `sequence`.
    """
    random.seed()

    starts = (random.randint(0, len(sequence) - size) for _ in range(number))

    return [sequence[start : start + size] for start in starts] + [
        sequence[:size],
        sequence[len(sequence) - size :],
    ]


def generate(filename: Path, number: int, size: int) -> List[str]:
    """ Given an input file containing a sequence, generate random fragments. """
    with open(filename) as seq_file:
        return genfrags(read_sequence(seq_file), number, size)


def write_fragments(output: TextIO, fragments: List[str]) -> None:
    " Write fragments to a file. "
    output.write("\n".join(fragments))
