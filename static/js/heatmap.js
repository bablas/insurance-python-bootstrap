

var myMap = L.map("map", {
  center: [35, -95],
  zoom: 4
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

var url = coordinates;

console.log(url)


var markers = L.markerClusterGroup();

  for (var i = 0; i < url.length; i++) {


    console.log([url[i].Latitude, url[i].Longitude])
    if (url[i].Latitude != 'NULL' && url[i].Longitude != 'NULL'){
      markers.addLayer(L.marker([url[i].Latitude, url[i].Longitude]));
    }
  }

  myMap.addLayer(markers);
  /*var heat = L.heatLayer(heatArray, {
    radius: 20,
    blur: 35
  }).addTo(myMap);*/
