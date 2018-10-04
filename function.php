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
<form method="post" action="/SRA_DB/S288c/function2.php">
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
// print_r(shell_exec("whoami"));
if(!file_exists("/var/www/html/SRA_DB/SRR4841864"))
print_r(shell_exec("wget https://sra-download.ncbi.nlm.nih.gov/traces/sra7/SRR/004728/SRR4841864 && echo 'Successfully download SRR4841864' "));
else
echo "<br>The SRR file already exists.";

if(!file_exists("/var/www/html/SRA_DB/SRR4841864.fastq"))
print_r(shell_exec("fastq-dump --split-spot SRR4841864 && echo '<br>Successfully transfer SRR4841864 to fastq' "));
    //echo '<br>Successfully transfer SRR4841864 to fastq' ;
else
     echo "<br>The .fastq file already exists.";
        
//print_r(shell_exec("wget https://sra-download.ncbi.nlm.nih.gov/traces/sra7/SRR/004728/SRR4841864 && echo 'Successfully download SRR4841864' "));
#echo "<br>";
//print_r(shell_exec("fastq-dump --split-spot SRR4841864 && echo '<br>Successfully transfer SRR4841864 to fastq' "));
echo "<br>Finish!<br>";
$output = shell_exec("python quality_filters.py");
$array = explode(',', $output);

foreach ($array as $value) {
echo "\n";
echo $value;
echo "<br>";
}

?>