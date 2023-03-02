#!/bin/bash
lines=$(ls $1 |wc -l)
echo "$1 contains $lines items"
