#!/bin/bash

# Author: PokMan Ho pok.ho19@imperial.ac.uk
# Script: run_Mini_write.sh
# Desc: Master script file reproducing the MiniProject
# Input: ```./run_Mini_write.sh <tex> <start_line_num>```
# Output: write up a `tex` document for compiling
# Arguments: 0
# Date: Oct 2019

a1=$1
a2=$2
a3=`echo ${a1}|cut -f 1 -d "_"`

## Writing
cp $1 ${a3}_r.tex

## spacialize for *_r.tex
head -n 3 ${a3}_r.tex > tmp
echo -e '% Desc: Daughter script for corresponding final `LaTeX` report' >> tmp
tail -n +5 ${a3}_r.tex >> tmp

head -n 51 tmp > tmp1
echo -e $((`texcount tmp |tail -n 19|head -n 1|cut -f 2 -d ":"|cut -f 2 -d " "` -3 -13 -`grep -o "autocite{" ${a3}_r.tex |wc -l`)) >> tmp1
tail -n +52 ${a3}_r.tex >> tmp1

mv tmp1 tmp
mv tmp ${a3}_r.tex