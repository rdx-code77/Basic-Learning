<?php include('manager_server.php') ?>
<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	<script type="text/javascript" >
   function preventBack(){window.history.forward();
   window.history.backward();}
    setTimeout("preventBack()", 0);
    window.onunload=function(){null};
</script>
</head>
<body>

	<div class="header">
		<h2>Login</h2>
	</div>
	
	<form method="post" action="manager_login.php">

		<?php include('errors.php'); ?>

		<div class="input-group">
			<label>Email</label>
			<input type="email" name="username" >
		</div>
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="password">
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="login_user">Login</button>
		</div>
		<div class="input-group">
			<button  class="btn"><a href="index.php" style="text-decoration:None;">BACK</a></button>
		</div>
	</form>


</body>
</html>