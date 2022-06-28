import random
import string

from heyurl.models import (
    Url
)


def short_url_generator(size=5, chars=string.ascii_letters + string.digits):
    short_url = ''.join(random.choice(chars) for _ in range(size))
    
    while(Url.objects.filter(short_url=short_url).exists()):
        short_url = ''.join(random.choice(chars) for _ in range(size))

    return short_url
