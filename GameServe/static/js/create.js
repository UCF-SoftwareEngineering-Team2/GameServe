var weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
var selectedGameType = '';
	"use strict";

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

	// function initCalendar() {
	// 	datepicker = $('.datepicker.start')[0]
	// 	if datepicker?
	// 		var holder = document.getElementById("pikadayCalendarHolder");
	// 		$scope.startPicker = new Pikaday
	// 			// field: datepicker
	// 			format: "MMMM DD, YYYY"
	// 			defaultDate: moment(datepicker.value).toDate()
	// 			setDefaultDate: false
	// 			startdate: true
	// 			start: true
	// 			container: holder
	// 			bound: false
	// 		$scope.startPicker.show()

	// 		$(datepicker).on 'keyup', ->
	// 			$scope.startPicker.gotoDate(moment(this.value).toDate())
	// }
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
			var startTime = moment(pickedDate).hours(parseInt($('#startHourSelect').val()) + ($('#amPmToggle').hasClass('am') ? 0 : 12)).minutes($('#startMinSelect').val());
			$.ajax({
				type: "POST",
				url: '/events/new_game/',
				data: {
					dateTime: startTime.unix(),
					duration: parseInt($('#durationHourSelect').val()) + parseInt($('#durationMinSelect').val()),
					court:1
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
