// Setting constant variables

const express = require("express");
const app = express();

// Listening to port

app.listen(3000);

// Defining requests

app.static(__dirname + "../static");

app.get("/api:version", (req, res) => void {});