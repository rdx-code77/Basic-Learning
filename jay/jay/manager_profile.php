<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body{
	 background-image: url("image/bck.jpg");
}
.card {
  box-shadow: 0 20px 20px 0 rgba(0, 0, 0, 1);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
  background-color: grey;
}

.title {
  color: black;
  font-size: 18px;
}


button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}
img{
	border-radius: 50%;
}
img:hover {
  animation: shake 0.5s;
  animation-iteration-count: infinite;
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
button:hover, a:hover {
  opacity: 0.7;
}
</style>
<script type="text/javascript" >
   function preventBack(){window.history.forward();}
    setTimeout("preventBack()", 0);
    window.onunload=function(){null};
</script>
</head>
<body>
<?php include('manager_server.php') ?>
<?php 
$mid=$_SESSION['mid'];
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
<h2 style="text-align:center;color:white;">User Profile Card</h2>
<div class="img">
<div class="card">
<br>
  <img src="image/amb1.jpg" alt="<?php echo $username;  ?>" style="width:80%">
  <h1 style="text-transform:uppercase;font-family:cursive;"><?php echo $username;?></h1>
  <p class="title" style="text-transform:uppercase;font-family:cursive;">MANAGER,</p>
  <p style="text-transform:uppercase;font-family:cursive;">BRANCH NAME : <?php echo $branch; ?></p>
  <div style="margin: 24px 0;">
    <a href="#"><i class="fa fa-dribbble"></i></a> 
    <a href="#"><i class="fa fa-twitter"></i></a>  
    <a href="#"><i class="fa fa-linkedin"></i></a>  
    <a href="#"><i class="fa fa-facebook"></i></a> 
  </div>
  <p><button>Contact</button><button><a href="manager.php" style="text-decoration:none;color:white;">BACK</a></button></p>
</div>
</div>
</body>
</html>
