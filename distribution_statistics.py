print ",Begin Calculating Distributions.......\n"
import matplotlib as mpl
mpl.use('Agg')



import re
import vcf
import math
import numpy as np
import collections as cl
import matplotlib.pyplot as plt
Roman2numb = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9
    , "X": 10, "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15, "XVI": 16, "Mito": 17}
Chrome_size_list = (10**6)*np.array([0.23, 0.81, 0.32, 1.53
            , 0.58, 0.27, 1.09, 0.56, 0.44, 0.75, 0.67, 1.08, 0.92, 0.78, 1.09, 0.95, 0.09])
INDEL_type_list = np.array(['+A', '-A', '+T', '-T', '+C', '-C', '+G', '-G'])
SNP_type_list = np.array(['A->T', 'A->C', 'A->G', 'T->A', 'T->C', 'T->G', 'C->A', 'C->T', 'C->G', 'G->A', 'G->T', 'G->C'])
SNP_num_list = np.zeros(12)
INDEL_num_list = np.zeros(8)
vcf_reader = vcf.Reader(filename=r'WORK1.vcf')
total_length = np.sum(Chrome_size_list)
window_size = 10*(10**3)
bins_size = math.ceil(total_length/window_size)
windows_count = {'SNPs': np.zeros(bins_size), 'INDELs': np.zeros(bins_size)}
for record in vcf_reader:
    # print(record.POS)
    index_bin = math.floor((record.POS + np.sum(Chrome_size_list[:Roman2numb[record.CHROM]-1]))/window_size)
    if record.is_snp:
        windows_count['SNPs'][index_bin] += 1
    if record.is_indel:
        ref = cl.Counter(record.REF)
        alt_string = re.sub('[\[\],]', '', str(record.ALT))
        alt = cl.Counter(alt_string)
        for base in ['A', 'T', 'C', 'G']:
            diff = alt[base] - ref[base]
            windows_count['INDELs'][index_bin] += abs(diff)

plt.figure(1, figsize=(8, 4))
fig1 = plt.plot(window_size*np.arange(1, bins_size+1), windows_count['SNPs'])
plt.title("SNPs Distribution Statistics")
plt.ylim(0,)
plt.savefig("Distribution_snp.png")
plt.figure(2, figsize=(8, 4))
fig2 = plt.plot(window_size*np.arange(1, bins_size+1), windows_count['INDELs'])
plt.title("INDELs Distribution Statistics")
plt.ylim(0,)
# plt.show()
plt.savefig("Distribution_indel.png")


mean_SNPs = np.mean(windows_count['SNPs'])
std_SNPs = np.std(windows_count['SNPs'])
count_high_SNPs = 0
mean_INDELs = np.mean(windows_count['INDELs'])
std_INDELs = np.std(windows_count['INDELs'])
count_high_INDELs = 0
# find windows have SNPs or INDELs more than four deviations from mean
for each_SNPs_count, each_INDELs_count in zip(windows_count['SNPs'], windows_count['INDELs']):
    if each_SNPs_count > (mean_SNPs+4*std_SNPs):
        count_high_SNPs += 1
    if each_INDELs_count > (mean_INDELs+4*std_INDELs):
        count_high_INDELs += 1

print ",\nThe mean of SNPs is ", mean_SNPs
print "\n"
print ",\nThe deviation of SNPs is ", std_SNPs
print "\n"
print ",\nThe number of a window has SNPs more than 4 std from the mean is ", count_high_SNPs
print "\n"
print ",\nThe mean of INDELs is ", mean_INDELs
print "\n"
print ",\nThe deviation of INDELs is ", std_INDELs
print "\n"
print ",\nThe number of a window has INDELs more than 4 std from the mean is ", count_high_INDELs
print "\n"

