
function renderReasonsChart(data) {
  var $reasonsDiv = document.getElementById("reasons_chart")

  var data_entries = unpack(data, 0);
  var data_counts = unpack(data, 1);

  var trace1 = {
    y: data_counts,
    x: data_entries,
    text: data_entries,
    hoverinfo: 'none',
    marker: {
      color: 'rgba(55,128,191,0.6)',
      width: 1
    },
    type: 'bar',
    title: "Reasons Chart"
  };

  var layout = {
    font:{
      size : 10
    },
    title:"Reasons_Chart"
    }
     
   
     
  var data = [trace1];

     
  Plotly.newPlot('reasons_chart', data,layout);
}