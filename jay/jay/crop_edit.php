<?php include('crop_server.php') ?>
<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

	<div class="header">
		<h2>UPDATE PRODUCT</h2>
	</div>
	
	<form method="post" action="crop_insert.php">

		<?php include('errors.php'); ?>

		<div class="input-group">
			<label>PRODUCT ID</label>
			<input type="text" name="pid" required>
		</div>
		<div class="input-group">
			<label>PRODUCT NAME</label>
			<input type="text" name="pname" required>
		</div>
		<div class="input-group">
			<label>PRODUCT PRICE per Kg</label>
			<input type="number" name="price" required>
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="update_crop">UPDATE PRICE</button>
		</div>
		<div class="input-group">
			<button  class="btn"><a href="chart.php" style="text-decoration:None;">BACK</a></button>
		</div>
	</form>


</body>
</html>