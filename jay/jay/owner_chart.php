<!DOCTYPE html>
<html>
<head>
	<style>
		*{
			padding: 0;
			margin: 0;
			justify-content: center;
			align-items: center;

		}
		body{
			max-width: 80%;
			margin: auto;
		}
		#a td{
			background-color: black;

		}
		#a h1:hover{
			transition: 1.5%;
			color: #FFA500;
		}
		#b h4{
		 text-align: center;
		}
		#b h4:hover{
			transform: scale(1.3);
			color: #000000;
		}
		#b1{
		background-image: url(image/td.jpg);	 
		}
		#b
	{
		border-radius: 6px 6px 6px 6px;
		
		border-spacing: 0;
		
	}

	#b tr:first-child td:first-child 
	{
		border-top-left-radius: 10px;
	}
	
	#b tr:first-child td:last-child 
	{
		border-top-right-radius: 10px;
	}
		#c{
			background-image: url(image/td.jpg);
		}
		a{
			text-decoration: none
			color:black;
		}
		

}
.input-group {
	margin: 10px 0px 10px 0px;
}

.input-group label {
	display: block;
	text-align: left;
	margin: 3px;
}
.input-group input {
	height: 30px;
	width: 93%;
	padding: 5px 10px;
	font-size: 16px;
	border-radius: 5px;
	border: 1px solid gray;
}
.btn {
	padding: 10px;
	font-size: 15px;
	color: white;
	background: #5F9EA0;
	border: none;
	border-radius: 5px;
}


	</style>
	<title>CURRENT PRODUCT:</title>
		<link rel="shortcut icon" type="image/png" href="image/muscle-magic.png" sizes="128*128">

</head>
<body>
<table border="2" width="100%" cellpadding="0" cellspacing="0">
	<tr height="70px" align="center" id="a">
		<td ><font size="5" face="cursive" color="white"><h1>:PRODUCT LIST:</h1> </font></td>
	</tr>
</table>
<br>
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
<table border="0" width="100%" cellpadding="0" cellspacing="0" id="b" >
<tr height="50px" align="center" bgcolor="#32CD32">
		<td><font size="5" face="cursive" color="white"><h4><u>PRD ID </u></h4></font></td>
		<td><font size="5" face="cursive" color="white"><h4><u>PRD. NAME </u></h4></font></td>
		<td><font size="5" face="cursive" color="white"><h4><u>PRICE </u></h4></font></td>
	</tr>
</table>
<?php
while($row = $result->fetch_assoc())
{
?>
<table border="0" width="100%" cellpadding="0" cellspacing="0" id="b1">
<tr height="45px"  align="center">
<td width="33.3%"><font size="3" face="sans-serif" color="white"><?php echo $row["cid"]; ?></td>
<td width="33.3%"><font size="3" face="sans-serif" color="white"><?php echo $row["toc"]; ?></td>
<td width="33.3%"><font size="3" face="sans-serif" color="white"><?php echo $row["price"];?>
</td>
	</tr>
	</font>
</td>
</font>
</td>
</font></td></tr>
<?php }
	}
	?></table>
</header>
<div class="input-group">
<button  class="btn"><a href="owner.php" style="text-decoration:None;">BACK</a></button>
</div>
</body>
</html>