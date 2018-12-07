#!/bin/sh
tr '\n' ' ' < input.txt | cut -c 2- | bc
