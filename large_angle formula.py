"""
    Physics Homework:

    The period of a simple pendulum. Program takes in parameters to give you an
    approximate period of a pendulum
"""
import math as m


def angle_formula(L, theta):
    """
    :param L: int. length of string
    :param theta: int. angle at which pendulum started at. (degrees)
    :return: int. period of simple pendulum.
    """
    return 2 * m.pi * m.sqrt(L / 9.8) * (
            1 + (1 / 4) * pow(m.sin(m.radians(theta / 2)), 2) + (9 / (4 * 16)) * pow(m.sin(m.sin(m.radians(theta / 2))),
                                                                                     4))


def percent_error(exp, theo):
    return f"exp and theo: {round(abs((exp - theo)/theo) * 100, 3)}, t0 and theo: {round(abs((1.664-theo)/theo) * 100, 2)}"


if __name__ == '__main__':
    # angle
    l = -1
    while l != 0:
        if l == 0:
            break
        l, angle = float(input("Enter length: ")), float(input("Enter angle: "))
        print(f"T theoretical: {angle_formula(l, angle)}\n")

    while True:
        tested, actual = float(input("Enter exp: ")), float(input("Enter actual: "))
        print(percent_error(tested, actual))
