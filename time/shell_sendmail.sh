#! /bin/bash
dt=`date "+%Y-%m-%d %H:%M:%S"`
echo ${dt}
#cd /home/zhouqijun && python sendMail.py "${dt}"
echo `date "+%Y-%m-%d %H:%M:%S" -d "1 hour ago"`

cd /home/zhouqijun && python sendMail.py "`date "+%Y-%m-%d %H:%M:%S"`"
