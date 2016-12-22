#!/bin/bash

RED='\x1B[0;31m'
GREEN='\x1B[0;32m'
YELLOW='\x1B[0;33m'
BLUE='\x1B[0;34m'
END_COLOR='\x1B[0m'

PYTHON=python3

UNDER_TEST=$1

TESTS=$2

display_summary () {
  if [ $1 -eq 0 ]
  then
    echo -e "${GREEN}SUCCESS${END_COLOR}"
  else
    echo -e "${RED}FAIL" >&2
    cat "$2" >&2
    echo -e "\n${END_COLOR}"
  fi
}

check () {
    cmp --silent $1 $2
    display_summary $? $1
}

run_tests () {
    for input_file in $TESTS/*.dat
    do
        file_name="${input_file##*/}"
        base_name="${file_name%.*}"
        output_file="${TESTS}/${base_name}.ans"
        tmp_file=$(mktemp)

        printf "${BLUE}test #$base_name:${END_COLOR} $f "

        ${PYTHON} ${UNDER_TEST} ${input_file} ${tmp_file}

        check ${tmp_file} ${output_file}

        rm ${tmp_file}
    done
}

run_tests
