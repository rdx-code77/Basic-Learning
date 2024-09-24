<?php 
	session_start();

	// variable declaration
	
	$email    = "";
	$mid  = "";
	$errors = array(); 
	$_SESSION['success'] = "";

	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'registration');

	// REGISTER USER
	if (isset($_POST['reg_user'])) {
		// receive all input values from the form
		$email = mysqli_real_escape_string($db, $_POST['email']);
		$mid = mysqli_real_escape_string($db, $_POST['mid']);
	    
		// form validation: ensure that the form is correctly filled
		if (empty($email)) { array_push($errors, "Email is required"); }
if (empty($mid)) { array_push($errors, "Manger ID  is required"); }


		// register user if there are no errors in the form
		if (count($errors) == 0) {
			//$password = md5($password_1);//encrypt the password before saving in the database
			$query=mysqli_query($db,"SELECT email FROM users WHERE  email='$email'");
			$queri=mysqli_query($db,"SELECT mid FROM users WHERE  mid='$mid'");

		if (mysqli_num_rows($query) == 1 || mysqli_num_rows($queri) == 1) {
		$query = "UPDATE users SET users.email='$email' WHERE users.mid='$mid'";
			mysqli_query($db, $query);	
			header('location: manager_after_edit.php');
		}
	

		else{

			
			
			
			
			
			header('location: manager_after_register.php');
		}

	}
}
if (isset($_POST['back']))
{
				header('location: admin.php');

}
	// ... 

	// LOGIN USER
	

?>