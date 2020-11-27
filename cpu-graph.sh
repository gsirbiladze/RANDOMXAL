#!/bin/bash

cpu_info=($(cat /proc/stat | grep '^cpu '))
prev_cpu_numbers=(${cpu_info[@]:1})

while true; do
    cpu_info=($(cat /proc/stat | grep '^cpu '))
    cpu_numbers=(${cpu_info[@]:1})
    actual_cpu_numbers=()
    for i in $(seq 0 $[${#cpu_numbers[@]}-1])
    do
        actual_cpu_numbers=(${actual_cpu_numbers[@]} $[${cpu_numbers[$i]}-${prev_cpu_numbers[$i]}]);
    done
    prev_cpu_numbers=(${cpu_numbers[@]})

    
    whole_cpu_time=${actual_cpu_numbers[@]}
    whole_cpu_time=$[${whole_cpu_time// /+}]

    idle_pct=$[(${actual_cpu_numbers[3]} * 100)/$whole_cpu_time]
    busy_pct=$[100-$idle_pct]

    echo -e "\x1b[1;7;8;31m$(printf %${busy_pct}s '')\x1b[0m\x1b[1;7;8;32m$(printf %${idle_pct}s '')\x1b[0m"
    sleep 0.5
done

