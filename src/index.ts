// Setting constant variables

const express = require("express");
const app = express();
const fs = require("fs");

// Listening to port

app.listen(3000);

// Defining requests

app.get("/", (req, res) => {})

app.get("/api", (req, res) => {})

app.get("/api:req", (req, res) => {})


console.log("Server launching at 3000 port");
console.log("http://localhost:3000");