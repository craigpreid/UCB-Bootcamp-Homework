function buildMetadata(sample) {
    var defaultURL = `metadata/${sample}`;
    d3.json(defaultURL).then(function(data){
      var PANEL = d3.select("#sample-metadata");
      PANEL.html("");
      Object.entries(data).forEach(function([key, value]){
        PANEL.append('span').text(`${key}: ${value}`);
        PANEL.append('br');
      });
    })
  }
  
function buildCharts(sample) {
  var sample_url = `samples/${sample}`;

  d3.json(sample_url).then(function(data){

      // TOP Ten Values --> 
      // Use slice() to grab the top 10 sample_values,
      // otu_ids, and labels (10 each).

      var topTenOtuIds = data.otu_ids.slice(0,10);
      var topTenOtuLabels = data.otu_labels.slice(0,10);
      var topTenSampleValues = data.sample_values.slice(0,10);

      // Create the Bubble Chart
      var BubbleChartTraceData =  [{
        x: data.otu_ids,
        y: data.sample_values,
        mode: 'markers',
        text: data.otu_labels,
        marker: {
          color: data.otu_ids,
          size: data.sample_values
        }
      }];

      var BubbleChartLayout = {
      hovermode:'closest',
      title:'Bubble Chart',
      xaxis:{zeroline:false, title: 'OTU ID'},
      yaxis:{zeroline:false, title: 'Sample Values'}
      };

      // Create the Pie Chart
      var PieChartTraceData = [{
        "labels": topTenOtuIds,
        "values": topTenSampleValues,
        "hovertext": topTenOtuLabels,
        "type": "pie"
      }];

      // Plot the pie chart and the bubble chart
      Plotly.newPlot('pie', PieChartTraceData);
      Plotly.newPlot('bubble',BubbleChartTraceData, BubbleChartLayout);
  })
}

function buildWfreq(sample) {
  var wfreqURL = `/wfreq/${sample}`;

  d3.json(wfreqURL).then(function(data) {
    var wfreq = parseInt(data.WFREQ);

    meterLevel = wfreq * 20;

    // Trig to calc meter point
    var degrees = 180 - meterLevel,
        radius = .5;
    var radians = degrees * Math.PI / 180;
    var x = radius * Math.cos(radians);
    var y = radius * Math.sin(radians);
    
    // Path: may have to change to create a better triangle
    var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
        pathX = String(x),
        space = ' ',
        pathY = String(y),
        pathEnd = ' Z';
    var path = mainPath.concat(pathX,space,pathY,pathEnd);
    
    var data = [
        { 
            type: 'scatter',
            x: [0], 
            y:[0],
            marker: {size: 28, color:'850000'},
            showlegend: false,
            name: 'scrubs',
            text: wfreq,
            hoverinfo: 'text+name'
        },
        { 
            values: [50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50],
            rotation: 90,
            text: ['8-9', '7-8', '6-7', '5-6', '4-5', '3-4', '2-3', '1-2', '0-1', ''],
            textinfo: 'text',
            textposition:'inside',
            marker: {
                colors:[ 'rgba(14, 127, 0, .5)',
                            'rgba(14, 127, 0, .5)', 'rgba(14, 127, 0, .5)',
                            'rgba(14, 127, 0, .5)', 'rgba(110, 154, 22, .5)',
                            'rgba(170, 202, 42, .5)', 'rgba(202, 209, 95, .5)',
                            'rgba(210, 206, 145, .5)', 'rgba(232, 226, 202, .5)',
                            'rgba(255, 255, 255, 0)']
                    },
            labels: ['8-9', '7-8', '6-7', '5-6', '4-5', '3-4', '2-3', '1-2', '0-1', ''],
            hoverinfo: 'label',
            hole: .5,
            type: 'pie',
            showlegend: false
        }
    ];

    var layout = {
        shapes:[{
            type: 'path',
            path: path,
            fillcolor: '850000',
            line: {
                color: '850000'
            }
        }],
        title: 'Belly Button Washing Frequency',
        xaxis: {zeroline:false, showticklabels:false,
                    showgrid: false, range: [-1, 1]},
        yaxis: {zeroline:false, showticklabels:false,
                    showgrid: false, range: [-1, 1]}
    };
    Plotly.newPlot('gauge', data, layout);  
  })
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
    buildWfreq(firstSample);
  });
}
  
function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
  buildWfreq(newSample);
}

// Initialize the dashboard
init();