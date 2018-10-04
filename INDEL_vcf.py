print ",Begin searching INDELs.......\n"
import matplotlib as mpl
mpl.use('Agg')



import re
import vcf
import numpy as np
import collections as cl
import matplotlib.pyplot as plt
INDEL_type_list = np.array(['+A', '-A', '+T', '-T', '+C', '-C', '+G', '-G'])
INDEL_num_list = np.zeros(8)
vcf_reader = vcf.Reader(filename=r'WORK1.vcf')


def what_sign(x):
    if x >= 0:
        return '+'
    else:
        return '-'


for record in vcf_reader:
    if record.is_indel:
        ref = cl.Counter(record.REF)
        alt_string = re.sub('[\[\],]', '', str(record.ALT))
        alt = cl.Counter(alt_string)
        for base in ['A', 'T', 'C', 'G']:
            diff = alt[base] - ref[base]
            type_indel = what_sign(diff)+base
            index_indel = np.where(INDEL_type_list == type_indel)  # from 0 to 11
            INDEL_num_list[index_indel] += abs(diff)

plt.figure(figsize=(8, 4))
plt.bar(INDEL_type_list, INDEL_num_list)
plt.title("INDELs Statistics")
plt.savefig("INDELs_bar_plot.png")
print ",\n", INDEL_num_list
print ",\n", INDEL_type_list
