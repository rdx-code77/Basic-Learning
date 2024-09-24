<?php 
	session_start(); 

	if (!isset($_SESSION['username'])) {
		$_SESSION['msg'] = "You must log in first";
		header('location: manager_login.php');
	}

	if (isset($_GET['logout'])) {
		session_destroy();
		unset($_SESSION['username']);
		header("location: manager_login.php");
	}

?>
<!DOCTYPE html>
<html>
<head>
<title>MANAGER</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script type="text/javascript" >
   function preventBack(){window.history.forward();
   window.history.backward();}
    setTimeout("preventBack()", 0);
    window.onunload=function(){null};
</script>
<style>
body, h1,h2,h3,h4,h5,h6 {font-family: "Montserrat", sans-serif}
.w3-row-padding img {margin-bottom: 12px}
/* Set the width of the sidebar to 120px */
.w3-sidebar {width: 120px;background: #222;}
/* Add a left margin to the "page content" that matches the width of the sidebar (120px) */
#main {margin-left: 120px}
/* Remove margins from "page content" on small screens */
@media only screen and (max-width: 600px) {#main {margin-left: 0}}

.mySlides {
	
	display:none;}
.glow {
  font-size: 80px;
  color: #FFF;
  text-transform: uppercase;
  text-align: center;
  -webkit-animation: glow 1s ease-in-out infinite alternate;
  -moz-animation: glow 1s ease-in-out infinite alternate;
  animation: glow 1s ease-in-out infinite alternate;
}

@-webkit-keyframes glow {
 from {
    text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00, 0 0 40px #00ff00, 0 0 50px #00ff00, 0 0 60px #00ff00, 0 0 70px #00ff00;
  }
  
  to {
    text-shadow: 0 0 20px #fff, 0 0 30px #ff4da6, 0 0 40px #ff4da6, 0 0 50px #ff4da6, 0 0 60px #ff4da6, 0 0 70px #ff4da6, 0 0 80px #ff4da6;
  }
  .card {
  box-shadow: 0 20px 20px 0 rgba(0, 0, 0, 1);
  max-width: 200px;
  margin-left: auto;
  margin-right: auto;
  
  font-family: arial;
  background-color: grey;
}
.imgage{
	border-radius: 50%;
	
}
.imgage:hover {
  animation: shake 0.5s;
  animation-iteration-count: infinite;
}
.title {
  color: black;
  font-size: 18px;
}
@keyframes shake {
  0% { transform: translate(1px, 1px) rotate(0deg); }
  10% { transform: translate(-1px, -2px) rotate(-1deg); }
  20% { transform: translate(-3px, 0px) rotate(1deg); }
  30% { transform: translate(3px, 2px) rotate(0deg); }
  40% { transform: translate(1px, -1px) rotate(1deg); }
  50% { transform: translate(-1px, 2px) rotate(-1deg); }
  60% { transform: translate(-3px, 1px) rotate(0deg); }
  70% { transform: translate(3px, 1px) rotate(-1deg); }
  80% { transform: translate(-1px, -1px) rotate(1deg); }
  90% { transform: translate(1px, 2px) rotate(0deg); }
  100% { transform: translate(1px, -2px) rotate(-1deg); }
}

</style>
</head>

<body class="w3-black">
<?php  if (isset($_SESSION['mid'])) : ?>
<?php 
$mid=$_SESSION['mid'];
$name=$_SESSION['br'];?>
<!-- Icon Bar (Sidebar - hidden on small screens) -->
<nav class="w3-sidebar w3-bar-block w3-small w3-hide-small w3-center">
  <!-- Avatar image in top left corner -->
  <img src="image/agri3.jpg" style="width:100%">
  
	<a href="owner_register.php" class="w3-bar-item w3-button w3-padding-large w3-hover-black">
	<i class="fa fa-user w3-xlarge"></i>
<p>INSERT OWNER	</p>
</a>
	<a href="owner_edit.php" class="w3-bar-item w3-button w3-padding-large w3-hover-black">
	<i class="fa fa-eye w3-xlarge"></i>
    <p>EDIT OWNER</p>
	
</a>
<a href="owner_delete.php" class="w3-bar-item w3-button w3-padding-large w3-hover-black">
	<i class="fa fa-trash w3-xlarge"></i>
    <p>DELETE OWNER</p>
	
</a>
     <a href="owner_details.php" class="w3-bar-item w3-button w3-padding-large w3-hover-black">
    <i class="fa fa-search w3-xxlarge"></i>
    <p>VIEW DETAILS</p>
  </a>
  
</a>
  <a href="manager_login.php" class="w3-bar-item w3-button w3-padding-large w3-hover-black">
    <i class="fa fa-arrow-left w3-xxlarge"></i>
    <p>LOGOUT</p>
  </a>
</nav>
<!-- Page Content -->
<div class="w3-padding-large" id="main">
  <!-- Header/Home -->
  <header class="w3-container w3-padding-32 w3-center w3-black" id="home">
    <h1 class="glow"><span class="w3-hide-small">---<?php echo $name;  ?></span>---</h1>
    <p>MANAGER</p>
	<div class="w3-content w3-section" id="pos" >
  <img class="mySlides" src="image/agri11.jpg" style="width:100%;height:80%;">
  <img class="mySlides" src="image/agri2.jpg" style="width:100%;height:80%;">
  <img class="mySlides" src="image/agri3.jpg" style="width:100%;height:80%;">
  <img class="mySlides" src="image/agri4.jpg" style="width:100%;height:80%;">
  <img class="mySlides" src="image/agri5.jpg" style="width:100%;height:80%;">
<img class="mySlides" src="image/agri6.jpg" style="width:100%;height:80%;">
<img class="mySlides" src="image/agri7.jpg" style="width:100%;height:80%;">
<img class="mySlides" src="image/agri8.jpg" style="width:100%;height:80%;">
<img class="mySlides" src="image/agri9.jpg" style="width:100%;height:40%;">
<img class="mySlides" src="image/agri10.jpg" style="width:100%;height:80%;">

</div>
  </header>
</div>

  <!-- About Section -->
  <div class="w3-content w3-justify w3-text-grey w3-padding-64" id="about">
    <h2 class="w3-text-light-grey">BUSINESS MOTIVATION</h2>
    <hr style="width:200px" class="w3-opacity">
    <p>Moments of inspiration and motivation can seem elusive and fleeting when you’re a small business owner. 
	Think of how it feels when you’re on a roll: you’re focused, creative, productive, and you’re making things happen.
	It’s one of the best feelings in the world! Sadly, we all know these moments don’t last forever.
	There are times you may hit a wall. Whether it’s a mental block, a physical obstacle, 
	the loss of a sale, or the fear of the unknown holding you back,
	take comfort in the fact that every successful entrepreneur and business owner has encountered a similar situation.</p>

<?php 

$db = mysqli_connect('localhost', 'root', '', 'registration');
$sql = "SELECT * FROM users WHERE mid='$mid'";
			$result = $db->query($sql);
			if ($result->num_rows> 0)
			{
				while($row = $result->fetch_assoc())
				{
					$username= $row["username"];
					$branch = $row["branch"];
					
				}
			}
   ?>
<h2 style="text-align:left;color:white;">Manager Profile</h2>
<div id="profile">
<div class="card">
<div class="imgage">
  <img src="image/profile.png" alt="<?php echo $username;  ?>" style="width:20%">
  <h1 style="text-transform:uppercase;font-family:cursive;"><?php echo $username;?></h1>
  <p class="title" style="text-transform:uppercase;font-family:cursive;">MANAGER,</p>
  <p style="text-transform:uppercase;font-family:cursive;">BRANCH NAME : <?php echo $branch; ?></p>
 </div>
</div>
</div>
  <!-- Contact Section -->
  <div class="w3-padding-64 w3-content w3-text-grey" id="contact">
    <h2 class="w3-text-light-grey">Media</h2>
    <hr style="width:200px" class="w3-opacity">

    
    
  
    <!-- Footer -->
  <footer class="w3-content w3-padding-64 w3-text-grey w3-xlarge">
    <i class="fa fa-facebook-official w3-hover-opacity"></i>
    <i class="fa fa-instagram w3-hover-opacity"></i>
    <i class="fa fa-snapchat w3-hover-opacity"></i>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
    <!-- End footer -->
  </footer>

<!-- END PAGE CONTENT -->
</div>
<?php endif ?>
<script>
var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 2000); // Change image every 2 seconds
}
</script>
<!-- Footer -->


</body>
</html>
