$(document).ready(function() {
	function popupNotice(title, body){
		$('#noticeText').text(body);
		$('#noticeHeader').text(title);
		$('#popupNotice').removeClass('hidden');
		$('#fader').addClass('fade');
	}

	$('#signUp').click(function () {
		if ($('.accountSection').hasClass('expand')) {
			var name = $('#nameInput').val();
			var email =	$('#newEmailInput').val();
			var verEmail = $('#verEmailInput').val();
			var pass = $('#newPasswordInput').val();
			var verPass = $('#verPasswordInput').val();
			var phone = $('#pNumInput').val();

	  		alert('data: \nname:\t' + name + ' \nemail:\t' + email + ' \nverEmail:\t' + verEmail + ' \npass:\t' + pass + ' \nverPass:\t' + verPass + ' \nphone:\t' + phone );
			if ($('#pNumInput').val() == '') {
				popupNotice("Sign Up Error", "Must add an phone number");
			}
			else if ($('#nameInput').val() == '') {
				popupNotice("Sign Up Error", "Must choose a username");
			}
			else if ($('#newEmailInput').val() == '') {
				popupNotice("Sign Up Error", "Must add an email");
			}
			else if ($('#newPasswordInput').val() == '') {
				popupNotice("Sign Up Error", "Must add a password");
			}
			else if ($('#newEmailInput').val() != $('#verEmailInput').val()) {
				popupNotice("Sign Up Error", "Email inputs do not match");
			}
			else if ($('#newPasswordInput').val() != $('#verPasswordInput').val()) {
				popupNotice("Sign Up Error", "Password inputs do not match");
			}
		}
	});
	
	$('#signIn').click(function() {
		var email =	$('#emailInput').val();
		var pass = $('#passwordInput').val();

		alert('data: \email\t' + email + '\npass:\t' + pass);
		if (email == '') {
			popupNotice("Login Error", "Invalid email");
		}
		else if (pass == '') {
			popupNotice("Login Error", "Invalid Password");
		}
	});

	$('#noticeButton').click(function() {
		$('#popupNotice').addClass('hidden');
		$('#fader').removeClass('fade');
	});

	// $('#newVsOldUser').click(function() {
	// 	if ($(this).text() == 'New Member') {
	// 		$(this).text('Existing Member');
	// 		$('#signIn').addClass('hidden');
	// 		$('#signUp').removeClass('hidden');
	// 		$('.accountSection').addClass('expand');
	// 		$('#loginHeader').text('Sign up for gameServe');
	// 		$('#oldMember').addClass('hidden');
	// 		$('#newMember').removeClass('hidden');
	// 		$('#facebookLogin').removeClass('signIn');
	// 		$('#facebookText').text('Create an account through facebook');
	// 	}
	// 	else {
	// 		$(this).text('New Member');
	// 		$('.accountSection').removeClass('expand');
	// 		$('#signIn').removeClass('hidden');
	// 		$('#signUp').addClass('hidden');
	// 		$('#loginHeader').text('Login to gameServe');
	// 		$('#signIn').text('Login');
	// 		$('#oldMember').removeClass('hidden');
	// 		$('#newMember').addClass('hidden');
	// 		$('#facebookLogin').addClass('signIn');
	// 		$('#facebookText').text('Login through facebook');
	// 	} 
	// });

	$('#facebookLogin').click(function() {
		if ($(this).hasClass('signIn')) {
			alert('initiate Facebook Login');
		}
		else {
			alert('initiate Facebook account creation');
		}
	});	
});