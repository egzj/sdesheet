#!/bin/bash

topics=(
    "Arrays"
    "Arrays Part-II"
    "Arrays Part-III"
    "Arrays Part-IV"
    "Linked List"
    "Linked List Part-II"
    "Linked List and Arrays"
    "Greedy Algorithm"
    "Recursion"
    "Recursion and Backtracking"
    "Binary Search"
    "Heaps"
    "Stack and Queue"
    "Stack and Queue Part-II"
    "String"
    "String Part-II"
    "Binary Tree"
    "Binary Tree part-II"
    "Binary Tree part-III"
    "Binary Trees[Miscellaneous]"
    "Graph"
    "Graph Part-II"
    "Dynamic Programming"
    "Dynamic Programming Part-II"
    "Trie"
    "Operating System Revision"
    "DBMS Revision"
    "Computer Networks Revision"
    "Project Overview"
)

# loop through each index
for i in "${!topics[@]}"
do 
    # get topic 
    topic="${topics[$i]}"

    # add 1 to index as we start from day 1
    i=$((i+1))

    # prepend 0 if less than 10
    folder_name=`printf "day%02d ( %s )" "$i" "$topic"`

    # create folder if does not exists (ensure in right dir)
    mkdir -p "$folder_name"
done




