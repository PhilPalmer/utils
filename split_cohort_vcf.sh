#!/usr/bin/env bash
for sample in `bcftools query -l sampleA.vcf.gz`
do
  bcftools view -s $sample -Oz -o ${sample}.vcf.gz sampleA.vcf.gz
done