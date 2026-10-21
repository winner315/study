import subprocess
import sys
import time

server = subprocess.Popen([sys.executable, '-m', 'sql.api_server'])
time.sleep(3)

try:
    subprocess.run([sys.executable,'-m','pytest','sql/test_api_db.py','-v'])
finally:
    server.terminate()