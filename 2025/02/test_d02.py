"""
Since the young Elf was just doing silly patterns, you can find the invalid IDs
by looking for any ID which is made only of some sequence of digits repeated
twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be
invalid IDs.
"""

from d02 import repeats


def test_repeats():
    assert not repeats(1, "123")
    assert not repeats(1, "110")
    assert not repeats(1, "999")

    assert repeats(1, "55")
    assert repeats(1, "6464")
    assert repeats(1, "123123")
    assert repeats(1, "38593859")

    assert not repeats(2, "123")
    assert not repeats(2, "110")

    assert repeats(2, "999")
    assert repeats(2, "123123")
    assert repeats(2, "2121212121")
