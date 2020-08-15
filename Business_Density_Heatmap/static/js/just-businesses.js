var myMap = L.map("map", {
  // updated to Las Vegas
  center: [36.1699, -115.1398],
  zoom: 13
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

var newtry = "/api/restaurants";

d3.json(newtry, function (response) {

  var businesses = response.businesses;
  var heatArray = [];

  for (var i = 0; i < 1000; i++) {
    var location = ([businesses[i].latitude, businesses[i].longitude]);
    console.log(location);
    if (location) {
      var mark = L.marker(location).addTo(myMap);
      heatArray.push(location);
      mark.bindPopup(businesses[i].name)
    }
  }
  var heat = L.heatLayer(heatArray, {
    radius: 100,
    blur: 35
  }).addTo(myMap);
});
