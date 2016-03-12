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


	var currentMoreUrl,
		initialGet;
	if($('.infinite-more-link')[0]){
		currentMoreUrl = $('.infinite-more-link')[0].href;
		initialGet = $('.infinite-more-link')[0].href.split('/?')[0] + '/';
	}
	
	//Initalizes infinite scrolling, grabbing list items 
	var waypointSettings = {
		items: '.infinite-item',
		onAfterPageLoad: function(){
			if($('.infinite-more-link') && $('.infinite-more-link')[0]){
				currentMoreUrl = $('.infinite-more-link')[0].href;
			}
			else{
				$('.window > .gamesList').append('<div class="noItems">No more items to load </div>')
			}
		}
	}
	$('.window > .gamesList').waypoint('infinite', waypointSettings);

	//Change the infinite scroll link based on the current filter
	$('input').change(function(){
		if($('.infinite-more-link') && $('.infinite-more-link')[0]){
			$('.infinite-more-link')[0].href = currentMoreUrl + '&' + $('.filterResults form').serialize();
		}
	})

	//Filters the results
	$('.filterButton').click(function(){
		$('.gamesList').empty();

		//Creates the get request based on the form
		var htmlList = $.get('/events/upcoming_events/?numEvents=15&html=True&' + $('.filterResults form').serialize());

		//When it is done, import the data, and append each element to gamesList
		htmlList.done(function(data, success, error){
			var newElement = data;
			newElement = $(newElement);
			newElement = newElement.children();
			$('.gamesList').append(newElement);

			//Recreate the infinite link if it is there
			if($('.infinite-more-link') && $('.infinite-more-link')[0]){
				currentMoreUrl = $('.infinite-more-link')[0].href;
				$('.infinite-more-link')[0].href = currentMoreUrl + '&' + $('.filterResults form').serialize();
			}
			else{
				$('.window > .gamesList').append('<div class="noItems">No more items to load </div>')
			}

			//Reinitialize infinite scrolling
			$('.window > .gamesList').waypoint('infinite', waypointSettings);
		});
	})

	//selecting game types to browse
	$('#submitComment').click(function() {
		var comment = $('#commentInput').val(); 
		alert("comment:\n" + comment );
	});

});
