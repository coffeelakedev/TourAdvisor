function new_plan()
{
	console.log("Added New plan button detected!");
	const map_autocomplete = "https://maps.googleapis.com/maps/api/place/autocomplete/json?";
	const key = "AIzaSyC8cn_tgtIiNErOM5S5pVj8Eu9Y8gUkiXY";
	
	const input = "A";

	const request_url = map_autocomplete + 'key=' + key + '&input=' + input;
	console.log(request_url);
	$.get(request_url, 
		function(data, status)
		{
			alert("Data: " + data + "\nStatus: " + status);
		}
	);

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
