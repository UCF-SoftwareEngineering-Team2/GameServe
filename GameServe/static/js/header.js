$(document).ready(function() {
	console.log("inside");

	//login functionality
	$('#login').click(function () {
	  	$('#popupWindow').toggleClass('hidden');
	});
	$('#loginButton').click(function () {
	  	alert("email input: " + $('#emailInput').val() + "\npass input: " +$('#passwordInput').val());
	});
});