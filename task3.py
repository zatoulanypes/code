import re
import string
from collections import defaultdict, Counter

def lat_sorted(s):

    d = defaultdict(int)
    alphabet = string.ascii_letters + string.digits
    for letter in alphabet:
        d[letter] = 0

    c = Counter(d)
    c.update(s)
    return re.sub(' ', '', ''.join(list(c.elements())))

print(lat_sorted('Was Oxford worth while?'))