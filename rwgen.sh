#!/bin/bash

######################################################################################
# Grigol Sirbiladze
# 02/06/2017
# ###################################################################################

_ALL_LOWERCASE="a-z"
_ALL_UPPERCASE="A-Z"
_ALL_NUMBER="0-9"
_SYMBOLS="\-\_\+\=\~\!\@\#\$\%\^\&\*"
_MORE_SYMBOLS="\(\)\[\]\{\}\:\;\"\,\/\<\>\?"

# Make Sure Pattern Exists
_MSPE_LOWER=0
_MSPE_UP=0
_MSPE_SYM=0
_MSPE_MORE=0

_GEN_PATTERN=""
_LENGTH=12
_SWING=0
_COUNT=5

#---------------------------------------------------------------------------------------------------------------------------------
             ######################   FUNCTIONS   ##################################
#---------------------------------------------------------------------------------------------------------------------------------

print_message() {

        local print_date="{$(date)}"
        local whole_str_len="$(expr ${#1} \+ ${#print_date} \+ 2)"

        [[ "top" =~ ^("$2"|"$3")$ ]] && printf "\n%${whole_str_len}s\n"  | tr "\ " "-"  
        printf "{$(date)}  %s\n"   "$1"                                                  
        [[ "bottom" =~ ^("$2"|"$3")$ ]] && printf "%${whole_str_len}s\n" | tr "\ " "-"  
	
	#To exit with status 0 when we dont have 'bottom'
        return 0
}


word_contains_all_patterns(){

        local _word="$1"
        local _current_pattern="$2"

	if [ ${#_word} -lt 4 ] && [ ! -z "${_word//\ /}" ]; then

		echo "YES"
		exit 
	fi

        if [ ! -z $(echo "$_ALL_LOWERCASE" | tr -dc "$_current_pattern") ] && [ -z $(echo "$_word" | tr -dc "$_ALL_LOWERCASE") ]; then

                echo "Lowercase is missing ... "
		exit 
        fi

        if [ ! -z $(echo "$_ALL_UPPERCASE" | tr -dc "$_current_pattern") ] && [ -z $(echo "$_word" | tr -dc "$_ALL_UPPERCASE") ]; then

                echo "Uppercase is missing ... "
		exit 
        fi

        if [ ! -z $(echo "$_ALL_NUMBER" | tr -dc "$_current_pattern") ] && [ -z $(echo "$_word" | tr -dc "$_ALL_NUMBER") ]; then

                echo "Number is missing ... "
		exit 
        fi


        echo "YES"
}


usage_print(){

		echo	"

		Random words generator
		----------------------
		
   		Usage:
                        All arguments are case insensitive
			----------------------------------

			-up   :  Use upper case letters

                	-lo   :  Use lower case letters

                	-num  :  Use numbers

                	-sym  :  Use symbols

                        -more :  Use more symbols

                	-l    : Length of the generated word 

                	-s    : 'Swing' the length of the generated word by (-s)
                        
                        -c    : Quantity of the generated words

			------------------------------------------------------
			
			-h

			--help : Print this help

			-----------------------------------------------------

	"

}

#---------------------------------------------------------------------------------------------------------------------------------



while [ $# -ne 0 ]
do

	case "${1^^}" in

		"-UP") 
			_GEN_PATTERN="${_GEN_PATTERN}${_ALL_UPPERCASE}"
		;;

		"-LO") 
			_GEN_PATTERN="${_GEN_PATTERN}${_ALL_LOWERCASE}"
		;;

		"-NUM") 
			_GEN_PATTERN="${_GEN_PATTERN}${_ALL_NUMBER}"
		;;

		"-SYM") 
			_GEN_PATTERN="${_GEN_PATTERN}${_SYMBOLS}"
		;;

		"-MORE") 
			_GEN_PATTERN="${_GEN_PATTERN}${_MORE_SYMBOLS}"
		;;

		"-L")
			if [ -z "$2" ] || [ ! -z "${2//[0-9]/}" ]; then

				print_message " Argument ( -L ) requires number ... " top bottom
				usage_print
				exit 1						
			else
				_LENGTH=$2
                                shift
			fi
		;;
		
                "-S")
                        if [ -z "$2" ] || [ ! -z "${2//[0-9]/}" ]; then

                                print_message " Argument ( -S ) requires number ... " top bottom
                                usage_print
                                exit 1
                        else
                                _SWING=$(expr 1 + $2)
                                shift
                        fi
		;;

                "-C")
                        if [ -z "$2" ] || [ ! -z "${2//[0-9]/}" ]; then

                                print_message " Argument ( -C ) requires number ... " top bottom
                                usage_print
                                exit 1
                        else
                                _COUNT=$2
                                shift
                        fi
                ;;

                "-H" | "--HELP" | *)
			usage_print
			exit 0
                ;;
	esac

	shift
done


_GEN_PATTERN="${_GEN_PATTERN:-a-zA-Z0-9}"

for _nothing in $(seq $_COUNT)
do

	_RANDOM_WORD=""
	
	while [ "$(word_contains_all_patterns "$_RANDOM_WORD" "$_GEN_PATTERN" )" != "YES" ]; do

		if [ $_SWING -gt 1 ]; then

			_RANDOM_LENGTH_DIFFERENCE=$(expr $(cat /dev/urandom 2>/dev/null | tr -dc '0-9' 2>/dev/null | head -c 10) % $_SWING  )
			_RANDOM_WORD="$(cat /dev/urandom 2>/dev/null | tr -dc "$_GEN_PATTERN" 2>/dev/null | head -c $(expr  $_LENGTH + $_RANDOM_LENGTH_DIFFERENCE ) )"
		else
			_RANDOM_WORD="$(cat /dev/urandom 2>/dev/null | tr -dc "$_GEN_PATTERN" 2>/dev/null | head -c $_LENGTH)"
		fi
	done
	
	echo $_RANDOM_WORD
done



