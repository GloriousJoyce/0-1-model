import numpy as np
import pandas as pd
import math
from scipy.stats import bernoulli
from math import pi
from matplotlib import pyplot as plt


K, T = 2, 10000
mean1, mean2 = 0.85, 0.65
delta0, delta =0.1, 0.1

t, n1, n2 = 0, 0, 0
I_t_, N1_, N2_, Attack_, U1_, U2_, U1_0_ = 0, 0, 0, 0, 0, 0, 0

# def UCB(rounds, mu, N):
#     return mu + math.sqrt(3 * math.log(rounds) / (2 * N))
def UCB(rounds, mu, N):
    return mu + 3 * math.sqrt(math.log(rounds) / N) / 2


def add_list(l1, l2):
    return [x + y for x, y in zip(l1, l2)]


def alpha0():
    cumuatt = sum(Attack)
    tem = u2 - delta0 - 2 * math.sqrt(math.log(pi * pi * K * n2 * n2 / (3 * delta)) / (2 * n2))
    tem = max(tem, 0)
    ret = (n1 + 1) * u1_0 - cumuatt - tem * (n1 + 1)
    return [ret, tem]



for count in range(200):

    t, n1, n2 = 0, 0, 0
    I_t, N1, N2, Alpha0, Attack, U1, U2, U1_0 = [], [], [], [], [], [], [], []

    """
    first K rounds
    """

    r1 = bernoulli.rvs(mean1)
    t += 1
    n1 += 1
    I_t.append(1)
    Alpha0.append(r1)
    N1.append(1)
    N2.append(0)
    u1, u2, u1_0 = 0, 0, r1
    if r1 == 1:
        Attack.append(1)
    else:
        Attack.append(0)
    U1.append(u1)
    U2.append(u2)
    U1_0.append(u1_0)
    star = 0

    r2 = bernoulli.rvs(mean2)
    t += 1
    n2 += 1
    I_t.append(2)
    Alpha0.append(0)
    Attack.append(0)
    N1.append(1)
    N2.append(1)
    u2 = r2
    U1.append(u1)
    U2.append(u2)
    U1_0.append(u1_0)


    """
    next T-K rounds
    """

    for index in range(K, T):
        t += 1
        if UCB(t, u1, n1) >= UCB(t, u2, n2):
            I_t.append(1)
            r = bernoulli.rvs(mean1)
            if r == 1:
                u1_0 = (u1_0 * n1 + 1) / (n1 + 1)
                U1_0.append(u1_0)
                newalpha, temp = alpha0()
                if newalpha <= 1:
                    star = temp
                    alpha = newalpha
                    # print(index)
                else:
                    alpha = newalpha + (temp - star) * (n1 + 1)
                Alpha0.append(alpha)
                if alpha <= 0:
                    u1 = (u1 * n1 + 1) / (n1 + 1)
                    U1.append(u1)
                    Attack.append(0)
                else:
                    u1 = u1 * n1 / (n1 + 1)
                    U1.append(u1)
                    Attack.append(1)
            else:
                u1_0 = u1_0 * n1 / (n1 + 1)
                u1 = u1 * n1 / (n1 + 1)
                U1_0.append(u1_0)
                Alpha0.append(0)
                Attack.append(0)
                U1.append(u1)
            n1 += 1
            U2.append(u2)
            N1.append(n1)
            N2.append(n2)
        else:
            I_t.append(2)
            Alpha0.append(0)
            Attack.append(0)
            U1.append(u1)
            U1_0.append(u1_0)
            N1.append(n1)

            r = bernoulli.rvs(mean2)
            # if index < 1000:
            #     r = 1
            # else:
            #     r = 0

            u2 = (u2 * n2 + r) / (n2 + 1)
            U2.append(u2)
            n2 += 1
            N2.append(n2)

    N1_ += n1
    N2_ += n2
    Attack_ += sum(Attack)
    U1_ += u1
    U2_ += u2
    U1_0_ += u1_0

    print(count)


N1_ /= 200
N2_ /= 200
Attack_ /= 200
U1_ /= 200
U2_ /= 200
U1_0_ /= 200


"""
visualize
"""


print()
print("u1_0:", end=" ")
print(U1_0_)
print("u1:", end=" ")
print(U1_)
print("u2:", end=" ")
print(U2_)
print("Attack:", end=" ")
print(Attack_)
print("N1:", end=" ")
print(N1_)
print("N2:", end=" ")
print(N2_)
print()


print("Cost: ", end="")
print(Attack_)
print("Times: ", end="")
print(N2_)