import alphanum


def test_no_string_length():
    foo = alphanum.generate()
    assert len(foo) == 1


def test_with_string_length():
    foo = alphanum.generate(10)
    assert len(foo) == 10


def test_subsequent_strings_differ():
    foo = alphanum.generate(10)
    bar = alphanum.generate(10)
    assert foo != bar


def test_secure_no_string_length():
    foo = alphanum.generate_s()
    assert len(foo) == 1


def test_secure_with_string_length():
    foo = alphanum.generate_s(10)
    assert len(foo) == 10


def test_secure_subsequent_strings_differ():
    foo = alphanum.generate_s(10)
    bar = alphanum.generate_s(10)
    assert foo != bar
