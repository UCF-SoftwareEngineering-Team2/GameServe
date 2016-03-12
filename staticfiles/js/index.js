"use strict";
$(document).ready(function() {

	//This sets up the CSRF token for all ajax calls made in the javascript
	var csrftoken = $.cookie('csrftoken');function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});

	//Google Maps
	function initialize() {
		var myLatlng = new google.maps.LatLng(28.601648, -81.200306);  
		var mapOptions = {
			zoom: 15,
			center: myLatlng,
			mapTypeId: google.maps.MapTypeId.MAP
		}
		var map = new google.maps.Map(document.getElementById('mapCanvas'), mapOptions);
	}
	google.maps.event.addDomListener(window, 'load', initialize);

	//selecting game types to browse
	$('.gameType').click(function () {
	  	$(this).toggleClass('selected');
	});
	$('#selectAll').click(function() {
		$('input').each(function() {
			$(this).prop('checked', true);
		});
	});
	$('#clearAll').click(function() {
		$('input').each(function() {
			$(this).prop('checked', false);
		});
	});


});
