"use strict";

$(document).ready(function() {

    $('.icon-close').click(function () {
        $('#popupWindow').toggleClass('hidden');
        $('#content').toggleClass('blurry');
    });

    $('#loginButton').click(function () {
        var email = $('#emailInput').val();
        var pass = $('#passwordInput').val();
        $('#loginDropdown').remove('p');
        return $.ajax({
            url:'/profile/ajax/',
            type:"POST",
            data:{'username':email,'password':pass,'csrfmiddlewaretoken':$('#csrf').attr('value')},
            success:function(data,status){
                console.log(status);
                window.location.reload();
                return data.responseJSON ;
            },
            error:function(data,status){
                $('#loginDropdown').append($('<p>Invalid username/password</p>'));
                return data.responseJSON;
            },
            complete:function(data,status){
                console.log(status);
            },
            fail:function(data,status){
                console.log(status);
            }
        });
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
            if (pathname !== '/account/signup/') window.location.href = '/account/signup/';
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
