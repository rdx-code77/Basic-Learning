
<!DOCTYPE html>
<html>
<title>PRODUCT</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

<body class="w3-content" style="max-width:1300px">

<!-- First Grid: Logo & About -->
<div class="w3-row">
  <div class="w3-half w3-black w3-container w3-center" style="height:700px">
    <div class="w3-padding-64">
      <h1>PRODUCT</h1>
    </div>
    <div class="w3-padding-64">
      <a href="crop_insert.php" class="w3-button w3-black w3-block w3-hover-blue-grey w3-padding-16">INSERT</a>
      <a href="crop_edit.php" class="w3-button w3-black w3-block w3-hover-teal w3-padding-16">EDIT</a>
      <a href="admin.php" class="w3-button w3-black w3-block w3-hover-dark-grey w3-padding-16">BACK</a>

 </div>
  </div>
  <div class="w3-half w3-blue-grey w3-container" style="height:700px">
    <div class="w3-padding-64 w3-center">
      <h1>PRODUCT LIST</h1>
      <div class="w3-left-align w3-padding-xxxlarge">
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
	?>
	<div class="container">
<table class="table table-dark table-striped" border="2" align="center" width="80%">
<tr>
<th>PRODUCT ID</th><th>PRODUCT NAME</th><th>PRICE</th></tr>
</tr>
	<?php
while($row = $result->fetch_assoc())
{
?>
<tr>
<td ><?php echo $row["cid"]; ?></td>
<td><?php echo $row["toc"]; ?></td>
<td ><?php echo $row["price"];?></td>
</tr>

<?php
 }
}
	
	?>
	</table>
	  
	  
        </div>
    </div>
  </div>
</div>

<!-- Footer -->


</body>
</html>
