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


	// $.ajax({
 //          type: "POST",
 //          url: "http://localhost/DatabaseProject/ElderlyAssistanceProject/addCareRequest.php",
 //          dataType: 'json',
 //          data: {
 //            Type: 'Update',
 //            Vid: volunteer,
 //            Rid: request
 //          },
 //          success: function() {
 //            return console.log('success!');
 //          },
 //          error: function(xhr, desc, err) {
 //            console.log(xhr);
 //            console.log("Details: " + desc + "\nError:" + err);
 //            return console.log('did not work...');
 //          }
 //        });
 //        return false;

 //        $.ajax({
	// 		type: "POST",
	// 		url: "http://localhost/DatabaseProject/ElderlyAssistanceProject/addCareRequest.php",
	// 		dataType: 'json',
	// 		data: {
	// 			Type: 'New',
	// 			Rid: rid,
	// 			Cid: id,
	// 			ride: ride,
	// 			meal: meal,
	// 			visit: visit,
	// 			pickup: pickup,
	// 			other: other,
	// 			otherNotes: otherNotes,
	// 			month: month,
	// 			reqDayNum: reqDayNum,
	// 			rDayOfWeek: rDayOfWeek,
	// 			year: year,
	// 			reqStartHour: reqStartHour,
	// 			reqStartMin: reqStartMin,
	// 			reqStartAmPm: reqStartAmPm,
	// 			reqEndHour: reqEndHour,
	// 			reqEndMin: reqEndMin,
	// 			reqEndAmPm: reqEndAmPm,
	// 			notes: notes
	// 		},
	// 		success: function() {
	// 			return console.log('success!');
	// 		},
	// 		error: function(xhr, desc, err) {
	// 			console.log(xhr);
	// 			console.log("Details: " + desc + "\nError:" + err);
	// 			return console.log('did not work...');
	// 		}
 //        });
});
