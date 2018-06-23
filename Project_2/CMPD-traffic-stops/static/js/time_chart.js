function renderTimeChart() {
    Plotly.d3.json("/data_timechart"+getCurrentFilterParams(), function (error, response) {
        var $timeDiv = document.getElementById("time_chart")

        var data_entries = unpack(response, 0)
        var data_counts = unpack(response, 1)
        var data_counts_category = unpack(response, 2)

        $timeDiv.innerHTML = "<p>" + String(data_entries).replace(/,/g, ", ") +
            "</p><p>" + String(data_counts).replace(/,/g, ", ") +
            "<p><p>" + String(data_counts_category).replace(/,/g, ", ");
    });
}