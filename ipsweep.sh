#!/bin/bash

#Most basic ip sweeper!
#Feel free to edit to your liking

if [ "$1" == ""  ]
then
echo "Mising Ip Adress"
echo "Input format: ./ipsweep.sh 198.162.1"

else
for ip in `seq 1 254`; do
ping -c $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
