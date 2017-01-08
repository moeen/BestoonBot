#!/bin/bash

source "$(dirname $0)"/bestoonconfig.sh

TOKEN=$1
curl --data "token=$TOKEN" $BASE_URL/q/generalstat/
