from duration import parse, format


def test_roundtrip():
    assert parse("1h30m") == 5400
    assert format(5400) == "1h30m"
    assert format(0) == "0s"
