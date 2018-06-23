

function renderDivisionsChart(data) {

  var data_entries = unpack(data, 0);
  var data_counts = unpack(data, 1);

  console.log(data_entries);
  console.log(data_counts);
 
  //find the max value in the array of stop counts: create a copy and sort the copy
  var max_count = data_counts.slice().sort(function (a, b) { return b - a })[0];
  console.log(data_counts);
 
  console.log(max_count);
  for (var i = 0; i < data_entries.length; i++) {

    map_shades[data_entries[i]] = data_counts[i] / max_count;
    map_counts[data_entries[i]] = data_counts[i];
  }

  // redraw the map in the iframe
  document.getElementById('mapper').contentWindow.location.reload(true);

}
