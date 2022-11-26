am4core.ready(function () {
    // am4core.useTheme(am4themes_animated);
    var chart = am4core.create("chartdiv", am4plugins_forceDirected.ForceDirectedTree);
    var series = chart.series.push(new am4plugins_forceDirected.ForceDirectedSeries());

    // Set data
    series.dataSource.url = "data/data.json";

    // Set up data fields
    series.dataFields.value = "value";
    series.dataFields.name = "name";
    series.dataFields.children = "children";
    series.dataFields.collapsed = "off";
    series.dataFields.color = "color";

    series.manyBodyStrength = -100;
    series.links.template.distance = 2;


    series.links.template.strokeWidth = 5;
    series.links.template.strokeOpacity = 0.7;

  //  series.dataFields.fixed = "fixed";


    series.nodes.template.events.on("hit", function(ev) {
        window.location = "?page=dataset/files/Physics/Part1%20Mechanics/Ch05%20The%20Laws%20of%20Motion.html"
        console.log(ev);

    }, this);


    // Add labels
    series.nodes.template.label.fill = "000000";
    series.nodes.template.label.text = "[bold]{name}";
    series.fontSize = 10;
    series.minRadius = 15;
    series.maxRadius = 40;
}); // end am4core.ready()