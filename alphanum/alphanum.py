import random
import secrets
import string

POP = string.ascii_letters + string.digits


def generate(length: int = 1) -> str:
    """Generates a pseudo-random string of alphanumeric characters of the given
    length. If no length is specified, a single character is returned.

    Args:
        length (:obj:`int`, optional): Desired string length. Defaults to 1.

    Returns:
        str: A pseudo-random alphanumeric string.

    Examples:
        >>> print(generate())
        'G'
        >>> print(generate(10))
        'a93jfDjdA0'

    """
    return ''.join(random.SystemRandom().choices(POP, k=length))


def generate_s(length: int = 1) -> str:
    """Generates a cryptographically strong random string of alphanumeric
    characters of the given length. If no length is specified, a single
    character is returned.

    Args:
        length (:obj:`int`, optional): Desired string length. Defaults to 1.

    Returns:
        str: A random alphanumeric string.

    Examples:
        >>> print(generate_s())
        '5'
        >>> print(generate_s(10))
        't3g0Gh9Naj'

    """
    return ''.join(secrets.SystemRandom().choice(POP) for i in range(length))
