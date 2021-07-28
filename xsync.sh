#!/bin/bash
if [[ $# -lt 1  ]]; then  echo  no param;exit ; fi
# 必须目标父目录存在,否则会有问题.
p=$1
#echo p=$p 
dir=$(dirname $p)
#echo dir=$dir
filename=$(basename $p)
#echo filename=$filename
cd -P  $dir 
fullpath=$(pwd -P .)
user=$(whoami)
echo $fullpath
for(( i = 102 ; i <= 105 ; i = $i + 1 )) ; do
	echo ========= s$i   $params  =======
	rsync -lr  $p ${user}@s$i:$fullpath  
done ;

