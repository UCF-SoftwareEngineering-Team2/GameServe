var weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
var selectedGameType = '';
    "use strict";

$(document).ready(function() {

	// /*
	// * Global scope variables
	// */

	// var map;

	// // Keep a single instance of infowindow so there is only one popup balloon in map instance
	// var infowindow = new google.maps.InfoWindow();
	// var markers = [];
	// var lastValidCenter;
	// var list = {};
	// var crts = {};
	// // Use django_template_syntax to create json object in script
	
	// // Use django_template_syntax to create json object in script
	// (function(){
	// 	{% for s in sports  %}		
	// 		crts['{{s.sportType}}'] = []
	// 	{% endfor %}


	// 	{% for c in court %}
	// 	addToCourts('{{c.sport.sportType}}', {{c.latitude}}, {{c.longitude}});
	// 	{% endfor %}
	// })();


	// function addToCourts(sport, latitude, longitude ){
	// 	crts[sport].push({'latitude':latitude, 'longitude': longitude });
	// }


	// /*
	// * Given json object (jsonObj), assuming it is two-object-levels deep create marker instances and add to
	// * markers array.
	// */
	// function loadJSON(jsonObj){
	// 	for ( var key in jsonObj ){
	// 		for ( var el in jsonObj[key] ){
	// 			markers.push(new google.maps.Marker({
	// 				position: new google.maps.LatLng(jsonObj[key][el].latitude, jsonObj[key][el].longitude),
	// 				map: map,
	// 				animation:google.maps.Animation.DROP,
	// 				title: key
	// 			}));
	// 		}
	// 	}
	// 	return markers;
	// }

	// function loadSport(json, sport){
	// 	for ( var key in json){
	// 		if ( key === sport ){
	// 			for ( var el in json[key] ){
	// 					markers.push(new google.maps.Marker({
	// 						position: new google.maps.LatLng(jsonObj[key][el].latitude, jsonObj[key][el].longitude),
	// 						map: map,
	// 						animation:google.maps.Animation.DROP,
	// 						title: key
	// 				}));
	// 			}		
	// 		}
	// 	}
	// }


	// /*
	// * Given an array of gmap markers, add it to global map instance
	// */
	// function loadMarkers(markerArray){
	// 	if (markerArray.length > 0){
	// 		for (var i = 0; i < markers.length; i++) {
	// 			addMarkerEvent(markerArray[i]);
	// 			markerArray[i].setMap(map);
	// 		}
	// 	}
	// }




	// function addMarkerEvent(marker){
	// 	google.maps.event.addListener(marker, 'click', function(){
	// 		infowindow.setContent("<div>"+marker.title+"</div>");
	// 		infowindow.open(map,this);
	// 	});
	// }


	// var allowedBounds = new google.maps.LatLngBounds(new google.maps.LatLng(28.592276, -81.208642),
	//                                                  new google.maps.LatLng(28.611530, -81.187656));

	// function checkBoundsEvent(){
	// 	if ( allowedBounds.contains(map.getCenter())) {
	// 		lastValidCenter = map.getCenter();
	// 		return ;
	// 	}
	// 	map.panTo(lastValidCenter);
	// }



	// /*
	// * Initializes global map instance
	// */
	// function initMap(){
	// 	var mapOptions = {
	// 		zoom: 16,
	// 		minZoom:14,
	// 		maxZoom:20,
	// 		center: new google.maps.LatLng(28.601648, -81.200306),
	// 		mapTypeId: google.maps.MapTypeId.SATELLITE
	// 	};

	// 	map = new google.maps.Map(document.getElementById('mapCanvas'), mapOptions);
	// 	google.maps.event.addListener(map, 'center_changed', function(){
	// 		checkBoundsEvent();
	// 	});
	// 	google.maps.event.addListener(map, 'click', function(){
	// 		infowindow.close();
	// 	});
	// }



	// // Sets the map on all markers in the array.
	// function setAllMap(map) {
	//   for (var i = 0; i < markers.length; i++) {
	//     markers[i].setMap(map);
	//   }
	// }



	// // Deletes all markers in the array by removing references to them.
	// function deleteMarkers() {
 //  		clearMarkers();
 //  		markers = [];
	// }

	// // Removes the markers from the map, but keeps them in the array.
	// function clearMarkers() {
	// 	setAllMap(null);
	// }

	// function initialize() {
	// 	initMap();
	// 	loadMarkers(loadJSON(crts));
	// }


	// google.maps.event.addDomListener(window, 'load', function(){
	// 	initialize();
	// });



















































    var dayOWeek,
        pickedDate,
        monthDay;
    function initCalendar() {
        console.log("initingCal");
        var holder = document.getElementById("pikadayCalendarHolder");
        var picker = new Pikaday({
            field: document.getElementById('pickerInput'),
            format: "MMMM DD, YYYY",
            container: holder,
            bound: false,
            onSelect: function() {
                console.log(this.getMoment().format('DD MMMM YYYY'));
                console.log(this.getMoment().weekday());

                dayOWeek = weekdays[this.getMoment().weekday()];
                pickedDate = this.getMoment().format('DD MMMM YYYY');
                monthDay = this.getMoment().format('D MMMM');

                $('#dayOfWeek').text(dayOWeek);
                $('#monthDay').text(monthDay);


            }
        });
        picker.show()
    }

    initCalendar()

    function popupNotice(title, body){
        $('#noticeText').text(body);
        $('#noticeHeader').text(title);
        $('#popupNotice').removeClass('hidden');
        $('#fader').addClass('fade');
    }

    $('#noticeButton').click(function() {
        $('#popupNotice').addClass('hidden');
        $('#fader').removeClass('fade');
    });

    $('#publish').click(function() {
        if (selectedGameType == '') {
            popupNotice("Game Creation Error", "Choose the sport type of your game");
        }
        else if ($('#startHourSelect').val() == '') {
            popupNotice("Game Creation Error", "Choose a start hour for you game");
        }
        else if ($('#startMinSelect').val() == '') {
            popupNotice("Game Creation Error", "Choose a start minute for your game");
        }
        else if ($('#startMinSelect').val() == '') {
            popupNotice("Game Creation Error", "Choose a start minute for your game");
        }
        else{
        	console.log('in public click handler '+court_id);
            var startTime = moment(pickedDate).hours(parseInt($('#startHourSelect').val()) + ($('#amPmToggle').hasClass('am') ? 0 : 12)).minutes($('#startMinSelect').val());
            $.ajax({
                type: "POST",
                url: '/events/new_game/',
                data: {
                    dateTime: startTime.unix(),
                    duration: parseInt($('#durationHourSelect').val()) + parseInt($('#durationMinSelect').val()),
                    court:court_id
                },
                success: function(eventData, success){
                    window.location.href= window.location.origin + '/events/game/' + eventData.result.id + '/';
                }
            })
        }
    });

    $('.filterSection input').change(function() {
        $('.gameButton').removeClass('selected');
        $(this).addClass('selected');
        $('.windowBlock').find('.largeIcon').remove()
        console.log ("this item: "+ $(this).prop('id'));
        var gameIcon = document.createElement('div');
        selectedGameType = $(this).prop('id');
        gameIcon.className = "icon-" + $(this).prop('id') + " largeIcon";
        $(gameIcon).insertBefore('#afterIcon');


        // Get the sport and uppercase first letter
        var sport = selectedGameType[0].toUpperCase()+selectedGameType.slice(1);
        console.log(sport);
        deleteMarkers();

        loadMarkers(loadSport(crts,sport));

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

    $('#startHourSelect').change(function() {
        updateTime();
    });
    $('#startMinSelect').change(function() {
        updateTime();
    });
    $('#amPmToggle').click(function() {
        updateTime();
    });

    function updateTime() {
        $('#timeDisplay').text($('#startHourSelect').val() + ":" + $('#startMinSelect').val() + " " + $('#amPmToggle').text());
    }

});
