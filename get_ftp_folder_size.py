#!/usr/bin/env python3

"""
Get size of folder on FTP server in bytes
from: https://stackoverflow.com/questions/22090001/get-folder-size-using-ftplib
depends on:
> python 3
> ftplib
> os
"""

import os
from ftplib import FTP

# Change
ftp_server = 'ftp.ncbi.nlm.nih.gov'
ftp_dir = '/pub/clinvar/vcf_GRCh38/'

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

def list_files(ftp_server, ftp_dir):
    files = ftp.nlst(ftp_dir)
    for f in files:
        print(f"{ftp_server}/{f}")

list_files(ftp_server, ftp_dir)
print(get_total_size(ftp_dir))