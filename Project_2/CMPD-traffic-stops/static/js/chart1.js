function renderChart1() {
    Plotly.d3.json("/data_chart1" + getCurrentFilterParams(), function (error, response) {
        var $chartDiv = document.getElementById("chart1")

        var data_entries = unpack(response, 0)
        var data_counts = unpack(response, 2)
        var data_category = unpack(response, 1)
        var curr_category = ""
        var trace_labels = []
        var trace_counts = []
        var data = []
        var trace = {}
        var layout={}

        var categories = data_category.filter(function (item, pos) {
            return data_category.indexOf(item) == pos;
        });


        for (var i = 0; i < categories.length; i++) {
            curr_category = categories[i];
            trace_labels = [];
            trace_counts = [];

            for (var k = 0; k < data_category.length; k++) {
                if (data_category[k] == curr_category) {
                    trace_labels.push(data_entries[k]);
                    trace_counts.push(data_counts[k]);
                }
            }


            trace = {
                x: trace_labels,
                y: trace_counts,
                name: curr_category,
                type: 'bar',
            };

            data.push(trace);


            // console.log(curr_category);
            // console.log(trace_labels);
            // console.log(trace_counts);
        }
        layout = {
            barmode: 'stack',
            font:{
                size:10
            },
        title: "Yearly Numbers of stops based on age",

        }

        Plotly.newPlot('chart1', data, layout);

    });
}