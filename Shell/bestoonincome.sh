#!/bin/bash

source "$(dirname $0)"/bestoonconfig.sh

TOKEN=$1
AMOUNT=$2
shift
shift
TEXT=$*

curl --data "token=$TOKEN&amount=$AMOUNT&text=$TEXT" $BASE_URL/submit/income/
