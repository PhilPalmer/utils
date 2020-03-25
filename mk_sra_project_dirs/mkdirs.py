#!/usr/bin/env python3

"""
Move FASTQ files from SRA into subdirectories based on their BioProjects
depends on:
> python 3
> pandas==0.24.2
> os
"""

import pandas as pd
import os

data_dir = 'test'
sra_run_table = pd.read_csv('SraRunTable.txt')
sra_ids = sra_run_table['Run']
projects = sra_run_table['BioProject']

# For each SRA ID
for i in range(len(sra_ids)):
  sra_id = sra_ids[i]
  project = projects[i]
  project_dir = f"{data_dir}/{project}"
  mv_cmd = f"mv {data_dir}/{sra_id}* {data_dir}/{project}"
  # Check if file(s) for that SRA ID exist
  if any(File.startswith(sra_id) for File in os.listdir(data_dir)):
    # Make project dir
    if not os.path.exists(project_dir):
      os.makedirs(project_dir)
    # Move SRA files to project dir
    os.system(mv_cmd)
  else:
    # Save missing SRA IDs to file
    with open("missing_rsids.txt", "a") as missing_rsids:
      missing_rsids.write(f"{sra_id}\n")