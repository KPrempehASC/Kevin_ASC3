//Setting reference
var database = firebase.database().ref();

function sendMessage() {
	var firstName = $("#first").val();
	var lastName = $("#last").val();
	var message = $("#msg").val();
	database.push({
		'first': firstName,
		'last': lastName,
		'msg': message,
	});

	$("#first").val('');
	$("#last").val('');
	$("#msg").val('');

	database.on('child_added', function(dataRow) {
		var row = dataRow.val();
		//adding to the div
		$("database_msg").append("<p>" + "Name:" + row.firstName + " " + row.lastName + " said:" + "<br>" + row.message);
	})
}