var url = "http://maps.googleapis.com/maps/api/staticmap?center=75+9th+Ave,+New+York,+NY+10011&zoom=16&scale=false&size=600x300&maptype=roadmap&format=png&visual_refresh=true&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C601+26th+St.+NYC";
var markerStart = "markers=icon:http://pldh.net/media/pokemon/gen3/frlg/149.png"

var pickas = ["1000 26th st.NYC"];

url = url + markerStart + encodeURI(pickas[0]);

var htmlIMG = document.createElement("img");
$("body").append(htmlIMG);
$("img").attr("src", url);