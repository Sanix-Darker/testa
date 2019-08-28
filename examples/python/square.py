# ::tesla_start::
# ::case_start::
# >> tesla.isEqual(2, 2)
# << true
# ::case_end::
# ::tesla_end::


# ::tesla_start::
# ::case_start::
# >> square(9)
# << 3.0
# ::case_end::
# ::code_start::
from math import sqrt as math_square

def square(a):
    return math_square(a)
# ::code_end::
# ::tesla_end::