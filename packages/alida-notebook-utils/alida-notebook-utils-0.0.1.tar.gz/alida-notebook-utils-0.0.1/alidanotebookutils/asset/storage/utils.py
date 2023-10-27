import random
import string

def path_generator(size=12, chars=string.ascii_lowercase + string.digits):
    return "d" + ''.join(random.choice(chars) for _ in range(size))

