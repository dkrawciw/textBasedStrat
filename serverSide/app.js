const express = require("express"),
      fs = require("fs"),
      app = express();


      app.use(express.static('public'));

let getJsonData = (fileName) => {
    return fs.readFileSync("public/" + fileName, {}, (err, data) => {
        if (err)
            console.log(err);
        else
            return data
    }).toString();
}

app.get('/', (req, res) => {
    res.send(getJsonData("playerInformation.json"));
});

app.get('*', (req, res) => {
    res.redirect("/");
});

app.listen(8080, () => {
    console.log("Server Up 'n Running!");
});