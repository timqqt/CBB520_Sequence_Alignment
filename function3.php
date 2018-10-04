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
<form method="post" action="/main_page.php">
<input type="submit" id="btn1" value="Now all programs are finished. You can click here to go back to Homepage">
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
$output = shell_exec("python SNP_vcf.py");
$array = explode(',', $output);

foreach ($array as $value) {
echo "\n";
echo $value;
echo "<br>";
}



$output = shell_exec("python INDEL_vcf.py");
$array = explode(',', $output);

foreach ($array as $value) {
echo "\n";
echo $value;
echo "<br>";
}



$output = shell_exec("python distribution_statistics.py");
$array = explode(',', $output);

foreach ($array as $value) {
echo "\n";
echo $value;
echo "<br>";
}


echo "<br>";

?>




<html>
<head>
<style>
#dog{
  text-align:center;
}
</style>
<body>
<div id="dog">
<SCRIPT LANGUAGE="JavaScript">
function reP(){
	document.getElementById('img1').style.display = "block";
	document.getElementById('img2').style.display = "block";
	document.getElementById('img3').style.display = "block";
	document.getElementById('img4').style.display = "block";

}
</SCRIPT>
<img src='SNPs_bar_plot.png' id="img1" style='display:none' width="400px" hight="400px" align="middle">
<img src='INDELs_bar_plot.png' id="img2" style='display:none' width="400px" hight="400px" align="middle">
<img src='Distribution_snp.png' id="img3" style='display:none' width="400px" hight="400px" align="middle">
<img src='Distribution_indel.png' id="img4" style='display:none' width="400px" hight="400px" align="middle">
<INPUT TYPE="button" value='Show picture of statistics' onclick="reP()">
</div>
<body>
</html>

