#!/bin/bash
## 必须目标fullpath中父目录存在,否则会出现问题
# 获取输出参数,如果没有参数则直接返回
pcount=$#
if [[ $pcount -lt 1  ]]; then  echo "no param";exit ; fi

#获取传输文件名字
filename=$1
echo "file name is  ${filename} ! "

#获取文件的绝对路径
pdir=`cd -P $(dirname ${filename}); pwd`
echo "file path is ${pdir}"

fullpath=${pdir}

user=$(whoami)
echo ${fullpath}
echo ${fullpath}/${filename}
for(( i = 200 ; i <= 202 ; i = $i + 1 )) ; do
        echo ========= s$i   $params  =======
        echo "rsync -lr  ${fullpath}/${filename} ${user}@s$i:${fullpath}"
        rsync -lr  ${fullpath}/${filename} ${user}@s$i:${fullpath}
done ;
