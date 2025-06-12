import typing
import io
import operator
from pathlib import Path

def best_subsequence_length(data: typing.TextIO) -> list[int]:
    """Find the longest contiguous subsequence of maximum quality."""
    raw = data.read().splitlines()
    if len(raw) != 4:
        raise ValueError("Invalid FASTQ data")
    if len(raw[1]) != len(raw[3]):
        raise ValueError("Quality scores do not match")
    
    minimum = int.from_bytes(b'!')
    maximum = int.from_bytes(b'~')
    scores = []
    for score_character in raw[3]:
        score = int.from_bytes(score_character.encode())
        if score < minimum:
            raise ValueError("Quality score too low")
        if score > maximum:
            raise ValueError("Quality score too high")

        if len(scores) == 0:
            scores.append([score, 1])
        elif scores[-1][0] == score:
            scores[-1][1] += 1
        else:
            scores.append([score, 1])

    return sorted(scores, key=operator.itemgetter(1), reverse=True)[0]


def test_best_subsequence_length():
    """Test best_subsequence_length function."""
    resource = io.StringIO("@SEQ\nATGCC\n+\n*///%")
    assert [47, 3] == best_subsequence_length(resource)
    resource = io.StringIO("@SEQ\nATAATGATTC\n+\n*///%%////")
    assert [47, 4] == best_subsequence_length(resource)
    resource = io.StringIO("@SEQ\nATGC\n+\nA2YY")
    assert [89, 2] == best_subsequence_length(resource)

    path = Path("temporary.fastq")
    with path.open(mode="w") as setup:
        setup.write("@SEQ\nATGC\n+\nA2YY")

    with path.open() as resource:
        assert [89, 2] == best_subsequence_length(resource)
    return "Success"

if __name__ == "__main__":
    test_best_subsequence_length()
