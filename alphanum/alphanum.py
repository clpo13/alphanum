import random

POP = 'abcdefghijklmnopqrstuvwxyz0123456789'


def generate(length=1) -> str:
    return ''.join(random.SystemRandom().choices(POP, k=length))
