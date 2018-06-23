function renderYearsChart(data) {


  var years = unpack(data, 0);
  var years_counts = unpack(data, 1);
  var colors = ["red","light-blue"]

  var data = [{
    labels: years,
    values: years_counts,
    type: "pie",
    text: years,
    textinfo: 'label',
    hoverinfo: 'value+percent',
    showlegend: false,
    marker:{
      colors: colors,
    }
  }];



  var layout = {
    showlegend: false,
    font:{
      size:10
    },
    title: "Yearly_Percentage"
  };


  var $PIE = document.getElementById("years_chart");
  Plotly.newPlot($PIE, data, layout)


}
