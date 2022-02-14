#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author(s): Laura Stahlhut
# date: 01.12.2021

# Functions to calculate accuracy, precision, recall and F-measure

import sys
import os


def accuracy(TP, FP, TN, FN):
    try:
        a = round((TP+TN)/(TP+TN+FP+FN), 2)
    except ZeroDivisionError:
        a = "NA"
    return a


def precision(TP, FP):
    try:
        p = round(TP/(TP+FP), 2)
    except ZeroDivisionError:
        p = "NA"
    return p


def recall(TP, FN):
    try:
        r = round(TP/(TP+FN), 2)
    except ZeroDivisionError:
        r = "NA"
    return r


def f_measure(TP, FP, FN):
    try:
        f = round(2*TP/((2*TP)+FP+FN), 2)
    except ZeroDivisionError:
        f = "NA"
    return f


def get_max(POS_list, accuracies, precisions, recalls, f_measures):
    "get the maximum value for each of the four measures along with their pos tag"
    max_a = max(accuracies)
    max_p = max(precisions)
    max_r = max(recalls)
    max_f = max(f_measures)

    for pos, a in zip(POS_list, accuracies):
        if a == max_a:
            max_a_line = pos + "\t"+ str(a)

    for pos, p in zip(POS_list, precisions):
        if p == max_p:
            max_p_line = pos + "\t"+ str(p)

    for pos, r in zip(POS_list, recalls):
        if r == max_r:
            max_r_line = pos + "\t"+ str(r)

    for pos, f in zip(POS_list, f_measures):
        if f == max_f:
            max_f_line = pos + "\t"+ str(f)

    return max_a_line, max_p_line, max_r_line, max_f_line


def output(newlines, max_values):
    print("POS\tA\tP\tR\tF")
    print("-----------------------")
    for line in newlines:
        print(line)
    print("Best accuracy: " + max_values[0])
    print("Best precision: " + max_values[1])
    print("Best recall: " + max_values[2])
    print("Best f-measure: " + max_values[3])


def main():
    newlines = []
    accuracies = []
    precisions = []
    recalls = []
    f_measures = []
    POS_list = []

    with open(os.path.join("data/", sys.argv[1]), 'r') as infile:
        next(infile)
        measurements = infile.readlines()

        for line in measurements:
            # get values
            POS = line.split("\t")[0]
            POS_list.append(POS)
            TP = int(line.split("\t")[1])
            FP = int(line.split("\t")[2])
            TN = int(line.split("\t")[3])
            FN = int(line.split("\t")[4].rstrip())

            # get measures
            a = accuracy(TP, FP, TN, FN)
            p = precision(TP, FP)
            r = recall(TP, FN)
            f = f_measure(TP, FP, FN)

            # get new line format for output
            newlines.append(POS + "\t" + str(a) + "\t" + str(p) + "\t" + str(r) + "\t" + str(f))

            # fill lists for max calculation
            if a == "NA":
                accuracies.append(0)
            else:
                accuracies.append(a)
            if p == "NA":
                precisions.append(0)
            else:
                precisions.append(p)
            if r == "NA":
                recalls.append(0)
            else:
                recalls.append(r)
            if f == "NA":
                f_measures.append(0)
            else:
                f_measures.append(f)

    max_values = get_max(POS_list, accuracies, precisions, recalls, f_measures)
    
    output(newlines, max_values)


if __name__ == main():
    main()