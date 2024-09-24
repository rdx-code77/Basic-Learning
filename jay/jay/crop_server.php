<?php 
	session_start();

	// variable declaration
	$pid = "";
	$pname = "";
	$price ;
	$errors = array(); 
	$_SESSION['success'] = "";

	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'registration');

	

	// ... 

	// LOGIN USER
	if (isset($_POST['login_user'])) {
		$pid = mysqli_real_escape_string($db, $_POST['pid']);
		$pname = mysqli_real_escape_string($db, $_POST['pname']);
		$price = mysqli_real_escape_string($db, $_POST['price']);

		if (empty($pid)) {
			array_push($errors, "Product id is required");
		}
		if (empty($pname)) {
			array_push($errors, "Product name is required");
		}
	if (empty($price)) {
			array_push($errors, "Product price is required");
		}

		if (count($errors) == 0) 
		{
			//$password = md5($password);
			$query = "INSERT INTO crops (cid,toc,price) 
					  VALUES('$pid','$pname','$price')";
			mysqli_query($db, $query);
				header('location: crop_update.php');
			}else {
				header('location: crop_fail.php');
			}
		}
	if (isset($_POST['update_crop'])) {
		$pid = mysqli_real_escape_string($db, $_POST['pid']);
		$pname = mysqli_real_escape_string($db, $_POST['pname']);
		$price = mysqli_real_escape_string($db, $_POST['price']);

		if (empty($pid)) {
			array_push($errors, "Product id is required");
		}
		if (empty($pname)) {
			array_push($errors, "Product name is required");
		}
	if (empty($price)) {
			array_push($errors, "Product price is required");
		}

		if (count($errors) == 0) 
		{
			//$password = md5($password);
			$query = "UPDATE crops SET crops.price='$price' WHERE crops.cid='$pid'";
			mysqli_query($db, $query);
			header('location: crop_update.php');
			}else {
				header('location: crop_fail.php');
			}
		}
	if (isset($_POST['delete_prd'])) {
		$pid = mysqli_real_escape_string($db, $_POST['pid']);
		
		if (empty($pid)) {
			array_push($errors, "Product id is required");
		}
		
		if (count($errors) == 0) 
		{
			//$password = md5($password);
			$query = "DELETE FROM crops WHERE cid='$pid'";
			mysqli_query($db, $query);
			header('location: crop_update.php');
			}else {
				header('location: crop_fail.php');
			}
		}
	
	

?>