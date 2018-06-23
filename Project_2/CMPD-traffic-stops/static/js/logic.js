// Creating map object
var map = L.map("map", {
  center: [35.2, -80.8],
  zoom: 9.5
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1IjoidGFyYWthcnMiLCJhIjoiY2ppMmE0cmZzMDFweTNrcGlnYmF5dmt1byJ9.sgeugeGHP0-w2HmmDj8C2A").addTo(map);

var link = "https://clt-charlotte.opendata.arcgis.com/datasets/47167ee6d69248acbd825f2859c68dbf_5.geojson";

// Function that will determine the color of a division based on the DNAME
function chooseColor(DNAME) {

  try {
    var number = parent.map_shades[DNAME]
console.log(DNAME);
    var b= Math.round(number);
    var g= Math.round(2*number/3).toString();
    var r= Math.round(number/2).toString();
    
    //   return "#" + number.toString(16);
    //color_str = 'rgba(' + r + ',' + g + ',' + b + ',0.9)';
     color_str = 'rgba(50,100,255,'+number.toString()+')';
    
    console.log(color_str);
    return color_str;

  }
  catch (err) {
    return 'rgba(50,100,255,0)';
  }


}

// Grabbing our GeoJSON data..
d3.json(link, function (data) {
  // Creating a geoJSON layer with the retrieved data
  L.geoJson(data, {
    // Style each feature (in this case a division)
    style: function (features) {
      return {
        color: "grey",
        // Call the chooseColor function to decide which color to color our division (color based on DNAME)
        fillColor: chooseColor(features.properties.DNAME),
        fillOpacity: 0.7,
        weight: 1.5
      };
    },
    // Called on each feature
    onEachFeature: function (features, layer) {
      // Set mouse events to change map styling
      layer.on({
        // When a feature (division) is clicked, the parent window filter parameter is set and filter is applied to all charts
        click: function (event) {
          item = event.target.feature.properties.DNAME;
          parent.division_filter = item;
          parent.renderAllCharts();

        }
      });

      function putDivisionCountInLayer(json) {

        var dname = features.properties.DNAME
        var dcount = 0

        var division_data = json.division_data

        for (var i = 0; i < division_data.length; i++) {
          if (dname === division_data[i][0]) {
            dcount = division_data[i][1]
          }
        }
        // Giving each feature a pop-up with information pertinent to it
        layer.bindPopup("<h1>" + features.properties.DNAME + "</h1> <hr> <h2>" + "Number of Stops: " + dcount + "</h2>");

      }

      d3.json('/data' + parent.getCurrentFilterParams(), putDivisionCountInLayer)

    }
  }).addTo(map);
});
