#!/usr/bin/env python3

import subprocess
import sys
import os
import datetime
#sources https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
import glob
import re

def logging(message):
     logpath = re.sub(r'\/[^/]*$',"/log.txt",sys.argv[0])
     time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
     try:
          file = open(logpath,"a")
          file.write(f"[{time}] {message}\n")
          file.close()
     except:
          pass

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
target_path = sys.argv[1]
dest_path = f"{sys.argv[2]}"
backup_name = f"{sys.argv[3]}_{timestamp}"

try:
    os.makedirs(dest_path, exist_ok=True)
except IOError:
     logging("Error: Auto backup failed. Deleteing crontab...")
     removecroncmd = f'crontab -l | grep -v \'{sys.argv[0]} "{sys.argv[1]}" {sys.argv[2]} {sys.argv[3]}\' | crontab -'
     process = subprocess.Popen(removecroncmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)   
     exit()

tar_cmd = f"tar cvzf {dest_path}{backup_name}.tar.gz {target_path}"
process = subprocess.Popen(tar_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
process.wait()

if process.returncode == 0:
     target = sys.argv[1].rsplit(" ",2)
     target = target[1] + "/" + target[2]
     logging(f"Auto backup of {target} was sucessful!")
else:
     logging("Error: Auto backup failed. Deleteing crontab...")
     removecroncmd = f'crontab -l | grep -v \'{sys.argv[0]} "{sys.argv[1]}" {sys.argv[2]} {sys.argv[3]}\' | crontab -'
     process = subprocess.Popen(removecroncmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
     exit()

filelist = glob.glob(f"{dest_path}{sys.argv[3]}_*_*.tar.gz")
if len(filelist) > 10:
     filelist.sort()
     os.remove(filelist[0])
     logging(f"Older backup of {filelist[0]} was removed!")