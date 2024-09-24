<!DOCTYPE html>
<html>
<body>
<style>
table, td, th
{
border: 1px solid black;
width: 50%;
text-align: center;
border-collapse:collapse;
background-color:lightblue;
}
table { margin: auto; }
</style>
<?php include('owner_server.php') 
?>
<?php
$midd=$_SESSION['mid'];
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "registration";
$a=[];
$conn = mysqli_connect($servername, $username, $password, $dbname);
if ($conn->connect_error)
die("Connection failed: " . $conn->connect_error);
$sql = "SELECT * FROM owners WHERE mid='$midd'";
// performs a query against the database
$result = $conn->query($sql);
echo "<br>";
echo "<center> Owner LIST </center>";
echo "<table border='2'>";
echo "<tr>";
echo "<th>SHOP ID</th><th>SHOP NAME</th><th>EMAIL ID</th></tr>";
if ($result->num_rows> 0)
{
// output data of each row and fetches a result row as an
//associative array
while($row = $result->fetch_assoc())
{
echo "<tr>";
echo "<td>". $row["sid"]."</td>";
echo "<td>". $row["sname"]."</td>";
echo "<td>". $row["email"]."</td>";
echo "</tr>";

}
}
else
{
echo "<tr><td>Table is Empty</td></tr>";
}
echo "</table>";
?>





