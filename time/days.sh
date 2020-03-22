#!/bin/bash

default_dt=`date +%Y-%m-%d -d "1 hour ago"`
default_before_hour=`date +%H -d "1 hour ago"`
default_next_hour=`date +%H -d "1 hour"`
echo ${default_dt}
echo ${default_before_hour}
echo ${default_next_hour}
