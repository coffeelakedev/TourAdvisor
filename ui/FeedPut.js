function getJSONP(url, success) {
	$.ajax({
		url:url_,
		dataType: 'jsonp', // Notice! JSONP <-- P (lowercase)
		success:function(json){
			// do stuff with json (in this case an array)
			alert("Success");
		},
		error:function(){
			alert("Error");
		}      
   });
}

function new_plan()
{
	console.log("Added New plan button detected!");
	var map_autocomplete = "https://maps.googleapis.com/maps/api/place/autocomplete/json?";
	var key = "AIzaSyC8cn_tgtIiNErOM5S5pVj8Eu9Y8gUkiXY";
	var input = encodeURI(prompt("Please Enter your Destination"));

	var request_url = map_autocomplete + 'key=' + key + '&input=' + input;
	console.log(request_url);
	getJSONP(request_url);

    document.getElementById('Feed').innerHTML = '\
    <div class="row">\
    <div class="col s12 m7">\
      <div class="card">\
        <div class="card-image">\
          <img src="images/sample-1.jpg">\
          <span class="card-title">Card Title</span>\
        </div>\
        <div class="card-content">\
          <p>I am a very simple card. I am good at containing small bits of information.\
          I am convenient because I require little markup to use effectively.</p>\
        </div>\
        <div class="card-action">\
          <a href="#">This is a link</a>\
        </div>\
      </div>\
    </div>\
  </div>'

}


function SignIn() {
  const email = document.getElementById("myInput").value;
  const pwd = document.getElementById("myInput").value;
	location.href = '/signin?email=' + email + '&pwd=' + pwd;
}
