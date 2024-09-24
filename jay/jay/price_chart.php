<!DOCTYPE html>
<html>
<head>
	
	<title>SHOP DETAILS:</title>
		<link rel="shortcut icon" type="image/png" href="image/muscle-magic.png" sizes="128*128">
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
<body>
<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "registration";
$a=[];
$conn = mysqli_connect($servername, $username, $password, $dbname);
if ($conn->connect_error)
die("Connection failed: " . $conn->connect_error);
$sql = "SELECT * FROM crops";
// performs a query against the database
$result = $conn->query($sql);
if ($result->num_rows> 0)
{
// output data of each row and fetches a result row as an
//associative array
?>
<br><br><br>
<div class="container">
<table class="table table-dark table-striped">
<tr>
		<th><h4>Product ID </h4></th>
		<th style="text-align:left;"><h4> Product name </h4></th>
		<th><h4>Price </h4></th>
</tr>
</table>
<table class="table table-dark table-striped">
<?php
while($row = $result->fetch_assoc())
{
?>
<tr>
<td style="color:white";><?php echo $row["cid"]; ?></td>
<td style="text-align:center;color:white;" ><?php echo $row["toc"]; ?></td>
<td style="color:white;text-align:center"><?php echo $row["price"];?></td>
	</tr>

<?php }
	}
	?>
	<tr ><td colspan="3">NOTE:- 0 in price indicates product not in market</td></td></table>
</header>
<div class="input-group">
<button  class="btn"><a href="index.php" style="text-decoration:None;color:white">BACK</a></button>
</div>
</div>
</body>
</html>