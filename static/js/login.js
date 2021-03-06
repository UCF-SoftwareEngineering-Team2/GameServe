"use strict";
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
            var email = $('#newEmailInput').val();
            var verEmail = $('#verEmailInput').val();
            var pass = $('#newPasswordInput').val();
            var verPass = $('#verPasswordInput').val();
            var phone = $('#pNumInput').val();

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
            else if ($('#id_password2').val() != $('#id_password1').val()) {
                popupNotice("Sign Up Error", "Password inputs do not match");
            }
            else{
                $('#newMember').submit();
            }
        }
    });

    $('#signIn').click(function() {
        var email = $('#emailInput').val();
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

    $('#existingUser').click(function(){
    	return window.location = "/account/login/";
    });

    $('#newUser').click(function(){
    	return window.location = "/account/signup/";
    });

});
