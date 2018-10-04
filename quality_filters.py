from Bio import SeqIO
import math
good_base_count = 0 # for counting high quality base
good_pairs_count = 0 # counting the high quality pairs
good_pairs_list = []
good_pairs_quality_list = []
total_good_pairs_length = 0
for rec in SeqIO.parse("SRR4841864.fastq", "fastq"):
    sequences = rec.seq
    sequences_quality = rec.letter_annotations["phred_quality"]
    for base, base_quality in zip(sequences, sequences_quality):
        a = base
        b = base_quality
        if base_quality > 25:
            good_base_count += 1
            good_pairs_list.append(base)
            good_pairs_quality_list.append(base_quality)
        else:
            if good_base_count >= 50:
                good_pairs_count += 1
                total_good_pairs_length += good_pairs_count
                # print "The number of good pairs is %d" % good_pairs_count
                # print good_pairs_list
                # print good_pairs_quality_list
            # Then reset
            good_pairs_list = []
            good_pairs_quality_list = []
            good_base_count = 0

print ",\nTotal numeber of good pairs is %d" % good_pairs_count
print  ",The length of total good pairs is %d" % total_good_pairs_length
coverage = math.floor(total_good_pairs_length/13000000)
print ", The number of coverages is %d" % coverage
