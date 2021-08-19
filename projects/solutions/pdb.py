"Support function for the 3D protein plotting project"

from typing import List, Tuple
from urllib import request


def compare_floats(_a: float, _b: float) -> bool:
    "Compare coordinates to PDB format precision"
    return abs(_a - _b) < 0.001


def compare_coordinate_lists(
    _xs: List[Tuple[float, float, float]], _ys: List[Tuple[float, float, float]]
) -> List[bool]:
    "Compare coordinate lists to PDB format precision"
    return [
        compare_floats(*val)
        for crd_pairs in [list(zip(*l)) for l in zip(_xs, _ys)]
        for val in crd_pairs
    ]


def get_pdb_online(entry):
    "Download PDB data from the internet"
    with request.urlopen(
        f"https://www.ebi.ac.uk/pdbe/entry-files/download/pdb{entry.lower()}.ent"
    ) as pdbfile:
        data = pdbfile.read().decode()

    return data


def get_pdb_offline(path):
    "Load PDB data from a local file"
    with open(path, mode="r") as pdbfile:
        data = pdbfile.read()

    return data


def parse_pdb(entry, chain):
    "Extract choordinates for a single chain"
    return [
        (float(line[30:38]), float(line[38:46]), float(line[46:54]))
        for line in entry.split("\n")
        if line[:6] == "ATOM  " and line[12:16] == " CA " and line[21] == chain
    ]
