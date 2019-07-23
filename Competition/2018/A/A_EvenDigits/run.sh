#!/bin/bash
echo "brute force"
g++ bruteforce.cpp
cat sample.txt | ./a.out
echo "improved: greedy"
g++ improved.cpp
cat sample.txt | ./a.out
g++ -DDEBUG=1 improved.cpp
cat custom.txt | ./a.out
rm a.out
