#!/bin/bash

#source ${HOME}/.profile

### Set up TAs in UG ###

year=$(date +%y)
#COURSES="prgm${year} prgi${year} datintro${year}p1"
COURSES="prgm${year} prgi${year}"

for course in ${COURSES}
do
  ug_path=$(nytid courses config ${course} ug.assistants | sed "s/.*= //")
  if test "$?" -ne 0; then
    echo "error: no ${course} in nytid"
    continue
  fi
  TAs=$(nytid signupsheets users ${course})
  if test "$?" -ne 0; then
    echo "error: can\'t read users for ${course} in nytid"
    continue
  fi
  if test -n "${TAs}"; then
    kthutils ug members add ${ug_path} ${TAs}
  else
    echo "warning: no-one signed up for ${course}"
  fi
done

### Generate schedules for TAs ###

#ICS_COURSES="(prg[im]23|datintro23p1)"
ICS_COURSES="prg[im]23"
ICS_DIR=~/afs/public_html/nytid

mkdir -p ${ICS_DIR}

for user in $(nytid signupsheets users "${ICS_COURSES}")
do
  nytid signupsheets ics "${ICS_COURSES}" --user ${user} \
    > ${ICS_DIR}/${user}.ics
done

# Update my schedule again with all courses this time
nytid signupsheets ics > ${ICS_DIR}/dbosk.ics 2> >(grep -v WARNING)

wait

