#!/usr/bin/env bash

# testdata:
# https://opensnp.org/data/9090.23andme.7430
# https://opensnp.org/data/9088.23andme.7429
# https://opensnp.org/data/9087.23andme.7428
# https://opensnp.org/data/9084.23andme.7424
# https://opensnp.org/data/9083.23andme.7423
# https://www.opensnp.org/data/8117.23andme.7420
# https://www.opensnp.org/data/9080.23andme.7419
# https://www.opensnp.org/data/9078.23andme.7417
# https://www.opensnp.org/data/9077.23andme.7416
# https://www.opensnp.org/data/9076.23andme.7415
# https://www.opensnp.org/data/9073.23andme.7414
# https://www.opensnp.org/data/9072.23andme.7413
# https://www.opensnp.org/data/9069.23andme.7411
# https://www.opensnp.org/data/9066.23andme.7410
# https://www.opensnp.org/data/9055.23andme.7405
# https://www.opensnp.org/data/8389.23andme.7399
# https://www.opensnp.org/data/9048.23andme.7397
# https://www.opensnp.org/data/7611.23andme.7392
# https://www.opensnp.org/data/9044.23andme.7390
# https://www.opensnp.org/data/9042.23andme.7387

genotype_files=$(ls *)

for genotype_file in $genotype_files; do
  mv $genotype_file ${genotype_file}.txt
done

fasta_file='hs37d5.fa' # from s3://lifebit-featured-datasets/modules/beagle5/hs37d5.fa.gz
genotype_files=$(ls *.txt)

for genotype_file in $genotype_files; do
  name=${genotype_file%.*}
  #echo $name
  bcftools convert --tsv2vcf ${genotype_file} -f ${fasta_file} -s $name -Oz -o ${name}.vcf.gz
done



