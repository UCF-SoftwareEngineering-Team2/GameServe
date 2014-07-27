$(document).ready(function() {

	$('.icon-close').click(function () {
	  	$('#popupWindow').toggleClass('hidden');
	  	$('#content').toggleClass('blurry');
	});

	// I don't think registration button belongs in the popup
	$('#newUser').click(function() {
		alert("redirect to creat_account page");
	});



	// Login form submission
	$('#loginButton').click(function () {
		var email =	$('#emailInput').val();
		var pass = $('#passwordInput').val();
		console.log('email: '+email);
		console.log('password: '+pass);
	});
	
	
	// Navigation bar clicks handlers
	$('.headerLink').click(function(){
		// Get current path
		var pathname = window.location.pathname ; 

		// login navi button was clicked
		if ( this.id === 'login'){
			$('#loginDropdown').toggleClass('hidden');
		}
		// Logout button clicked
		else if (this.id === 'logout') {
			window.location.href='/account/logout/';
		}
		// Home button clicked
		else if (this.id === "home"){
			if (pathname !== '/' && pathname !== '/events/') window.location.href = '/' ;
		}
		// Browse button
		else if (this.id === 'browse'){
			if (pathname !== '/events/browse/') window.location.href = "/events/browse/";
		}
		// Register button 
		else if ( this.id === 'register'){
			if (pathname !== '/account/register/') window.location.href = '/account/signup/';
		}
		// create events button (shown only if user is logged in)
		else if ( this.id === 'create'){
			if (pathname !== '/events/create/') window.location.href = '/events/create/';	
		}
		// Nada
		else {
			return ;
		}
	});
});
