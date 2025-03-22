import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

const width = 640;
const height = 400;
const marginTop = 20;
const marginRight = 20;
const marginBottom = 30;
const marginLeft = 40;

const x = d3
  .scaleUtc()
  .domain([new Date("2023-01-01"), new Date("2024-01-01")])
  .range([marginLeft, width - marginRight]);

const y = d3
  .scaleLinear()
  .domain([0, 100])
  .range([height - marginBottom, marginTop]);

const svg = d3.create("svg").attr("width", "auto").attr("height", "auto");

svg
  .append("g")
  .attr("transform", `translate(0,${height - marginBottom})`)
  .call(d3.axisBottom(x));

svg
  .append("g")
  .attr("transform", `translate(${marginLeft},0)`)
  .call(d3.axisLeft(y));

let me = document.querySelector('script[data-id="test"]');
me.parentElement.append(svg.node());
// document.currentScript.parentElement.append(svg.node());

// const el = document.querySelector("#test");
// el.append(svg.node());
