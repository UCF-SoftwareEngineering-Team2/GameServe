$(document).ready(function() {
	console.log("inside");

	//login functionality
	$('#login').click(function () {
	  	$('#popupWindow').toggleClass('hidden');
	  	$('#content').toggleClass('blurry');
	});
	$('.icon-close').click(function () {
	  	$('#popupWindow').toggleClass('hidden');
	  	$('#content').toggleClass('blurry');
	});
	$('#loginButton').click(function () {
		if ($('#popupWindow').hasClass('expand')) {
			var name = $('#nameInput').val();
			var email =	$('#newEmailInput').val();
			var verEmail = $('#verEmailInput').val();
			var pass = $('#newPasswordInput').val();
			var verPass = $('#verPasswordInput').val();
			var phone = $('#pNumInput').val();

	  		alert("data: \nname:\t" + name + " \nemail:\t" + email + " \nverEmail:\t" + verEmail + " \npass:\t" + pass + " \nverPass:\t" + verPass + " \nphone:\t" + phone );
		}
		else {
			var email =	$('#emailInput').val();
			var pass = $('#passwordInput').val();

	  		alert("data: \email\t" + email + "\npass:\t" + pass);
	  	}
	});


	$('#newUser').click(function() {
		if ($(this).text() == "New Member") {
			$(this).text("Existing Member");
			$('#popupWindow').addClass('expand');
			$('#loginHeader').text("Sign up for gameServe");
			$('#existingMember').addClass('hidden');
			$('#newMember').removeClass('hidden');
		}
		else {
			$(this).text('New Member');
			$('#popupWindow').removeClass('expand');
			$('#loginHeader').text("Login to gameServe");
			
			$('#existingMember').removeClass('hidden');
			$('#newMember').addClass('hidden');
		} 
	});
});