<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="bg">
	<?php include('manager_server.php') ?>
	<div class="header">
		<h2>Manager Register</h2>
	</div>
	​<picture>
  <source srcset="..." type="image/svg+xml">
  <img src="agri1.jpg" class="bg" alt="manager">
</picture>
	
	<form method="post" action="manager_register.php">

		<?php include('errors.php'); ?>
		<div class="input-group">
			<label>Manager ID</label>
			<input type="text" name="mid" value="<?php echo $m; ?>">
		</div>
		<div class="input-group">
			<label>Username</label>
			<input type="text" name="username" value="<?php echo $username; ?>">
		</div>
		<div class="input-group">
			<label>Email</label>
			<input type="email" name="email" value="<?php echo $email; ?>">
		</div>
		<div class="input-group">
			<label>Branch</label>
			<input type="text" name="branch" value="<?php echo $branch; ?>">
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
			<button type="submit" class="btn" name="reg_user">Register</button>
		</div>
		<div class="input-group">
			<button type="submit" class="btn" ><a href="admin.php" style="text-decoration:None;">BACK</a></button>
		</div>
	
	</form>
	</div>
</body>
</html>