$(document).ready(function() {
	console.log("inside");

	//login functionality
	$('#login').click(function () {
		console.log("Clicked");
		console.log ($(this).next('.linkSlider').hasClass('active'));
		// if $('.linkSlider').hasClass('active') {
	 //  		$('#loginDropdown').toggleClass('hidden');
		// }
	  	$('#loginDropdown').toggleClass('hidden');

	});

	$('.icon-close').click(function () {
	  	$('#popupWindow').toggleClass('hidden');
	  	$('#content').toggleClass('blurry');
	});

	$('#loginButton').click(function () {
		var email =	$('#emailInput').val();
		var pass = $('#passwordInput').val();

		alert("data: \email\t" + email + "\npass:\t" + pass);
	});


	$('#newUser').click(function() {
		alert("redirect to creat_account page");
	});
});