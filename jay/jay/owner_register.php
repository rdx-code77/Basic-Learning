<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="bg">
	<?php include('owner_server.php') ?>
	<div class="header">
		<h2>Owner Register</h2>
	</div>
	
	<form method="post" action="owner_register.php">

		<?php include('errors.php'); ?>
		<div class="input-group">
			<label>Shop ID</label>
			<input type="text" name="sid" value="<?php echo $sid; ?>" required>
		</div>
		<div class="input-group">
			<label>Shop name</label>
			<input type="text" name="sname" value="<?php echo $sname; ?>" required>
		</div>
		<div class="input-group">
			<label>Email</label>
			<input type="email" name="email" value="<?php echo $email; ?>" required>
		</div>
		
		<div class="input-group">
			<label>Manager ID</label>
			<input type="text" name="mid" value="<?php echo $_SESSION['mid']; ?>" readonly>
		</div>
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="password_1">
		</div>
		<div class="input-group">
			<label>Confirm password</label>
			<input type="password" name="password_2">
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="reg_owner">Register</button>
		</div>
		<div class="input-group">
			<button type="submit" class="btn" ><a href="manager.php" style="text-decoration:None;">BACK</a></button>
		</div>
	
	</form>
	</div>
</body>
</html>