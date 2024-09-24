<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="bg">
	
	<?php 
	

	// variable declaration
	
	$phn1    = "";
	$phn2  = "";
	$errors = array(); 


	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'registration');

	// REGISTER USER
	if (isset($_POST['update'])) {
		// receive all input values from the form
		$phn1 = mysqli_real_escape_string($db, $_POST['phn1']);
		$phn2 = mysqli_real_escape_string($db, $_POST['phn2']);
	    
		// form validation: ensure that the form is correctly filled
		if (empty($phn1)) { array_push($errors, "Old number is required"); }
if (empty($phn2)) { array_push($errors, "new Number is required"); }

if($phn1==$phn2)
{array_push($errors, "both are same"); }
	
		// register user if there are no errors in the form
		if (count($errors) == 0) {
			//$password = md5($password_1);//encrypt the password before saving in the database
			$query=mysqli_query($db,"SELECT phno FROM fd WHERE  phno='$phn1'");
			
		if (mysqli_num_rows($query) == 1) {
		$query = "UPDATE fd SET fd.phno='$phn2' WHERE fd.phno='$phn1'";
			mysqli_query($db, $query);	
			header('location: farmer_succ_reg.php');
		}
	

		else{			
			
			header('location: fail_fd.php');
		}

	}
}
if (isset($_POST['back']))
{
				header('location:owner.php');

}
	// ... 

	
	

?>
	
	
	
	
	<div class="header">
		<h2>Farmer Update</h2>
	</div>
	
	<form method="post" action="farmer_edit.php">

		<?php include('errors.php'); ?>
		<div class="input-group">
			<label>Old contact number</label>
			<input type="number" name="phn1" value="<?php echo $phn1; ?>">
		</div>
		<div class="input-group">
			<label>New contact number</label>
			<input type="number" name="phn2" value="<?php echo $phn2; ?>">
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="update">UPDATE-CONTACT</button>
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="back">BACK</button>
		</div>
	
	</form>
	</div>
</body>
</html>