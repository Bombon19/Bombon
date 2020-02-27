'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
<!DOCTYPE html>
<html>
<body bgcolor="#E6E6FA">
<h1>
Employee Login</h1>
<button onclick="myFunction()"name ="employeeLogin">Continue</button>

<p id="msg">
</p>
<script>
function myFunction() {
 var login = prompt("Please re-enter your name", "xxxxxx");
 
 if (login != null) {
 document.getElementById("msg").innerHTML =
 "Welcome " + login + "!! How can I help you?";
 alert("You have logged in successfully !!")
 }
}
</script>
</body>
</html>