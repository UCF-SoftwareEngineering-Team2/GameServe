$(document).ready(function() {
	"use strict";

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

	//Initalizes infinite scrolling, grabbing list items 
	$('.window.gamesContainer').waypoint('infinite',{
		items: '.listItem'

	});

	//selecting game types to browse
	$('#submitComment').click(function() {
		var comment = $('#commentInput').val(); 
		alert("comment:\n" + comment );
	});

});
