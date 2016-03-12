console.log("game file working!!");
"use strict";

$(document).ready(function() {
	console.log("inside");

	var dayOWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
	var months = ["null", "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
	var amPm = "am";
	
	//calc time
	if (eventHour % 12 > 0) {
		amPm = "pm";
		eventHour = eventHour % 12;
	}
	if (eventMin.length < 2 ) {
		eventMin = "0"+eventMin;
	}

	var time = moment().minutes(eventDuration);
	//show date & time
	$('#duration').text((eventDuration/60).toFixed(0) + ":" + eventDuration%60 + " hours");
	$('#time').text(eventHour + ":" + eventMin + " " + amPm);
	$('#weekday').text(dayOWeek[eventDateDOW]);
	$('#monthDay').text(months[eventMonth] + " " + eventDay);

	//user click commit, thus a post is sent to the server committing the user with the current eventId
	$('#commit').click(function() {
		$.ajax({
			type: "POST",
			url: '/events/commit/',
			data: {event: eventId},
			success: function(){
				$('#commit').addClass('invis');
				$('#uncommit').removeClass('invis');
				$('#verify').removeClass('invis');
				var currentCount = parseInt($('#participantsCount')[0].innerHTML);
				currentCount++;
				$('#participantsCount')[0].innerHTML = currentCount;
			}
		});
	});	

	$('#uncommit').click(function() {
		$.ajax({
			type: "POST",
			url: '/events/uncommit/',
			data: {event: eventId},
			success: function(){
				$('#uncommit').addClass('invis');
				$('#verify').addClass('invis');
				$('#unverify').addClass('invis');
				$('#commit').removeClass('invis');
				var currentCount = parseInt($('#participantsCount')[0].innerHTML);
				currentCount--;
				$('#participantsCount')[0].innerHTML = currentCount;
			}
		});
	});

	$('#verify').click(function() {
		$.ajax({
			type: "POST",
			url: '/events/check_in/',
			data: {event: eventId},
			success: function(eventData, success){
				if(!eventData || typeof eventData.result === 'string'){
					alert(eventData.result);
				}
				else{
					$('#uncommit').addClass('invis');
					$('#verify').addClass('invis');
					$('#unverify').removeClass('invis');
					var currentCount = parseInt($('#checkedInCount')[0].innerHTML);
					currentCount++;
					$('#checkedInCount')[0].innerHTML = currentCount;
				}
			}
		});
	});


	$('#unverify').click(function() {
		$.ajax({
			type: "POST",
			url: '/events/cancel_check_in/',
			data: {event: eventId},
			success: function(){
				$('#uncommit').removeClass('invis');
				$('#unverify').addClass('invis');
				$('#verify').removeClass('invis');
				var currentCount = parseInt($('#checkedInCount')[0].innerHTML);
				currentCount--;
				$('#checkedInCount')[0].innerHTML = currentCount;
			}
		});
	});

});
