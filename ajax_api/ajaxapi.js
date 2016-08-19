
function grabData(){
	var name = $("#title").val();

	$.ajax({
        url:'http:www.omdbapi.com/?t=' + name, //whatever is searched
        //if it returns something
        success: function(result){
            //print whatever movie title we have in json format
            print_result(result);
        }
    })

    //$.ajax({
    	//url:'' + name,
    	//success: function(result){
    		//print_result(result);
    	//}
    //})
}

function print_result(obj){
	$("#content").text('');

	for(var i in obj){
		if (i !== "Poster") {
			$("#content").append('<p>' + i + ': ' + obj[i] + '</p>');
		}
		else if(i == "Poster") {
			var image = document.createElement("img");
			image.src = obj[i];
			$('#poster').append(image);

		}
	}
}






$('#submit').click(function(){
	grabData();
})