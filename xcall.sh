#!/bin/bash
echo hello

params=$@
i=102


for(( i = 102 ; i <= 105 ; i = $i + 1 )) ; do
	echo ========= s$i   $params  ==  =====
	ssh s$i  "$params" 
done
