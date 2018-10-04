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
Assignment 2

<br>
<a href="https://github.com/timqqt/CBB520_-Finding-SNPS-and-INDELS-">Click here to see all the program in my Github.</a>
<br>
<form method="post" action="/SRA_DB/function.php">
<input type="submit" id="btn1" value="Run the program" onClick="bt_click();">
</form>

<div id = "txt1">
We try our best to do the processing.<br>
</div>
<img class="img1" src="http://5b0988e595225.cdn.sohucs.com/images/20171120/407c128e637643bc953c97f1bcc562ef.gif" style="height:500px; width: 500px">  

<br>
Copy from http://5b0988e595225.cdn.sohucs.com/images/20171120/407c128e637643bc953c97f1bcc562ef.gif

</div>

<body>
</html>

<script>
var txt1 = document.getElementById("txt1");
txt1.style.display= "none";

function bt_click(){
alert('Please wait....'); 
var btn1 = document.getElementById("btn1");
btn1.disabled=true;

var txt1 = document.getElementById("txt1");
txt1.style.display= "inline";
}
</script>
