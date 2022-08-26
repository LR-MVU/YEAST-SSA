# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:12:43 2022

@author: Lokha
"""


def litering_by_three(a):
    return ' '.join([a[i:i + 3] for i in range(0, len(a), 3)])

print ("Enter the sequence")

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
sequence = ''.join(lines)

print("You entered...")
print()
print(sequence)

print()
sequence = litering_by_three(sequence)
print (sequence)

print (sequence.count("GCT", 0, len(sequence)))
print (sequence.count("TCT", 0, len(sequence)))
print (sequence.count("ACT", 0, len(sequence)))
print (sequence.count("GTT", 0, len(sequence)))
print (sequence.count("ATT", 0, len(sequence)))

print (sequence.count("GAC", 0, len(sequence)))
print (sequence.count("TTC", 0, len(sequence)))
print (sequence.count("TAC", 0, len(sequence)))
print (sequence.count("TGT", 0, len(sequence)))
print (sequence.count("AAC", 0, len(sequence)))
print (sequence.count("CAC", 0, len(sequence)))

print (sequence.count("AGA", 0, len(sequence)))
print (sequence.count("GAA", 0, len(sequence)))
print (sequence.count("TTG", 0, len(sequence)))
print (sequence.count("AAG", 0, len(sequence)))
print (sequence.count("GGT", 0, len(sequence)))
print (sequence.count("CAA", 0, len(sequence)))
print (sequence.count("CCA", 0, len(sequence)))

print (sequence.count("ATG", 0, len(sequence)))
print (sequence.count("UGG", 0, len(sequence)))
