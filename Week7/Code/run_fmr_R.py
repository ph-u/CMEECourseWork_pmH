#!/bin/env python3

# Author: ph-u
# Script: run_fmr_R.py
# Desc: call fmr.R from python3 terminal environment
# Input: python3 run_fmr_R.py
# Output: terminal output
# Arguments: 0
# Date: Nov 2019


"""call fmr.R from python3 terminal environment"""

__appname__="run_fmr_R.py"
__author__="ph-u"
__version__="0.0.1"
__license__="None"

import subprocess

subprocess.Popen("Rscript fmr.R 2> ../results/fmr_err.Rout", shell=True).wait()
with open('../results/fmr_err.Rout', 'r') as f: text = f.read()
if len(text) > 0: print("python3 announcement: unsuccessful run")
else: print("python3 announcement: successful run")
