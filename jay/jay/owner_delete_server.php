<?php 
	session_start();

	// variable declaration
	
	
	$sid  = "";
	$errors = array(); 
	$_SESSION['success'] = "";

	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'registration');

	// REGISTER USER
	if (isset($_POST['reg_user'])) {
		// receive all input values from the form
		
		$sid = mysqli_real_escape_string($db, $_POST['sid']);
	    $pswd = mysqli_real_escape_string($db, $_POST['password_1']);
	    
		// form validation: ensure that the form is correctly filled
if (empty($sid)) { array_push($errors, "Shop ID  is required"); }
if (empty($pswd)) { array_push($errors, "Password  is required"); }


		// register user if there are no errors in the form
		if (count($errors) == 0) {
			//$password = md5($password_1);//encrypt the password before saving in the database
			
			$queri=mysqli_query($db,"SELECT * FROM owners WHERE  sid='$sid' AND password='$pswd'");
			
		
		if (mysqli_num_rows($queri) == 1) {
		$query = "DELETE FROM owners WHERE owners.sid='$sid'";
			mysqli_query($db, $query);	
			header('location: owner_after_delete.php');
		}
		else
		{
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