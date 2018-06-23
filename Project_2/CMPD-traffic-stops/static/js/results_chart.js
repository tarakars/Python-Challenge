
function renderResultsChart(data) {
    var $resultsDiv = document.getElementById("results_chart")
    var data_entries = unpack(data, 0);
    var data_counts = unpack(data, 1);

    var trace1 = {
      y: data_counts,
      x: data_entries,
      marker: {
        color: 'rgba(55,128,191,0.6)',
        width: 1
      },
      type: 'bar',
      width:0.4,
    };
       
     
       
    var data = [trace1];

    var layout = {
      font:{
        size : 10
      },
      title:"Results_Chart"
      }
       
       
    Plotly.newPlot('results_chart', data, layout);
  }