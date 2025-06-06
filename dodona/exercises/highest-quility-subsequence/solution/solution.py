import typing
import io
from pathlib import Path

def best_subsequence_length(data: typing.TextIO) -> list[int]:
    """Find the longest contiguous subsequence of maximum quality."""
    raw = data.read().splitlines()
    if len(raw) != 4:
        raise ValueError("Invalid FASTQ data")
    if len(raw[1]) != len(raw[3]):
        raise ValueError("Quality scores do not match")
    
    highest = 0
    length = 0
    minimum = int.from_bytes(b'!')
    maximum = int.from_bytes(b'~')
    for score_character in raw[3]:
        score = int.from_bytes(score_character.encode())
        if score < minimum:
            raise ValueError("Quality score too low")
        if score > maximum:
            raise ValueError("Quality score too high")
        if score == highest:
            length += 1
        elif score > highest:
            length = 1
            highest = score

    return [highest, length]



def test_best_subsequence_length():
    """Test best_subsequence_length function."""
    resource = io.StringIO("@SEQ\nATGCC\n+\n*///%")
    assert [47, 3] == best_subsequence_length(resource)
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
