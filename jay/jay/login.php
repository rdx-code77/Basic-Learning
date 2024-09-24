<?php include('server.php') ?>
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
<style>
body{
	background-image:url("image/agri1.jpg");
	 background-position: inherit;
  background-repeat: no-repeat;
  background-size: cover;
}
.header
{
	width: 30%;
	margin: 50px auto 0px;
	color: white;
	background: none;
	text-align: center;
	border: 1px solid #B0C4DE;
	border-bottom: none;
	border-radius: 10px 10px 0px 0px;
	padding: 20px;
	
}
form, .content {
	
	width: 30%;
	margin: 0px auto;
	padding: 20px;
	border: 1px solid #B0C4DE;
	background: none;
	border-radius: 0px 0px 10px 10px;
}
.cnt{
	top:0;
}
</style>
</head>
<body>
<div class="cnt">
	<div class="header">
		<h2>Login</h2>
	</div>
	
	<form method="post" action="login.php">

		<?php include('errors.php'); ?>

		<div class="input-group">
			<label>Username</label>
			<input type="text" name="username" >
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
	
</div>

</body>
</html>