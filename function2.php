<html>
<head>
<style>
#dog{
  text-align:center;
}
</style>
</head>
<body>
<div id="dog">
<form method="post" action="/SRA_DB/S288c/function3.php">
<input type="submit" id="btn1" value="Next Step" onClick="bt_click();">
</form>

</div>
<body>
</html>
<script>
function bt_click(){
alert('Please wait....'); 
var btn1 = document.getElementById("btn1");
btn1.disabled=true;
}
</script>
<?php
if(!file_exists("/var/www/html/SRA_DB/S288c/WORK1.mem.sam")){
	print_r(shell_exec("bwa index -p genome Saccharomyces_cerevisiae.R64-1-1.dna.chromosome.I.fa &&  echo '<br>Successfully build up index' "));
	print_r(shell_exec("bwa mem -t 4 genome SRR4841864.fastq > WORK1.mem.sam &&  echo '<br>Successfully generate .sam for alignment' "));}
else
	echo "<br>The .sam file already exists.";

if(!file_exists("/var/www/html/SRA_DB/S288c/WORK1.sorted.bam")){
	print_r(shell_exec("samtools view -bS WORK1.mem.sam > WORK1.bam &&  echo '<br>Successfully build up .bam' "));
	print_r(shell_exec("samtools sort WORK1.bam WORK1.sorted &&  echo '<br>Successfully sort .bam' "));}
else
	echo "<br>The .bam file already exists.";

if(!file_exists("/var/www/html/SRA_DB/S288c/WORK1.vcf")){
	print_r(shell_exec("samtools index WORK1.sorted.bam &&  echo '<br>Successfully build up index for sorted bam' "));
	print_r(shell_exec("samtools mpileup -d 1000 -gSDf Saccharomyces_cerevisiae.R64-1-1.dna.chromosome.I.fa WORK1.sorted.bam |bcftools view -cvNg -> WORK1.vcf &&  echo '<br>Successfully generate .vcf for detection on SNPs and INDELS' "));}
else
	echo "<br>The file for counting SNPs and INDELs is already generated.";

?>