<!DOCTYPE html>
<html>
<body>
<style>

</style>
<head>
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
<style>
body{  
  /* The image used */
  background-image: url("image/bck.jpg");

  /* Full height */
  

  /* Center and scale the image nicely */
  background-position: inherit;
  background-repeat: no-repeat;
  background-size: cover;
}

</style>
</head>
<?php include('shopowner_server.php') ?>
<?php
$sidd=$_SESSION['sid'];
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "registration";

$conn = mysqli_connect($servername, $username, $password, $dbname);
if ($conn->connect_error)
die("Connection failed: " . $conn->connect_error);
$sql = "SELECT * FROM fd WHERE sid='$sidd'";
// performs a query against the database
$result = $conn->query($sql);
$tsp=0;
$te=0;
$a=0;
echo "<br>";
?><div class="container"><table class="table table-dark table-striped">
<tr>
		<th><h4>FARMER NAME </h4></th>
		<th style="text-align:center;"><h4> CONTACT NUMBER</h4></th>
		<th><h4>PRODUCT ID </h4></th>
		<th><h4>QUANTITY </h4></th>
		<th><h4>AMOUNT </h4></th>
		<th><h4>DATE </h4></th>
</tr>

<?php 
if ($result->num_rows> 0)
{
// output data of each row and fetches a result row as an
//associative array
while($row = $result->fetch_assoc())
{
echo "<tr>";
echo "<td>". $row["name"]."</td>";
echo "<td>". $row["phno"]."</td>";
echo "<td>". $row["cid"]."</td>";
echo "<td>". $row["qty"]."</td>";
echo "<td>".$row["sold"]."</td>";
echo "<td>".$row["date"]."</td></tr>";
$tsp=$tsp+$row["sold"];
}
echo "<tr ><td colspan='6'>Total spent:".$tsp."</td></tr>";
}
else
{
echo "<tr colspan='6'><td>Table is Empty</td></tr>";
}
echo "</table>";
echo "</div>";
echo "<br><br><br>";
$sqll = "SELECT * FROM bidders WHERE shopid='$sidd'";
// performs a query against the database
$result = $conn->query($sqll);
?><div class="container"><table class="table table-dark table-striped">
<tr>
		<th><h4>BIDDER NAME </h4></th>
		<th style="text-align:center;"><h4> CONTACT NUMBER</h4></th>
		<th><h4>PRODUCT ID </h4></th>
		<th><h4>QUANTITY </h4></th>
		<th><h4>AMOUNT </h4></th>
		<th><h4>DATE </h4></th>
</tr>

<?php 
if ($result->num_rows> 0)
{
// output data of each row and fetches a result row as an
//associative array
while($row = $result->fetch_assoc())
{
echo "<tr>";
echo "<td>". $row["name"]."</td>";
echo "<td>". $row["phno"]."</td>";
echo "<td>". $row["cid"]."</td>";
echo "<td>". $row["qty"]."</td>";
echo "<td>". $row["bcost"]."</td>";
echo "<td>".$row["datee"]."</td></tr>";
$te=$te+$row["bcost"];
}
echo "<tr><td colspan='6'>Total earned:".$te."</td></tr>";
}
else
{
echo "<tr><td>Table is Empty</td></tr>";
}
?></table>
<table class="table table-dark table-striped">
<tr align="center">
<?php 

if ($te-$tsp>0)
{
$a=$te-$tsp;
echo "<td colspan='6'style='background-color:green'>Total profit".$a."</td></tr>";
}
else{
	$a=$tsp-$te;
	echo "<td colspan='6' style='background-color:red'>Total loss".$a."</td></tr>";
	
}
echo "</div>";
echo "</table>";
?>
<div class="input-group">
<button  class="btn"><a href="owner.php" style="text-decoration:None;color:white">BACK</a></button>
</div>
</body>
</html>





