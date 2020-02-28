#!/bin/bash

read LEVEL

levels=(16 8 4 2 1)
id=0

member_of(){
     arr=(${@})
     arr=(${arr[@]:1})
     arr_checker=(${arr[@]/$1})
     [ ${#arr_checker[@]} -ne ${#arr[@]} ] && echo "YES"
}


if [ -z "${LEVEL/[0-9]}" -a -n "$(member_of $LEVEL 1 2 3 4 5)" ]; then
     LEVEL=$[LEVEL-1]
else
     LEVEL=4
fi

build_the_tree(){

    local lvl_const=$1
    local anchors=(${@})
    local anchors=(${anchors[@]:1})

    if [ $lvl_const -le ${levels[$LEVEL]} ]; then
        # Coplete lines
        for column in $(seq $[lvl_const*2-1])
        do
            line=""
            for row in {1..100}
            do
                line+="_"
            done
            echo $line
        done
    else       
        anchors_4_next_lvl=()
        for anc in ${anchors[@]}
        do
            anchors_4_next_lvl=(${anchors_4_next_lvl[@]} $[anc-lvl_const] $[anc+lvl_const])
        done
        build_the_tree $[lvl_const/2] ${anchors_4_next_lvl[@]}
    fi

    # echo "lvl_const: $lvl_const, anchors: ${anchors[@]}"

    for column in $(seq $lvl_const)
    do
        line=""

        # prev_left=0
        prev_right=0

        for row in ${anchors[@]}
        do
            left=$[row-(lvl_const-(column-1))]
            right=$[row+(lvl_const-(column-1))]

            printf -v tmp "%0$[left-prev_right]d%0$[right-left]d" 1 1 
            line+=$tmp

            # prev_left=left
            prev_right=$right

        done
        printf -v tmp "%0$[100-prev_right]d" 0
        line+=$tmp
        line=${line//0/_}
        printf "%s\n" "$line"
    done

    for column in $(seq $lvl_const)
    do
        line=""
        prev_row=0
        for row in ${anchors[@]}
        do
            printf -v tmp "%0$[row-prev_row]d" 1
            prev_row=$row
            line+=$tmp
        done

        printf -v tmp "%0$[100-prev_row]d" 0
        line+=$tmp
        line=${line//0/_}
        printf "%s\n" "$line"
    done
}

build_the_tree 16 50

