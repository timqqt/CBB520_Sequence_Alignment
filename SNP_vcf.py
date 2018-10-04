print ",\nThe statistics result of SNPs and INDELs  is shown as follows and you can see the bar plot of the statistics by clicking the button."
print ",Begin searching SNPs.......\n "

import matplotlib as mpl
mpl.use('Agg')

import vcf
import numpy as np
import matplotlib.pyplot as plt

SNP_type_list = np.array(['A->T', 'A->C', 'A->G', 'T->A', 'T->C', 'T->G', 'C->A', 'C->T', 'C->G', 'G->A', 'G->T', 'G->C'])
SNP_num_list = np.zeros(12)
vcf_reader = vcf.Reader(filename=r'WORK1.vcf')
for record in vcf_reader:
    # print(record)
    if record.is_snp:
        # print(str(record.REF)+'->'+ str(record.ALT)[1])
        index_snp = np.where(SNP_type_list == (str(record.REF)+'->' + str(record.ALT)[1:-1])) # from 0 to 11
        SNP_num_list[index_snp] += 1

print ",\n", SNP_num_list
print ",\n", SNP_type_list
print "\n,"
plt.figure(figsize=(8, 4))
plt.bar(SNP_type_list, SNP_num_list)
plt.title("SNPs Statistics")
plt.savefig("SNPs_bar_plot.png")