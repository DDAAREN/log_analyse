#!/usr/bin/env python
LOG_ROOT='/home/y/var/log'
LOG_FILES=('openapi_access_log','backend_access_log','frontend_access_log','yongche-app-api_access_log','driver-api_access_log','papi_access_log','atm_access_log','chat_papi_access_log','message_papi_access_log','user_access_log','asset_access_log')


YESTERDAY=`date -d 'yesterday' '+%Y%m%d'`
YESTERDAYMONTH=`date -d 'yesterday' '+%Y%m'`
MAIL_FILE='for_mail.txt'


if [ -f $MAIL_FILE ]; then
	unlink $MAIL_FILE
fi

for log_file in $LOG_FILES
do
	FILES=`ls $LOG_ROOT/*/$YESTERDAYMONTH/$log_file-$YESTERDAY.gz 2>/dev/null`
	echo $FILES
done
