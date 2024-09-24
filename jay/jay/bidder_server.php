<?php 
	

	// variable declaration
	$fname = "";
	$phn = "";
	$qty = "";
	$tcost="";
	$pid ="";
	$sid = "";
	$date="";
	$price ="";
	
	$errors = array(); 
	//$_SESSION['success'] = "";

	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'registration');
		// REGISTER USER
	if (isset($_POST['reg_bidder'])) {
		// receive all input values from the form
		$sid = mysqli_real_escape_string($db, $_POST['sid']);
		$fname = mysqli_real_escape_string($db, $_POST['fname']);
		$phn = mysqli_real_escape_string($db, $_POST['phn']); 
		$pid = mysqli_real_escape_string($db, $_POST['pid']);
		$qty = mysqli_real_escape_string($db, $_POST['qty']);
		//$amt = mysqli_real_escape_string($db, $_POST['amt']);
		$date = mysqli_real_escape_string($db, $_POST['date']);
		$tcost=mysqli_real_escape_string($db, $_POST['tcost']);

		// form validation: ensure that the form is correctly filled
		if (empty($fname)) { array_push($errors, "Bidder name is required"); }
		if (empty($sid)) { array_push($errors, "Shop ID is required"); }
	    
		if (empty($pid)) { array_push($errors, "Product id is required"); }
		if (empty($date)) { array_push($errors, "Date is required"); }

		if (empty($phn)) { array_push($errors, "Phone Number is required"); }
		if ($qty==0) { array_push($errors, "Quantity???????????"); }
		if (empty($tcost)) { array_push($errors, "enter bidding cost per Kg"); }

		

		// register user if there are no errors in the form
		if (count($errors) == 0) 
		{
			$amt="";
			//$password = md5($password_1);//encrypt the password before saving in the database
			$query=mysqli_query($db,"SELECT phno FROM bidders WHERE  phno='$phn'");
			$quere=mysqli_query($db,"SELECT cid FROM crops WHERE  cid='$pid'");
			//$result = $db->query($quere);
		if (mysqli_num_rows($query) > 0 )  {
			echo "Phone number  already exist!!!";
		}
		 if(mysqli_num_rows($quere) != 1 )  {
			echo "You dont have the product";
		}
		
		
		else{
			
			$amt = $tcost*$qty;
			$query = "INSERT INTO bidders (name,shopid,bcost,datee,cid,qty,phno) 
					  VALUES('$fname','$sid','$amt','$date','$pid','$qty','$phn')";
			mysqli_query($db, $query);
			header('location: farmer_succ_reg.php');
		}

	}
}
	

	// ... 

	

?>