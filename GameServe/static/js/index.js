$(document).ready(function() {

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
		$('.gameType').each(function() {
			$(this).addClass('selected');
		});
	});
	$('#clearAll').click(function() {
		$('.gameType').each(function() {
			$(this).removeClass('selected');
		});
	});


});
