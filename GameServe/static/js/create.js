console.log("create file working!!");
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

	$('.gameButton').click(function() {
		$('.gameButton').removeClass('selected');
		$(this).addClass('selected');
		$('.windowBlock').find('.largeIcon').remove()
		console.log ("this item: "+ $(this).prop('id'));
		var gameIcon = document.createElement('div');
		gameIcon.className = "icon-" + $(this).prop('id') + " largeIcon";
		$(gameIcon).insertBefore('#afterIcon');
	});

	$('#amPmToggle').click(function() {
		if ($('#amPmToggle').hasClass('am')) {
			$('#amPmToggle').text('AM');
			$('#amPmToggle').toggleClass('am');
		}
		else {
			$('#amPmToggle').text('PM');
			$('#amPmToggle').toggleClass('am');
		}
	});	

	$('#hourSelect').change(function() {
		updateTime();
	});
	$('#minSelect').change(function() {
		updateTime();
	});
	$('#amPmToggle').click(function() {
		updateTime();
	});
	function updateTime() {
		$('#timeDisplay').text($('#hourSelect').val() + ":" + $('#minSelect').val() + " " + $('#amPmToggle').text());
	}

});
