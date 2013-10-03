




for i in $(seq 5)
do
mkfifo pipe$i
nohup python getFileFromFtp.py |grep -v "signature" > pipe$i &
nohup psql -a -U zakupki < pipe$i |gzip -c > client$i.log.gz &
sleep 10
done
