import numpy as np
import pandas as pd
import math
from scipy.stats import bernoulli
from math import pi
from matplotlib import pyplot as plt

def minusList(l1, l2):
    return [x - y for x, y in zip(l1, l2)]


trivial_cost = [810.32, 458.27, 291.92, 201.215, 148.17, 113.47, 88.905, 72.61, 59.8, 50.09, 42.825, 36.785]
ours_cost = [809.37, 456.675, 359.865, 337.66, 314.73, 292.97, 271.765, 249.77, 226.905, 205.59, 183.52, 162.08]
nips_cost = [809.055, 457.225, 360.365, 338.575, 315.585, 292.82, 271.08, 249.23, 226.625, 204.505, 184.4, 161.305]
oracle_cost = [804.235, 454.605, 293.45, 201.735, 148.34, 113.365, 89.22, 72.42, 59.405, 50.15, 42.685, 36.765]

trivial_times_target = [9046.51, 9461.36, 9656.155, 9762.985, 9826.42, 9866.77, 9894.89, 9914.735, 9929.86, 9941.075, 9949.665, 9956.7]
ours_times_target = [9048.89, 9462.895, 9561.06, 9561.895, 9563.495, 9564.62, 9563.99, 9564.005, 9565.655, 9565.365, 9566.585, 9565.865]
nips_times_target = [9046.685, 9462.36, 9560.545, 9561.855, 9563.28, 9563.82, 9564.57, 9564.715, 9564.985, 9565.815, 9565.99, 9567.36]
oracle_times_target = [9053.125, 9464.635, 9655.84, 9762.995, 9825.87, 9867.055, 9894.915, 9914.715, 9929.895, 9941.05, 9949.78, 9956.625]


oursTrivialCost = minusList(trivial_cost, ours_cost)
nipsTrivialCost = minusList(trivial_cost, nips_cost)
oracleTrivialCost = minusList(trivial_cost, oracle_cost)
print(oursTrivialCost)
print(nipsTrivialCost)
print(oracleTrivialCost)


plt.figure()
plt.grid(True)
plt.title("Improvement from Trivial algorithm\nand Comparison with Oracle Attack")
plt.text(0.4, -25, "mu1 = 0.85\nT = 10000, repeat 200 times")
plt.axhline(0, color='green', lw=2)
x = np.linspace(0.1, 0.65, 12)
# plt.ylim(-2, 6)
plt.plot(x, oursTrivialCost, label="ours")
plt.plot(x, nipsTrivialCost, label="nips", ls=":")
plt.plot(x, oracleTrivialCost, label="oracle", color='black', lw=1.5, ls="--")
plt.xlabel("mu2")
plt.ylabel("Cost")
plt.legend()
plt.show()
# plt.savefig(fname="CostCompare.png")

oursTrivialTimes = minusList(ours_times_target, trivial_times_target)
nipsTrivialTimes = minusList(nips_times_target, trivial_times_target)
oracleTrivialTimes = minusList(oracle_times_target, trivial_times_target)
print(oursTrivialTimes)
print(nipsTrivialTimes)
print(oracleTrivialTimes)

plt.figure()
plt.grid(True)
plt.title("Improvement from trivial algorithm\nand Comparison with Oracle Attack")
plt.text(0.4, -50, "mu1 = 0.85\nT = 10000, repeat 200 times")
plt.axhline(0, color='green', lw=2)
x = np.linspace(0.1, 0.65, 12)
# plt.ylim(-3, 5)
plt.plot(x, oursTrivialTimes, label="ours")
plt.plot(x, nipsTrivialTimes, label="nips", ls=":")
plt.plot(x, oracleTrivialTimes, label="oracle", color='black', lw=1.5, ls="--")
plt.xlabel("mu2")
plt.ylabel("times of target arm")
plt.legend()
plt.show()
# plt.savefig(fname="TargetTimesCompare.png")
















