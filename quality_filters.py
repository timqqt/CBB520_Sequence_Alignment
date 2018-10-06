from Bio import SeqIO
good_base_count = 0 # for counting high quality base
good_pairs_count = 0 # counting the high quality pairs
globals_steps = 0
# total_good_pairs_length = 0
for rec in SeqIO.parse("SRR4841864.fastq", "fastq"):
    sequences = rec.seq
    sequences_quality = rec.letter_annotations["phred_quality"]
    for base, base_quality in zip(sequences, sequences_quality):
        a = base
        b = base_quality
        if base_quality >= 25:
            good_base_count += 1
        else:
            if good_base_count >= 50:
                good_pairs_count += 1
                good_base_count = 0
                break
            good_base_count = 0
    if globals_steps % 10000:
        print("Global Step: ", globals_steps)
    globals_steps += 1

print ",Total numeber of good pairs is %d" % good_pairs_count
print ",The number of coverages it represents is %d" % good_pairs_count*101/(1.3*10**7)