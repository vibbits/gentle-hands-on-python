"""
A module for calculating the relationship (or distance) between 2 strings.

Namely:
    - edit_distance()
    - needleman_wunsch()
    - align()
    - coverage()
"""
from typing import Callable, Tuple, List
from enum import IntEnum
from operator import itemgetter
from functools import cache
import unittest


class BackTrack(IntEnum):
    " Used by align() for backtracking. "
    DELETE = 1
    INSERT = 2
    SUBSTITUTE = 3
    UNASSIGNED = 4


# (Score, backtrack direction)
MatrixElement = Tuple[float, BackTrack]
Matrix = List[List[MatrixElement]]


def print_matrix(mat: Matrix) -> None:
    " Pretty print an alignment matrix. "

    def show_backtrack(val: BackTrack) -> str:
        if val == BackTrack.DELETE:
            return "d"

        if val == BackTrack.INSERT:
            return "i"

        if val == BackTrack.SUBSTITUTE:
            return "m"

        return "?"

    rowstr: List[List[str]] = [[] for _ in mat[0]]
    for col in mat:
        for irow, elem in enumerate(col):
            rowstr[irow].append(
                "(" + str(elem[0]) + ", " + show_backtrack(elem[1]) + ")"
            )

    print("\n".join([" ".join(r) for r in rowstr]) + "\n")


@cache
def edit_distance(reference: str, target: str) -> Matrix:
    """ Computes the edit distance matrix between a and b. """
    rows = len(reference) + 1
    cols = len(target) + 1
    dist = [[(0.0, BackTrack.UNASSIGNED) for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        dist[i][0] = (i, BackTrack.DELETE)

    for j in range(1, cols):
        dist[0][j] = (j, BackTrack.INSERT)

    for col in range(1, cols):
        for row in range(1, rows):
            if reference[row - 1] == target[col - 1]:
                cost = 0
            else:
                cost = 1

            options = [
                (dist[row - 1][col - 1][0] + cost, BackTrack.SUBSTITUTE),
                (dist[row][col - 1][0] + 1, BackTrack.INSERT),
                (dist[row - 1][col][0] + 1, BackTrack.DELETE),
            ]

            dist[row][col] = min(options, key=itemgetter(0))

    return dist


@cache
def needleman_wunsch(reference: str, target: str) -> Matrix:
    """ Computes the Needleman-Wunsch matrix between a and b. """
    gap_open = 2
    gap_extend = 0.1  # Expected length is 10

    def gap_penalty(gaps: List[MatrixElement], direction: BackTrack) -> float:
        penalty = float(gap_open)
        for gap in gaps[::-1]:
            if gap[1] == direction:
                penalty += gap_extend
            else:
                penalty += gap[0]
                break

        return penalty

    rows = len(reference) + 1
    cols = len(target) + 1
    dist = [[(0.0, BackTrack.UNASSIGNED) for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        boundaryrow = [dist[r][0] for r in range(0, i)]
        dist[i][0] = (
            gap_penalty(boundaryrow, BackTrack.DELETE) - gap_open,
            BackTrack.DELETE,
        )

    for j in range(1, cols):
        dist[0][j] = (
            gap_penalty(dist[0][:j], BackTrack.INSERT) - gap_open,
            BackTrack.INSERT,
        )

    for col in range(1, cols):
        for row in range(1, rows):
            insert_penalty = gap_penalty(
                [dist[row][c] for c in range(col)], BackTrack.INSERT
            )
            delete_penalty = gap_penalty(
                [dist[r][col] for r in range(row)], BackTrack.DELETE
            )

            dist[row][col] = min(
                [
                    (insert_penalty, BackTrack.INSERT),
                    (delete_penalty, BackTrack.DELETE),
                    (
                        dist[row - 1][col - 1][0]
                        + (0 if reference[row - 1] == target[col - 1] else 1),
                        BackTrack.SUBSTITUTE,
                    ),
                ],
                key=itemgetter(0),
            )

    return dist


def align(
    reference: str, target: str, scoringfn: Callable[[str, str], Matrix]
) -> Tuple[str, str]:
    """ Compute the alignment between a and b using a provided scoring function. """
    i = len(reference)
    j = len(target)
    matrix = scoringfn(reference, target)
    _reference = ""
    _target = ""
    while (i, j) != (0, 0):
        backtrack = matrix[i][j][1]

        if backtrack == BackTrack.SUBSTITUTE:
            i -= 1
            j -= 1
            _reference += reference[i]
            _target += target[j]
        elif backtrack == BackTrack.INSERT:
            j -= 1
            _reference += "-"
            _target += target[j]
        elif backtrack == BackTrack.DELETE:
            i -= 1
            _reference += reference[i]
            _target += "-"

    return (_reference[::-1], _target[::-1])


@cache
def coverage(reference: str, target: str) -> int:
    """
    The number of substitutions in an alignment.

    >>> coverage("---ATGGC", "GTTA-GGG")
    4
    """
    return sum([ref != "-" and tgt != "-" for ref, tgt in zip(reference, target)])


####### TESTING ########


class TestDistance(unittest.TestCase):
    " Unit tests functions in this file. "

    def test_coverage(self):
        " Unit tests for the merge() function. "
        self.assertEqual(coverage("", ""), 0)
        self.assertEqual(coverage("A", "A"), 1)
        self.assertEqual(coverage("A", "G"), 1)
        self.assertEqual(coverage("-A", "AA"), 1)
        self.assertEqual(coverage("A-", "AA"), 1)
        self.assertEqual(coverage("AA", "-A"), 1)
        self.assertEqual(coverage("AA", "A-"), 1)
        self.assertEqual(coverage("A-A", "AAA"), 2)
        self.assertEqual(coverage("AAA", "A-A"), 2)

    def test_align_edit_distance(self):
        " Unit tests for align() using edit_distance(). "
        self.assertEqual(align("", "", edit_distance), ("", ""))
        self.assertEqual(align("A", "A", edit_distance), ("A", "A"))
        self.assertEqual(align("AB", "A", edit_distance), ("AB", "A-"))
        self.assertEqual(align("AB", "B", edit_distance), ("AB", "-B"))
        self.assertEqual(align("A", "AB", edit_distance), ("A-", "AB"))
        self.assertEqual(align("B", "AB", edit_distance), ("-B", "AB"))
        self.assertEqual(align("AB", "CD", edit_distance), ("AB", "CD"))

    def test_align_needleman_wunsch(self):
        " Unit tests for align() using needleman_wunsch(). "
        self.assertEqual(align("", "", needleman_wunsch), ("", ""))
        self.assertEqual(align("A", "A", needleman_wunsch), ("A", "A"))
        self.assertEqual(align("AB", "A", needleman_wunsch), ("AB", "-A"))
        self.assertEqual(align("AB", "B", needleman_wunsch), ("AB", "-B"))
        self.assertEqual(align("A", "AB", needleman_wunsch), ("-A", "AB"))
        self.assertEqual(align("B", "AB", needleman_wunsch), ("-B", "AB"))
        self.assertEqual(align("AB", "CD", needleman_wunsch), ("AB", "CD"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    unittest.main()
