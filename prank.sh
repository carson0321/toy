#!/bin/bash
#########################################################################
# File Name: prank.sh
# Author: Carson Wang
# mail: carson.wang@droi.com
# Created Time: 2018-03-23 14:52:43
#########################################################################

pts=$(eval "lsof /dev/pts/* | grep '$1' | awk '{print \$9}' | uniq")
echo $pts
array=(${pts//\ / })
echo "Send $2 message to $1"
for i in "${!array[@]}"
do
    echo "$i=>${array[i]}"
    echo $2 > ${array[i]}
done
