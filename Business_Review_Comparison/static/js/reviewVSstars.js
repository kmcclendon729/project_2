
//var newtry = "/api"
console.log("Hellow world!");
// console log 
d3.json("/api").then((response)=> {
  console.log(response);

var stars = []
var frequency = []

response.forEach((row)=>{
   stars.push(row.stars)
   frequency.push(row.review_count)
})

// Create the Trace
var trace = {
  x: stars,
  y: frequency,
  mode: "markers",
  type : "scatter"
};

// Create the data array for our plot
var data = [trace];


// Define our plot layout
var layout = {
  title: "Distribution of Number of Reviews and Ratings",
  xaxis: { title: "Star Ratings" },
  yaxis: { title: "Number of Reviews"}
};

Plotly.newPlot("plot", data, layout);

});

