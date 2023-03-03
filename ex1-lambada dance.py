from functools import reduce


"""
div_and_mod:
Receives two integers – a,b and returns the result of a//b and a%b.
"""
div_and_mod = lambda a, b: (a // b, a % b)

"""
non_negative:
Receives one integer – a. If a is negative, returns zero. Otherwise, returns a.
"""
non_negative = lambda a: 0 if a < 0 else a

"""
double_digits:
Receives one integer – a, and returns it with each digit doubled
"""
double_digits = lambda given_input: int(reduce(lambda element1, element2: element1+element2, map(lambda a: a*2, str(given_input))))


assert div_and_mod (5,2) == (2, 1)
assert non_negative(5) == 5
assert non_negative(-5) == 0
assert double_digits(542) == 554422
