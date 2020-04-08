#!/usr/bin/env python3

"""
Get URLs to download the 100 latest genotype files from OpenSNP
depends on:
> python 3
> bs4==0.0.1
> requests==2.21.0
> re
> time
"""
 
from bs4 import BeautifulSoup
import requests
import re
from time import sleep

# Change
n_genotypes = 100
output_filename = 'opensnp_genotype_urls.txt'

# Don't change
n_pages = n_genotypes // 20
max_range = n_pages + 1
genotype_file_names = []

# Get names of the genotype files from each scraped OpenSNP page
for page in range(1, max_range):
  url = 'https://opensnp.org/genotypes?page={}'.format(page)
  response = requests.get(url, timeout=10)
  content = BeautifulSoup(response.content, "html.parser")
  pattern = re.compile("../data/(.*)")
  for link in content.find_all('a'):
    link_url = link['href']
    if link_url.startswith('../data/'):
      genotype_file_name = pattern.search(link_url).group(1)
      genotype_file_names.append(genotype_file_name)

# Write URLs to download OpenSNP genotypes to file
download_base_url = 'https://opensnp.org/data/'
genotype_file_names = [download_base_url + genotype_file_name for genotype_file_name in genotype_file_names]
with open(output_filename, mode='wt', encoding='utf-8') as outfile:
    outfile.write('\n'.join(genotype_file_names))