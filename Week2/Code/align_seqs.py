#!/bin/env python3

# Author: ph-u
# Script: align_seqs.py
# Desc: python homework -- genetic alignment module program
# Input: python3 align_seqs.py <seq_1> <seq_2>
# Output: 1. python interpreter output -- all alignment possibilities, raw sequences and best alignment score; 2. output best alignment(s) and its/their score(s) to a txt file in `Data` subdirectory
# Arguments: 0 or 2
# Date: Oct 2019

"""python homework -- genetic alignment module program"""

__appname__="align_seqs.py"
__author__="ph-u"
__version__="0.0.1"
__license__="None"

## imports
import sys

## input
f=open('../Data/seq.csv',"r")
seq2=f.readline().strip()
seq1=f.readline().strip()
f.close()

# Two example sequences to match
# seq2 = "ATCGCCGGATTACGGG"
# seq1 = "CAATTCGGAT"

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# A function that computes a score by returning the number of matches starting from arbitrary startpoint (chosen by user)

def calculate_score(s1, s2, l1, l2, startpoint):
    """calculate alignment scores"""
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):

#	import ipdb; ipdb.set_trace() ## debug breakpoint added

        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

print("Slave is writing your best results into report...")
f=open("../Data/result.txt","w")

for i in range(l1): # Note that you just take the last alignment with the highest score
    # import ipdb; ipdb.set_trace() ## debug breakpoint added
    z = calculate_score(s1, s2, l1, l2, i)
    print("cal: pos ",i," with ",z)

    if z >= my_best_score:
        my_best_align = "." * i + s2 # think about what this is doing!
        my_best_score = z 


        f.write(my_best_align+"\n")
        f.write(s1+"\n")
        f.write("Best score:"+str(my_best_score)+"\n\n")
        print(my_best_align)
        print(s1)
        print("Best score:", my_best_score)

f.close()
print("Slave finishes its report")
