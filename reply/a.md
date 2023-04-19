## 回答
cat reply.txt | sed 's/Re://g;s/日目//;s/太郎->花子/>/;s/花子->太郎/</' | awk '{if(a[$3] == 0){a[$3]=$1}else{print $1-a[$3],$3}}' | sort -k1,1n
