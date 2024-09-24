<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="bg">
	<?php include('manager_delete_server.php') ?>
	<div class="header">
		<h2>Manager DELETE</h2>
	</div>
	
	<form method="post" action="manager_delete.php">

		<?php include('errors.php'); ?>
		<div class="input-group">
			<label>Manager ID</label>
			<input type="text" name="mid" value="<?php echo $mid; ?>">
		</div>
		<div class="input-group">
			<label>Email</label>
			<input type="email" name="email" value="<?php echo $email; ?>">
		</div>
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="password_1">
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="reg_user">DELETE</button>
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="back">BACK</button>
		</div>
	
	</form>
	</div>
</body>
</html>
