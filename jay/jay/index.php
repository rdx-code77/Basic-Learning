
<?php  
	
if (isset($_POST['send'])) {
  $username = mysqli_real_escape_string($db, $_POST['Name']);
  $email = mysqli_real_escape_string($db, $_POST['Email']);
  $subject = mysqli_real_escape_string($db, $_POST['Subject']);
$msg = mysqli_real_escape_string($db, $_POST['Message']);
$to= "ameshmogaveera123@gmail.com";

mail($to,$subject,$msg,$username);

}

?>
<!DOCTYPE html>
<html>
<head>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<style>
html,body,h1,h2,h3,h4 {font-family:"Lato", sans-serif}
.mySlides {display:none}
.w3-tag, .fa {cursor:pointer}
.w3-tag {height:15px;width:15px;padding:0;margin-top:6px}
.glow {
  font-size: 40px;
  color: rgb(36, 5, 109);
  text-transform: uppercase;
  text-align: center;
  -webkit-animation: glow 1s ease-in-out infinite alternate;
  -moz-animation: glow 1s ease-in-out infinite alternate;
  animation: glow 1s ease-in-out infinite alternate;
}

-webkit-keyframes glow {
 from {
    text-shadow: 0 0 10px #0e0679, 0 0 20px #6b6b47, 0 0 30px #6b6b47, 0 0 40px #6b6b47;
  }
  
  to {
    text-shadow: 0 0 20px 	#500808, 0 0 30px 	#630909, 0 0 40px 	#5e0707;
  }
</style>
<script type="text/javascript" >
   function preventBack(){window.history.forward();}
    setTimeout("preventBack()", 0);
    window.onunload=function(){null};
</script>

<body>

<!-- Links (sit on top) -->
<div class="w3-top">
  <div class="w3-row w3-medium w3-light-grey">
    <div class="w3-col s2">
      <a href="#" class="w3-button w3-block">APMC</a>
    </div>
    <div class="w3-col s2">
      <a href="login.php" class="w3-button w3-block">Admin</a>
    </div>
    <div class="w3-col s2">
      <a href="manager_login.php" class="w3-button w3-block">Manager</a>
    </div>
    <div class="w3-col s2">
      <a href="owner_login.php" class="w3-button w3-block">Shopowner</a>
    </div>
    <div class="w3-col s2">
      <a href="price_chart.php" class="w3-button w3-block">Price chart</a>
    </div>
    <div class="w3-col s2">
      <a href="#contact" class="w3-button w3-block">Contact</a>
    </div>
  </div>
</div>

<!-- Content -->
<div class="w3-content" style="max-width:1100px;margin-top:80px;margin-bottom:80px">

  <div class="w3-panel">
    <h1 class="glow"><b>AGRICULTURAL PRODUCE MARKET COMMITTEE</b></h1>
    
  </div>

  <!-- Slideshow -->
  <div class="w3-container">
    <div class="w3-display-container mySlides">
      <img src="image/agri11.jpg" style="width:100%">
      <div class="w3-display-topleft w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">Buffalo</span>
      </div>
    </div>
    <div class="w3-display-container mySlides">
      <img src="image/agri12.jpg" style="width:100%">
      <div class="w3-display-topright w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">Sheep</span>
      </div>
    </div>
	<div class="w3-display-container mySlides">
      <img src="image/agri15.jpg" style="width:100%">
      <div class="w3-display-middle w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">Farming</span>
      </div>
    </div>
    <div class="w3-display-container mySlides">
      <img src="image/agri5.jpg" style="width:100%">
      <div class="w3-display-bottomright w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">Apricot</span>
      </div>
    </div>
	<div class="w3-display-container mySlides">
      <img src="image/agri13.jpg" style="width:100%">
      <div class="w3-display-bottomleft w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">Tractor</span>
      </div>
    </div>
	<div class="w3-display-container mySlides">
      <img src="image/agri14.jpg" style="width:100%">
      <div class="w3-display-middle w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">Field</span>
      </div>
    </div>
	<div class="w3-display-container mySlides">
      <img src="image/agri7.jpg" style="width:100%">
      <div class="w3-display-middle w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">CHICKEN</span>
      </div>
    </div>
	<div class="w3-display-container mySlides">
      <img src="image/agri15.jpg" style="width:100%">
      <div class="w3-display-middle w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">Farming</span>
      </div>
    </div>
	<div class="w3-display-container mySlides">
      <img src="image/agri8.jpg" style="width:100%">
      <div class="w3-display-middle w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">APPLE</span>
      </div>
    </div>
	<div class="w3-display-container mySlides">
      <img src="image/agri14.jpg" style="width:100%">
      <div class="w3-display-middle w3-container w3-padding-32">
        <span class="w3-white w3-padding-large w3-animate-bottom">Field</span>
      </div>
    </div>

    <!-- Slideshow next/previous buttons -->
    <div class="w3-container w3-dark-grey w3-padding w3-xlarge">
      <div class="w3-left" onclick="plusDivs(-1)"><i class="fa fa-arrow-circle-left w3-hover-text-teal"></i></div>
      <div class="w3-right" onclick="plusDivs(1)"><i class="fa fa-arrow-circle-right w3-hover-text-teal"></i></div>
    
      <div class="w3-center">
        <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(1)"></span>
        <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(2)"></span>
        <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(3)"></span>
     <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(4)"></span>
        <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(5)"></span>
        <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(6)"></span>
     <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(7)"></span>
        <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(8)"></span>
        <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(9)"></span>
              <span class="w3-tag demodots w3-border w3-transparent w3-hover-white" onclick="currentDiv(10)"></span>
</div>
    </div>
  </div>
  
  <!-- Grid -->
  <div class="w3-row w3-container">
    <div class="w3-center w3-padding-64">
      <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">What We Offer</span>
    </div>
    <div class="w3-col l3 m6 w3-light-grey w3-container w3-padding-16">
      <h3>Design</h3>
      <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p>
    </div>

    <div class="w3-col l3 m6 w3-grey w3-container w3-padding-16">
      <h3>Branding</h3>
      <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p>
    </div>

    <div class="w3-col l3 m6 w3-dark-grey w3-container w3-padding-16">
      <h3>Consultation</h3>
      <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p>
    </div>

    <div class="w3-col l3 m6 w3-black w3-container w3-padding-16">
      <h3>Promises</h3>
      <p>Phasellus eget enim eu lectus faucibus vestibulum. Suspendisse sodales pellentesque elementum.</p>
    </div>
  </div>
  
    <div class="w3-third w3-margin-bottom">
      
    </div>
  
  <!-- Contact -->
  <div class="w3-center w3-padding-64" id="contact">
    <span class="w3-xlarge w3-bottombar w3-border-dark-grey w3-padding-16">Contact Us</span>
  </div>

  <form class="w3-container" action="index.html" method="POST" target="_self">
    <div class="w3-section">
      <label>Name</label>
      <input class="w3-input w3-border w3-hover-border-black" style="width:100%;" type="text" name="Name" required>
    </div>
    <div class="w3-section">
      <label>Email</label>
      <input class="w3-input w3-border w3-hover-border-black" style="width:100%;" type="text" name="Email" required>
    </div>
    <div class="w3-section">
      <label>Subject</label>
      <input class="w3-input w3-border w3-hover-border-black" style="width:100%;" name="Subject" required>
    </div>
    <div class="w3-section">
      <label>Message</label>
      <input class="w3-input w3-border w3-hover-border-black" style="width:100%;" name="Message" required>
    </div>
    <button type="submit" class="w3-button w3-block w3-black" name="send">Send</button>
  </form>

	
</div>

<!-- Footer -->

<footer class="w3-container w3-padding-32 w3-light-grey w3-center">
  
  <a href="#" class="w3-button w3-black w3-margin"><i class="fa fa-arrow-up w3-margin-right"></i>To the top</a>
  <div class="w3-xlarge w3-section">
    <i class="fa fa-facebook-official w3-hover-opacity"></i>
    <i class="fa fa-instagram w3-hover-opacity"></i>
    <i class="fa fa-snapchat w3-hover-opacity"></i>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
  </div>
</footer>


<script>
// Slideshow
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function currentDiv(n) {
  showDivs(slideIndex = n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demodots");
  if (n > x.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = x.length} ;
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" w3-white", "");
  }
  x[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " w3-white";
}
</script>

</body>
</html>
