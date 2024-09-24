<?php 
	session_start(); 

	if (!isset($_SESSION['username'])) {
		$_SESSION['msg'] = "You must log in first";
		header('location: login.php');
	}

	if (isset($_GET['logout'])) {
		session_destroy();
		unset($_SESSION['username']);
		header("location: login.php");
	}

?>
<!DOCTYPE html>
<html>
<head>
<title>ADMIN</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<script type="text/javascript" >
   function preventBack(){window.history.forward();
   window.history.backward();}
    setTimeout("preventBack()", 0);
    window.onunload=function(){null};
</script>
</head>
<body>
<?php  if (isset($_SESSION['username'])) : ?>
<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-blue w3-wide w3-padding w3-card">
    <a href="#home" class="w3-bar-item w3-button"><b>ADMIN</b> </a>
    <!-- Float links to the right. Hide them on small screens -->
    <div class="w3-right w3-hide-small">
      <a href="manager_register.php" class="w3-bar-item w3-button">INSERT</a>
      <a href="manager_edit.php" class="w3-bar-item w3-button">EDIT</a>
      <a href="manager_delete.php" class="w3-bar-item w3-button">DELETE</a>
       <a href="view_details.php" class="w3-bar-item w3-button">LOGS</a>
        <a href="chart.php" class="w3-bar-item w3-button">PRICE CHART</a>
         <a href="login.php" class="w3-bar-item w3-button">LOGOUT</a>
    </div>
  </div>
</div>

<!-- Header -->
<header class="w3-display-container w3-content w3-wide" style="max-width:1500px;" id="home">
  <img class="w3-image" src="image/agri1.jpg" alt="Architecture" width="1500" height="800">
  <div class="w3-display-middle w3-margin-top w3-center">
    <h1 class="w3-xxlarge w3-text-white"><span class="w3-padding w3-black w3-opacity-min"><b>Admin</b></span> <span class="w3-hide-small w3-text-light-grey"><?php echo $_SESSION['username'] ?></span></h1>
  </div>
</header>

<!-- Page content -->
<div class="w3-content w3-padding" style="max-width:1564px">

  <!-- Project Section -->
  <div class="w3-container w3-padding-32" id="projects">
    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">OUR LOCATIONS</h3>
  </div>

  <div class="w3-row-padding">
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-display-container">
        <div class="w3-display-topleft w3-black w3-padding">KERALA</div>
        <img src="image/kerala.jpg" alt="House" style="width:100%;height:268px;">
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-display-container">
        <div class="w3-display-topleft w3-black w3-padding">MYSORE</div>
        <img src="image/mysore.jpg" alt="House" style="width:100%;height:268px;">
      </div>
    </div>
	
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-display-container">
        <div class="w3-display-topleft w3-black w3-padding">MUMBAI</div>
        <img src="image/mumbai.jpg" alt="House" style="width:100%;height:268px;">
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-display-container">
        <div class="w3-display-topleft w3-black w3-padding">HAMPI</div>
        <img src="image/hampi.jpg" alt="House" style="width:100%;height:268px;">
      </div>
    </div>
  </div>

  <div class="w3-row-padding">
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-display-container">
        <div class="w3-display-topleft w3-black w3-padding">CHENNAI</div>
        <img src="image/chennai.jpg" alt="House" style="width:100%;height:268px;">
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-display-container">
        <div class="w3-display-topleft w3-black w3-padding">HYDERABAD</div>
        <img src="image/hyd.jpg" alt="House" style="width:100%;height:268px;">
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-display-container">
        <div class="w3-display-topleft w3-black w3-padding">HARYANA</div>
        <img src="image/haryana.jpg" alt="House" style="width:100%;height:268px;">
      </div>
    </div>
    <div class="w3-col l3 m6 w3-margin-bottom">
      <div class="w3-display-container">
        <div class="w3-display-topleft w3-black w3-padding">PUNJAB</div>
        <img src="image/punjab.jpg" alt="House" style="width:100%;height:268px;">
      </div>
    </div>
  </div>


  
  
<!-- Image of location/map -->


<!-- End page content -->
</div>


<!-- Footer -->

<?php endif ?>
</body>
</html>