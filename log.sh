#!/bin/bash
LOG_ROOT='/home/y/var/log'
BIN_ROOT='/home/liulei/log'
LOG_FILES="\
openapi_access_log \
backend_access_log \
frontend_access_log \
yongche-app-api_access_log \
driver-api_access_log \
papi_access_log \
atm_access_log \
chat_papi_access_log \
message_papi_access_log \
user_access_log \
asset_access_log"

YESTERDAY=`date -d 'yesterday' '+%Y%m%d'`
YESTERDAYMONTH=`date -d 'yesterday' '+%Y%m'`
MAIL_FILE=/home/liulei/log/for_mail.txt




function write_log() #$file
{
	echo $1| awk -F '/|-' '{print $6"\t\t"$8}' 2>/dev/null >> $MAIL_FILE
	[ -f $1 ] && zcat $1| python $BIN_ROOT/retest2.py >> $MAIL_FILE ||exit 2
	#echo -e "\033[33m======================================= \033[0m" >> $MAIL_FILE
	echo -e "======================================= " >> $MAIL_FILE
}

function std_out() #$file
{
	echo $1| awk -F '/|-' '{print $6"\t\t"$8}' 2>/dev/null
	[ -f $1 ] && zcat $1| python $BIN_ROOT/retest2.py ||exit 2
	echo -e "\033[33m======================================= \033[0m"
	#echo -e "======================================= " >> $MAIL_FILE
}

#function sendmail(){
#mail_test.py
#}

#main()
if [ $# -ne 2 ];then
    echo 'Usage: sh log.sh HOST PROJECT'
    echo 'e.g.: sh log.sh fe3 openapi'
    exit 1
fi


if [ -f $MAIL_FILE ]; then
	unlink $MAIL_FILE
fi

log_file="$2_access_log"
host=$1
if [ ! -f $LOG_ROOT/$host/$YESTERDAYMONTH/$log_file-$YESTERDAY.gz ]; then
    echo gzfile is not exist
    exit 1
fi
FILES=`ls $LOG_ROOT/$host/$YESTERDAYMONTH/$log_file-$YESTERDAY.gz 2>/dev/null`

#标准输出
std_out $FILES

#编辑邮件内容
write_log $FILES


#发邮件
cat $MAIL_FILE | python mail_test.py

if [ -f $MAIL_FILE ]; then
     unlink $MAIL_FILE
fi
