##### This program takes the files modified in the last 24 hours and transfers them to an archive folder #######

import time
import os
import shutil
from datetime import datetime

today = datetime.now()
SECONDS_IN_DAY = 24 * 60 * 60

src = "C:\Vision\Data\Archive"
dst = "E:\Data\Vision_PC_1_" + today.strftime('%Y_%m_%d')

if not os.path.exists(dst):
    os.makedirs(dst)

now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    if last_mod_time(src_fname) > before:
        dst_fname = os.path.join(dst, fname)
        shutil.copy(src_fname, dst_fname)
