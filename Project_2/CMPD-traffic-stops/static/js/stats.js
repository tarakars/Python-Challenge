function renderStats(data) {
    var $statsDiv = document.getElementById("stats")

    stats_str="<h1 class=display-4>"+data+" Stops in"+"</h1><p class=font-weight-light style:color:blue>";
    stats_str+=division_filter.replace(/ /g, "&nbsp;");
    if(division_filter == "")  stats_str+="All Divisions".replace(/ /g, "&nbsp;");
    stats_str+=", ";

    stats_str+=reason_filter.replace(/ /g, "&nbsp;");
    if(reason_filter == "")  stats_str+="All Reasons".replace(/ /g, "&nbsp;");
    stats_str+=", ";

    stats_str+=result_filter.replace(/ /g, "&nbsp;");
    if(result_filter == "")  stats_str+="All Results".replace(/ /g, "&nbsp;");
    stats_str+=", ";

    stats_str+=year_filter.replace(/ /g, "&nbsp;");
    if(year_filter == "")  stats_str+="All Years".replace(/ /g, "&nbsp;");
    stats_str+="</p>";

    $statsDiv.innerHTML = stats_str;
  }