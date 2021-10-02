d3.json("clean_data_analyst.json").then(function(data) {
    console.log(data[0]);
  });
//function displaySampleData(ID) {
    //console.log ("Display data", ID); 

    //d3.json("clean_data_analyst.json").then ((data) => {

        //var metadata = data.metadata; 

        //var result = metadata.find(o => o.id == ID);
        //console.log(result); 

        //handle on the sample metadata DOM element
        //var demTable = d3.select("#sample-metadata");

        // clear the table for each section 
        //demTable.html("");

        //display data
        //for(var key in result){
            //demTable.append('h6').text(key + ": " + result[key]);
//   }
   // });
//}




//Create Bar Chart
function createBarChart(id) {
    console.log("createBarChart", id)
    d3.json("clean_data_analyst.json").then((data) => {
    
        var traceBar = {
            x: titles.slice(0, 10).reverse(),
            y: yticks,
            text: "max",
            type: "bar",
            orientation: "v",
        };

        var dataBar = [traceBar];

        var layoutBar = {
            title: "Top 10 Salaries",
        };

        //Plot Bar Chart
        Plotly.newPlot("bar", dataBar, layoutBar);
        var bubbleChart = d3.select("bubble");
    });
};
//Reset Data
function optionChanged(newID) {
    displaySampleData(newID);
    createBarChart(newID); 
    createBubbleChart(newID);
};
var selector = d3.select("#selDataset");

d3.json ("clean_data_analyst.json").then ( (data) => {
    var names = data.names; 
    names.forEach(function (name){
        selector.append('option').text(name).property('value', name);
    });
    var selectedID = names[0];
    displaySampleData(selectedID);
    createBarChart(selectedID); 
    createBubbleChart(selectedID);
});