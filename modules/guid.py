import string
import random


def guid(key_size=6, chars=string.ascii_lowercase + string.digits):
    try:
        return ''.join(random.SystemRandom().choice(chars) for _ in range(key_size))
    except(NotImplementedError):
        return ''.join(random.choice(chars) for _ in range(key_size))
