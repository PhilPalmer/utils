#!/usr/bin/env python3

"""
Get size of folder on FTP server in bytes
depends on:
> python 3
> ftplib
> os
"""

import os
from ftplib import FTP

# Change
ftp_server = 'ftp.ebi.ac.uk'
ftp_dir = '/pub/databases/gwas/summary_statistics/'

# Don't change
ftp = FTP(ftp_server)
ftp.login()

def get_total_size(ftp_dir):
    size = 0
    parent_dir = ftp.pwd() # get the current directory
    for filename in ftp.nlst(ftp_dir):
        # (don't forget to import os)
        path = os.path.join(parent_dir, filename) # keeps recursively track of the path
        try:
            ftp.cwd(path)
            size += get_total_size(path)
            ftp.cwd(parent_dir)
        except:
            ftp.voidcmd('TYPE I')
            size += ftp.size(path)
    return size

print(get_total_size(ftp_dir))