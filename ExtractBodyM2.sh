#!/bin/bash
inputdir=$1
tail -n +2 $inputdir | cut -d "," -f 2-6 | tr -s "," " " | sort -r -n -k 6
