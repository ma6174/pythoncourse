#!/usr/bin/env python3
#coding=utf-8

num_str = input("Please give me a Richter scale measure: ",)
num_float = float(num_str)
print("Richter measure:",num_float)
energy = 10 ** (1.5 * num_float + 4.8)
print("Equivalence in joules:",energy)
tnt = energy/4.184E9
print("Equivalence in Tons of TNT:",tnt)
print()
richters = [1,5,9.1,9.2,9.5]
print("Richter\t\tJoules\t\t\t\tTNT")
for item in richters:
    energy = 10 ** (1.5 * item + 4.8)
    tnt = energy/4.184E9
    print(item,energy,tnt,sep="\t\t")

