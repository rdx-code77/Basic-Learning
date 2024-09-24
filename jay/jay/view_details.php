<!DOCTYPE html>
<html>
<head>
	<style>


	</style>
	<title>CURRENT PRODUCT:</title>
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
$conn = mysqli_connect($servername, $username, $password, $dbname);
if ($conn->connect_error)
die("Connection failed: " . $conn->connect_error);
$sql = "SELECT * FROM logs";
// performs a query against the database
$result = $conn->query($sql);
if ($result->num_rows> 0)
{
// output data of each row and fetches a result row as an
//associative array
?>
<div class="container">
<table class="table table-dark table-striped">
<tr>
<th>SNo</th><th>Email</th><th>Action</th><th>Date-Time</th></tr>
</tr>
<?php
while($row = $result->fetch_assoc())
{
?>
<tr>
<td ><?php echo $row["SNo"]; ?></td>
<td style="text-align:left;" ><?php echo $row["email"]; ?></td>
<td ><?php echo $row["action"];?></td>
<td ><?php echo $row["date_time"];?></td>
</tr>

<?php
 }
}
	
	?></table>
<div class="input-group">
<button  class="btn"><a href="admin.php" style="text-decoration:None;color:white">BACK</a></button>
</div>
</body>
</html>






