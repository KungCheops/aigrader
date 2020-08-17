#!/bin/bash

PATH_TO_SUBMISSIONS=$1

aigrader editdist -fi $PATH_TO_SUBMISSIONS && \
aigrader linkage $PATH_TO_SUBMISSIONS && \
aigrader cluster $PATH_TO_SUBMISSIONS -d 100 -n 4 && \
aigrader dendrogram $PATH_TO_SUBMISSIONS
