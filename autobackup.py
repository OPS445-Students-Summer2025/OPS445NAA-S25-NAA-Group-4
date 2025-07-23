#!/usr/bin/env python3

import subprocess
import sys
import os
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
target_path = sys.argv[1]
dest_path = f"{sys.argv[2]}"
backup_name = f"{sys.argv[3]}_{timestamp}"

try:
    os.makedirs(dest_path, exist_ok=True)
except IOError:
        exit()
tar_cmd = f"tar cvzf {dest_path}{backup_name}.tar.gz {target_path}"
process = subprocess.Popen(tar_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
process.wait()

if process.returncode == 0:
     pass
else:
     pass