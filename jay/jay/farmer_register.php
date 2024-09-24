<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="bg">
	<?php include('farmer_server.php') ?>
	<?php include('shopowner_server.php') ?>
	<div class="header">
		<h2>Farmer Register</h2>
	</div>
	
	<form method="post" action="farmer_register.php">

		<?php include('errors.php'); ?>
		
		<div class="input-group">
			<label>Farmer name</label>
			<input type="text" name="fname" value="<?php echo $fname; ?>" required>
		</div>
		<div class="input-group">
			<label>Contact Number</label>
			<input type="text" name="phn" value="<?php echo $phn; ?>" required>
		</div>
		<div class="input-group">
			<label>Product ID</label>
			<input type="text" name="pid" value="<?php echo $pid; ?>" required>
		</div>
		<div class="input-group">
			<label>Quantity (in Kg)</label>
			<input type="number" name="qty" value="<?php echo $qty; ?>" required>
		</div>
		<div class="input-group">
			<label>Shop ID</label>
			<input type="text" name="sid" value="<?php echo $_SESSION['sid']; ?>" readonly>
		</div>
		<div class="input-group">
			<label>DATE</label>
			<input type="date" name="date" value="<?php echo $date; ?>" required>
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="reg_farmer">Register</button>
		</div>
		<div class="input-group">
			<button type="submit" class="btn" ><a href="owner.php" style="text-decoration:None;">BACK</a></button>
		</div>
	
	</form>
	</div>
</body>
</html>