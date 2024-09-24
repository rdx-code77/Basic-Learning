<?php 
	session_start();

	// variable declaration
	
	$email    = "";
	$sid  = "";
	$errors = array(); 
	$_SESSION['success'] = "";

	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'registration');

	// REGISTER USER
	if (isset($_POST['reg_user'])) {
		// receive all input values from the form
		$email = mysqli_real_escape_string($db, $_POST['email']);
		$sid = mysqli_real_escape_string($db, $_POST['sid']);
	    
		// form validation: ensure that the form is correctly filled
		if (empty($email)) { array_push($errors, "Email is required"); }
if (empty($sid)) { array_push($errors, "Shop ID  is required"); }


		// register user if there are no errors in the form
		if (count($errors) == 0) {
			//$password = md5($password_1);//encrypt the password before saving in the database
			$query=mysqli_query($db,"SELECT email FROM owners WHERE  email='$email'");
			$queri=mysqli_query($db,"SELECT sid FROM owners WHERE  sid='$sid'");

		if (mysqli_num_rows($query) == 1 || mysqli_num_rows($queri) == 1) {
		$query = "UPDATE owners SET owners.email='$email' WHERE owners.sid='$sid'";
			mysqli_query($db, $query);	
			header('location: owner_after_edit.php');
		}
	

		else{			
			
			header('location: fail.php');
		}

	}
}
if (isset($_POST['back']))
{
				header('location: manager.php');

}
	// ... 

	// LOGIN USER
	

?>