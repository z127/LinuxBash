#!/bin/bash

start_dt=$1
end_t=$2

days=$((($(date -d $2 +%s)-$(date -d $1 +%s))/60/60/24))
date_end=$end_t
date_start=$start_dt

for((i=$days;i>0;i--));do
	dt=`date -d "$date_end $i days ago" +%Y-%m-%d`
	echo ${dt}
	#python 123  ${dt}i
done
