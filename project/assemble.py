"""
Functions to assemble sequences.

The most important of these functions is:
   - assemble(fragments)
"""

from typing import Callable, Tuple
from collections.abc import Sequence
from functools import lru_cache
import math
import unittest

from project.distance import align, coverage, Matrix

GAP_CHARACTER = "-"


def merge(reference: str, target: str) -> str:
    """
    Merge an alignment into a single sequence.
    For example:
    >>> merge("ATTGC---", "--TGCTTG")
    'ATTGCTTG'
    """
    return "".join([tgt if ref == "-" else ref for ref, tgt in zip(reference, target)])


def stripgaps(reference: str, target: str) -> Tuple[str, str]:
    """
    Remove prefix and suffix inserts and delets.

    For example:
    >>> stripgaps("ATTGC---", "--TGCTTG")
    ('TGC', 'TGC')

    >>> stripgaps("GTCC", "GTGG")
    ('GTCC', 'GTGG')
    """
    index = [
        i
        for i, (ref, tgt) in enumerate(zip(reference, target))
        if all([ref != GAP_CHARACTER, tgt != GAP_CHARACTER])
    ]

    if index:
        return reference[index[0] : index[-1] + 1], target[index[0] : index[-1] + 1]

    return "", ""


@lru_cache(maxsize=None)
def score(alignment: Tuple[str, str]) -> float:
    """
    Compote a 'score' to be maximised for an alignment.

    In this case, I only want alignments that will _extend_ a contig.
    So alignments that contain gaps between substitutions are given
    the worst possible score. Otherwise the score is just the sequence
    identity.
    """
    reference, target = stripgaps(alignment[0], alignment[1])
    if "-" in reference or "-" in target:
        return -math.inf

    return sum((ref == tgt for ref, tgt in zip(reference, target)))


def assemble_helper(
    fragments: Sequence[str], scoringfn: Callable[[str, str], Matrix]
) -> Sequence[str]:
    """
    This is where the _real_ work is done.

    1. Generate and score all possible alignments between fragments.
    2. Pick the highest scoring alignment and merge the fragments
    3. Return the original fragments without the merged fragments +
       the config we created in step 2.
    """
    if len(fragments) < 2:
        return fragments
    print(f"{len(fragments)=}")

    alignments = []
    for i, reference in enumerate(fragments):
        for j in range(i + 1, len(fragments)):
            alignments.append((i, j, align(reference, fragments[j], scoringfn)))

    tomerge = max(alignments, key=lambda a: score(a[2]))
    thescore = score(*tomerge[2])
    print(tomerge[2][0])
    print(tomerge[2][1])
    print(thescore)
    print("=======================================")

    if coverage(*tomerge[2]) > 0 and thescore > 0:
        return [
            fragments[i]
            for i in range(len(fragments))
            if i not in (tomerge[0], tomerge[1])
        ] + [merge(*tomerge[2])]

    return fragments


def assemble(
    fragments: Sequence[str], scoringfn: Callable[[str, str], Matrix]
) -> Sequence[str]:
    """
    Assemble fragments using an alignment `scoringfn`.

    Two scoring functions are defined:
        - edit_distance(), and
        - needleman_wunsch()

    This function can be called like e.g.
    assemble(fragments, needleman_wunsch)
    """
    assembly = assemble_helper(fragments, scoringfn)

    # If the number of fragments has not changed, we're done
    if len(assembly) == len(fragments):
        return assembly

    return assemble(assembly, scoringfn)


####### TESTING ########


class TestAssembly(unittest.TestCase):
    " Unit tests functions in this file. "

    def test_merge(self):
        " Unit tests for the merge() function. "
        self.assertEqual(merge("", ""), "")
        self.assertEqual(merge("A", "A"), "A")
        self.assertEqual(merge("A", "G"), "A")
        self.assertEqual(merge("-A", "AA"), "AA")
        self.assertEqual(merge("A-", "AA"), "AA")
        self.assertEqual(merge("AA", "-A"), "AA")
        self.assertEqual(merge("AA", "A-"), "AA")

    def test_stripgaps(self):
        " UNit tests for the stripgaps() function. "
        self.assertEqual(stripgaps("", ""), ("", ""))
        self.assertEqual(stripgaps("A", "A"), ("A", "A"))
        self.assertEqual(stripgaps("-", "A"), ("", ""))
        self.assertEqual(stripgaps("-A", "AA"), ("A", "A"))
        self.assertEqual(stripgaps("AA", "-A"), ("A", "A"))
        self.assertEqual(stripgaps("A-", "AA"), ("A", "A"))
        self.assertEqual(stripgaps("AA", "A-"), ("A", "A"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    unittest.main()
