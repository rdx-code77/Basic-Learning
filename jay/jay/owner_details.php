<!DOCTYPE html>
<html>
<head>
	
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
	<title>CURRENT PRODUCT:</title>
		<link rel="shortcut icon" type="image/png" href="image/muscle-magic.png" sizes="128*128">
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

</head>
<body>
<?php include('manager_server.php')?>
<?php
$mid= $_SESSION['mid'];
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "registration";
$conn = mysqli_connect($servername, $username, $password, $dbname);
if ($conn->connect_error)
die("Connection failed: " . $conn->connect_error);
$sql = "SELECT * FROM owners WHERE mid='$mid'";
// performs a query against the database
$result = $conn->query($sql);
if ($result->num_rows> 0)
{
// output data of each row and fetches a result row as an
//associative array
?>
<div class="container">
<br><br><br>
<table class="table table-dark table-striped">
<tr>
<th>SHOP ID</th><th>SHOP NAME</th><th>EMAIL ID</th></tr>
</tr>
<?php
while($row = $result->fetch_assoc())
{
?>
<tr>
<td ><?php echo $row["sid"]; ?></td>
<td style="text-align:left;" ><?php echo $row["sname"]; ?></td>
<td ><?php echo $row["email"];?></td>

</tr>

<?php
 }
}
	
	?></table>
<div class="input-group">
<button  class="btn"><a href="manager.php" style="text-decoration:None;color:white">BACK</a></button>
</div>
</body>
</html>






