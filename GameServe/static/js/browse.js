console.log("javascript file working!!");
$(document).ready(function() {
	console.log("inside");

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
	$('#submitComment').click(function() {
		var comment = $('#commentInput').val();
		alert("comment:\n" + comment );
	});

});
