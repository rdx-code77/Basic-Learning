<?php 
	session_start();

	// variable declaration
	$username = "";
	$password = "";
	$email = "";
	$branch = "";
	$m ="";
	$errors = array(); 
	$_SESSION['success'] = "";

	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'registration');
		// REGISTER USER
	
	// LOGIN USER
	if (isset($_POST['login_user'])) {
		$id = mysqli_real_escape_string($db, $_POST['id']);
		$password = mysqli_real_escape_string($db, $_POST['password']);

		if (empty($id)) {
			array_push($errors, "Shop ID is required");
		}
		if (empty($password)) {
			array_push($errors, "Password is required");
		}

		if (count($errors) == 0) {
			//$password = md5($password);
			$query = "SELECT * FROM owners WHERE sid='$id' AND password='$password'";
			$results = mysqli_query($db, $query);

			if (mysqli_num_rows($results) == 1) {
				$_SESSION['username'] = $username;
				$_SESSION['success'] = "You are now logged in";
				
			$result = $db->query($query);
			if ($result->num_rows> 0)
			{
				while($row = $result->fetch_assoc())
				{
					$sid= $row["sid"];
					$sname = $row["sname"];
					$_SESSION['sid']=$sid;
					$_SESSION['sname']=$sname;
					
				}
			}
				header('location: owner.php');
			}else {
				array_push($errors, "Wrong username/password combination");
			}
			
				
				
		}
	}
	

?>