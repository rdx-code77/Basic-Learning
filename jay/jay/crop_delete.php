<?php include('crop_server.php') ?>
<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>

	<div class="header">
		<h2>DELETE PRODUCT</h2>
	</div>
	
	<form method="post" action="crop_delete.php">

		<?php include('errors.php'); ?>

		<div class="input-group">
			<label>PRODUCT ID</label>
			<input type="text" name="pid" required>
		</div>
		
		<div class="input-group">
			<button type="submit" class="btn" name="delete_prd">DELETE</button>
		</div>
		<div class="input-group">
			<button  class="btn"><a href="chart.php" style="text-decoration:None;">BACK</a></button>
		</div>
	</form>


</body>
</html>