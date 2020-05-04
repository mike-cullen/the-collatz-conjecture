#!/usr/bin/env python3.8

# The Collatz conjecture is a conjecture in mathematics
# named after Lothar Collatz, who first proposed it in 1937.
# The conjecture is also known as the 3n + 1 conjecture,
# the Ulam conjecture (after Stanisław Ulam), Kakutani's problem
# (after Shizuo Kakutani), the Thwaites conjecture (after Sir Bryan Thwaites),
# Hasse's algorithm (after Helmut Hasse), or the Syracuse problem;
# the sequence of numbers involved is referred to as the hailstone
# sequence or hailstone numbers (because the values are usually subject
# to multiple descents and ascents like hailstones in a cloud),
# or as wondrous numbers.
#
# Take any natural number n. If n is even, divide it by 2 to get n / 2.
# If n is odd, multiply it by 3 and add 1 to obtain 3n + 1.
# Repeat the process (which has been called "Half Or Triple Plus One",
# or HOTPO) indefinitely. The conjecture is that no matter what number
# you start with, you will always eventually reach 1. The property
# has also been called oneness.
#
# Paul Erdős said about the Collatz conjecture:
# "Mathematics may not be ready for such problems."
# He also offered $500 for its solution.
#
# In 1972, J. H. Conway proved that a natural generalization
# of the Collatz problem is algorithmically undecidable.

n = 5765675757657657657575765467686868768768587 * 999999993433434399999999999
while n != 1:
    if n % 2 == 0: #if n is an even number
        n = n/2
        print(n)
    else:
        n = 3 * n + 1
        print(n)
