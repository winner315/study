import subprocess
import sys
import time

server = subprocess.Popen([sys.executable,'sql/api_server.py'])
time.sleep(3)

try:
    subprocess.run([sys.executable,'-m','pytest','sql/test_api_db.py','-v'])
finally:
    server.terminate()