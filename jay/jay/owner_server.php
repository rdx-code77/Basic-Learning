<?php 
	session_start();

	// variable declaration
	$sname = "";
	$password = "";
	$email = "";
	$mid ="";
	$sid = "";
	$errors = array(); 
	$_SESSION['success'] = "";

	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'registration');
		// REGISTER USER
	if (isset($_POST['reg_owner'])) {
		// receive all input values from the form
		$sid = mysqli_real_escape_string($db, $_POST['sid']);
		$sname = mysqli_real_escape_string($db, $_POST['sname']);
		$email = mysqli_real_escape_string($db, $_POST['email']); 
		$mid = mysqli_real_escape_string($db, $_POST['mid']);
		$password_1 = mysqli_real_escape_string($db, $_POST['password_1']);
		$password_2 = mysqli_real_escape_string($db, $_POST['password_2']);

		// form validation: ensure that the form is correctly filled
		if (empty($sname)) { array_push($errors, "Shop name is required"); }
		if (empty($email)) { array_push($errors, "Email is required"); }
	    
		if (empty($mid)) { array_push($errors, "manager id is required"); }
		if (empty($sid)) { array_push($errors, "shop id is required"); }

		if (empty($password_1)) { array_push($errors, "Password is required"); }

		if ($password_1 != $password_2) {
			array_push($errors, "The two passwords do not match");
		}

		// register user if there are no errors in the form
		if (count($errors) == 0) {
			//$password = md5($password_1);//encrypt the password before saving in the database
			$query=mysqli_query($db,"SELECT email FROM owners WHERE  email='$email'");
			$queri=mysqli_query($db,"SELECT sid FROM owners WHERE  sid='$sid'");

		if (mysqli_num_rows($query) > 0 )  {
			echo "email is already exist!!!";
		}
		else if (mysqli_num_rows($queri) > 0){
			echo "username is already exist!!! ";

		}
	

		else{

			$query = "INSERT INTO owners (sid,sname,email, password,mid) 
					  VALUES('$sid','$sname', '$email', '$password_1','$mid')";
			mysqli_query($db, $query);
			header('location: owner_after_register.php');
		}

	}
}
	

	// ... 

	

?>