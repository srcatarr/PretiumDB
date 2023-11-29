// Setting constant variables

const express = require("express");
const app = express();

// Listening to port

app.listen(3000);

// Defining requests

app.use(express.static("static"));

console.log("Server launching at 3000 port");
console.log("http://localhost:3000");