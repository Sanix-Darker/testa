# ::import_start::
from hashlib import sha256
from math import sqrt as math_square

# ::import_end::

# ::testa_start::
# ::case_start::
# >> square(9)
# << 3.0
# ::case_end::
# ::code_start::
def square(a):
    return math_square(a)


# ::code_end::
# ::testa_end::


# ::testa_start::
# ::case_start::
# >> shasha256("test")
# << "12345"
# ::case_end::
# ::code_start::
def shasha256(a):
    return sha256(a.encode()).hexdigest()


# ::code_end::
# ::testa_end::
