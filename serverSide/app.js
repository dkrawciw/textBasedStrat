const express = require("express"),
      app = express();


app.use(express.static('public'))

app.get('/', (req, res) => {
    res.sendFile("index.html");
});

app.listen(8080, () => {
    console.log("Server Up 'n Running!");
});