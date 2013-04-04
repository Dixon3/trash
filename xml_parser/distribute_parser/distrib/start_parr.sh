




for i in $(seq 5)
do
mkfifo pipe$i
nohup python getFileFromFtp.py > pipe$i &
nohup psql -a -U zakupki < pipe$i > client$i.log &
sleep 10
done
