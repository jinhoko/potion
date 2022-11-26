am4core.ready(function () {
    // am4core.useTheme(am4themes_animated);
    var chart = am4core.create("chartdiv", am4plugins_forceDirected.ForceDirectedTree);
    var series = chart.series.push(new am4plugins_forceDirected.ForceDirectedSeries())

    // Set data
    series.dataSource.url = "data/data.json";

    // Set up data fields
    series.dataFields.value = "value";
    series.dataFields.name = "name";
    series.dataFields.children = "children";
    series.dataFields.collapsed = "off";

    // Add labels
    series.nodes.template.label.text = "{name}";
    series.fontSize = 10;
    series.minRadius = 15;
    series.maxRadius = 40;
}); // end am4core.ready()