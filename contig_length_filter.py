#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:58:28 2020

@author: dylan
"""

#import os
#import sys
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description='filename, then contig length threshold')

parser.add_argument('filename', type=str, help='path to fasta file')
parser.add_argument('min_length', type=int, help='minimum length of contigs to allow.')

args = parser.parse_args()

input_file = args.filename

min_contig_length = args.min_length


my_seq = SeqIO.parse(input_file, "fasta")

#placeholder list construct
longer_contigs = []
filter_counter = 0

for record in my_seq:
    if len(record.seq) > min_contig_length:
        longer_contigs.append(record)
    else:
        filter_counter = filter_counter + 1


SeqIO.write(longer_contigs, ("filtered_" + input_file), "fasta" )
print(f'{filter_counter} contigs removed')

        

