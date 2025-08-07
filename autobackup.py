#!/usr/bin/env python3

import sys
import subprocess
import argparse
import os
import datetime
import glob
import re

def logging(message):
     logpath = re.sub(r'\/[^/]*$',"/log.txt",sys.argv[0]) #replace the end of current path to /log.txt
     time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #time stamp
     try:
          file = open(logpath,"a") #open log file for logging
          file.write(f"[{time}] {message}\n") #write into the log file
          file.close()
     except:
          pass

parser = argparse.ArgumentParser() #create argparse object
parser.add_argument("target_path", nargs="?") #add a positional argument target_path into the python script
parser.add_argument("dest_path", nargs="?") #add dest_path positional argument
parser.add_argument("backup_name", nargs="?") #add backup_name positional argument
args = parser.parse_args() #make a object that contain all the argument entered

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
target_path = f"{args.target_path}" #target path from cron job for example: "-C /home/thko1/ops445/a2 things"
dest_path = f"{args.dest_path}" #destination path for example: "/home/thko1/ops445/backup/"
backup_name = f"{args.backup_name}_{timestamp}" 

try:
    os.makedirs(dest_path, exist_ok=True) #check if it can make file in the destination path 
except IOError:
     logging("Error: Auto backup failed. Deleteing crontab...") #make log of backup failed
     removecroncmd = f'crontab -l | grep -v \'{sys.argv[0]} "{sys.argv[1]}" {sys.argv[2]} {sys.argv[3]}\' | crontab -' #delete cronjob command
     process = subprocess.Popen(removecroncmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #run the delete cronjob command
     exit()

tar_cmd = f"tar cvzf {dest_path}{backup_name}.tar.gz {target_path}" #tar command for backup
process = subprocess.Popen(tar_cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #run the tar command
process.wait() # wait a bit

if process.returncode == 0: #if backup is sucessful
     target = args.target_path.rsplit(" ",2)
     if len(target) > 1: #for edge case of file starting from root / for example /etc
          target = target[1] + "/" + target[2]
     logging(f"Auto backup of {target} was sucessful!") #log a message of backup sucessful
else: #if backup is not sucessful
     logging("Error: Auto backup failed. Deleteing crontab...") #log a message of backup not sucessful
     removecroncmd = f'crontab -l | grep -v \'{sys.argv[0]} "{sys.argv[1]}" {sys.argv[2]} {sys.argv[3]}\' | crontab -' #delete cronjob command
     process = subprocess.Popen(removecroncmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) #run deletecron job command
     exit()

filelist = glob.glob(f"{dest_path}{sys.argv[3]}_*_*.tar.gz") #get all the backup file path in a list
if len(filelist) > 10: # if there are more than 10 backup
     filelist.sort() #sort the list from old to new
     os.remove(filelist[0]) #delete the oldest backup
     logging(f"Older backup of {filelist[0]} was removed!") #log the backup deleted
