#!/usr/bin/env bash

# Arg parsing
if [ $# -eq 0 ] || [ "$1" == "help" ] ; then
  echo "Usage: $0 DAY_NUMBER"
  echo "    Sets up files for the advent day"
  echo "Arguments:"
  echo "    DAY_NUMBER: (Required) the number of the calendar day"
  echo 
  exit
fi

YEAR=2018
PROJECT_HOME=$HOME/git/aoc$YEAR
wget https://adventofcode.com/$YEAR/day/$1/input \
    --load-cookies=$PROJECT_HOME/cookies.txt \
    -O $PROJECT_HOME/inputs/day_$1.txt
cp $PROJECT_HOME/day_template.py $PROJECT_HOME/day_$1.py
sed -i.bak "4a\\
DAY_NR = $1" $PROJECT_HOME/day_$1.py
rm $PROJECT_HOME/day_$1.py.bak
