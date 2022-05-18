from src.identity import IdentitySequence


def test_identity_sequence():
    expected = [0, 1, 2]

    incrementor = IdentitySequence()
    actual = [incrementor.count, incrementor.next(), incrementor.next()]

    assert actual == expected
