#!/usr/bin/env bash
# docker run -it -v $PWD:$PWD -w $PWD halllab/bcftools:v1.9 bash
for sample in `bcftools query -l sampleA.vcf.gz`
do
  bcftools view -s $sample -Oz -o ${sample}.vcf.gz sampleA.vcf.gz
done