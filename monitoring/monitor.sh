ps -aux | grep -v grep | grep facial.py | tee /home/bigfella/Desktop/v3/monitoring/kameraproces;
ps -aux | grep -v grep | grep MoveImgtoUSBCron.py | tee /home/bigfella/Desktop/v3/monitoring/emailproces;
python3 /home/bigfella/Desktop/v3/monitoring/kameratest.py
