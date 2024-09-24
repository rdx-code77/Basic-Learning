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
	if (isset($_POST['reg_user'])) {
		// receive all input values from the form
		$username = mysqli_real_escape_string($db, $_POST['username']);
		$email = mysqli_real_escape_string($db, $_POST['email']);
	    $branch = mysqli_real_escape_string($db, $_POST['branch']);
		$m = mysqli_real_escape_string($db, $_POST['mid']);
		$password_1 = mysqli_real_escape_string($db, $_POST['password_1']);
		$password_2 = mysqli_real_escape_string($db, $_POST['password_2']);

		// form validation: ensure that the form is correctly filled
		if (empty($username)) { array_push($errors, "Username is required"); }
		if (empty($email)) { array_push($errors, "Email is required"); }
	    if (empty($branch)) { array_push($errors, "branch name is required"); }
if (empty($m)) { array_push($errors, "manager id is required"); }

		if (empty($password_1)) { array_push($errors, "Password is required"); }

		if ($password_1 != $password_2) {
			array_push($errors, "The two passwords do not match");
		}

		// register user if there are no errors in the form
		if (count($errors) == 0) {
			//$password = md5($password_1);//encrypt the password before saving in the database
			$query=mysqli_query($db,"SELECT * FROM users WHERE  email='$email'");
			$queri=mysqli_query($db,"SELECT * FROM users WHERE  username='$username'");

		if (mysqli_num_rows($query) > 0 || mysqli_num_rows($queri) > 0) {
			echo "email is already exist!!!";
			echo "OR   username is already exist!!! ";

		}
	

		else{

			$query = "INSERT INTO users (mid,username, email, password,branch) 
					  VALUES('$m','$username', '$email', '$password_1','$branch')";
			mysqli_query($db, $query);

			
			header('location: manager_after_register.php');
		}

	}
}
	

	// ... 

	// LOGIN USER
	if (isset($_POST['login_user'])) {
		$username = mysqli_real_escape_string($db, $_POST['username']);
		$password = mysqli_real_escape_string($db, $_POST['password']);

		if (empty($username)) {
			array_push($errors, "Username is required");
		}
		if (empty($password)) {
			array_push($errors, "Password is required");
		}

		if (count($errors) == 0) {
			//$password = md5($password);
			$query = "SELECT * FROM users WHERE email='$username' AND password='$password'";
			$results = mysqli_query($db, $query);

			if (mysqli_num_rows($results) == 1) {
				$_SESSION['username'] = $username;
				$_SESSION['success'] = "You are now logged in";
				
			$result = $db->query($query);
			if ($result->num_rows> 0)
			{
				while($row = $result->fetch_assoc())
				{
					$mid= $row["mid"];
					$usr=$row["username"];
					$_SESSION['br']=$usr;
					$_SESSION['mid']=$mid;
					
				}
			}
				header('location: manager.php');
			}else {
				array_push($errors, "Wrong username/password combination");
			}
			
				
				
		}
	}
	

?>