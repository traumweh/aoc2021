#!/usr/bin/env bash
cd "$( dirname "${BASH_SOURCE[0]}" )"

[ -n "$0" ] && [ "$0" -eq "$0" ] 2>/dev/null
if [ $? -ne 0 ]; then
    dir=$(printf "days/%02d" $1)
    mkdir $dir
    touch $dir/input
    cp template.py $dir/solution.py
else
    echo "Requires number parameter"
fi