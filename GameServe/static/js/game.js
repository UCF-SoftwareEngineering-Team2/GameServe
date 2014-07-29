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
	//show date & time
	$('#time').text(eventHour + ":" + eventMin + " " + amPm);
	$('#weekday').text(dayOWeek[eventDateDOW]);
	$('#monthDay').text(months[eventMonth] + " " + eventDay);

	//user click verify
	$('#verify').click(function() {
		alert("user clicked verify");
	});	

	//user click commit, thus a post is sent to the server committing the user with the current eventId
	$('#commit').click(function() {
		$.ajax({
			type: "POST",
			url: '/events/commit/',
			data: {event: eventId},
			success: function(){
			}
		})
	});	

});
