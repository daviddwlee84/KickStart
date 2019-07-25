#!/bin/bash
echo "recursive"
g++ recursive.cpp
cat sample.txt | ./a.out
echo "iterative"
g++ iterative.cpp
cat sample.txt | ./a.out
rm a.out
