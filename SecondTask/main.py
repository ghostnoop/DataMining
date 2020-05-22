from operator import attrgetter
import matplotlib.pyplot as plt
import numpy as np

from SecondTask.graph3 import graph4_0
from SecondTask.ProductClass import Product

mapa = {}


def check(l):
    if mapa.get(l[0]) is None:
        mapa[l[0]] = 1
    else:
        mapa[l[0]] = mapa.get(l[0]) + 1


f = open('transactions.csv')
f.readline()
for line in f:
    check(line.split(";"))

products = []
sum_count = 0

for i in mapa:
    sum_count += mapa[i]
    products.append(Product(str(i), mapa[i]))
sum_count = sum_count / len(mapa)

products.sort()

the_best = []

index = len(products) - 50

f = open('res.csv', 'w')
i = 0
for j in products:

    if index <= i and j.count >= sum_count:
        the_best.append(j)
        f.write(j.name + ";" + str(j.count) + "\n")
    i = i + 1

graph4_0(the_best)
print("best done")
