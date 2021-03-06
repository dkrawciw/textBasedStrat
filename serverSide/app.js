const express = require("express"),
      fs = require("fs"),
      bodyParser = require("body-parser"),
      app = express();


app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: true}));

//Read and write text file
let getTxtFile = (fileName) => {
    return fs.readFileSync("public/" + fileName).toString();
}
let modifyFile = (fileName, data) => {
    fs.writeFileSync("public/" + fileName, data);
}

// Specifically get a json file
let getJson = (fileName) => {
    const JSONString = getTxtFile(fileName);
    return JSON.parse(JSONString);
}

// Actual web requests
app.get('/', (req, res) => {
    res.send("Hello, world!");
});

// Serve the guest text file via a directory
app.get('/getGuestList', (req, res) => {
    let guestList = getTxtFile("guestList.txt");
    res.send(guestList);
});

// Send a modification request to the server
app.post('/addMoneyTest', (req, res) => {
    let playerInformation = getJson("playerInformation.json");
    playerInformation.money++;
    modifyFile("playerInformation.json", JSON.stringify(playerInformation));
    res.redirect('/');
});

// Retrieve the guest list
// Add a person to the guest list
app.post('/addGuestList', (req, res) => {
    let dateTime = new Date();
    let currGuestList = getTxtFile("guestList.txt");

    currGuestList += req.body["name"] + "\n" + (dateTime.getMonth() + 1) + "-" + dateTime.getDate() + "-" + dateTime.getFullYear() + "\n";
    modifyFile("guestList.txt", currGuestList);
    res.redirect('/');
})

// Drop all of the data in the guestList Manually
app.get('/dropGuestList', (req, res) => {
    modifyFile("guestList.txt", "");
    res.redirect("/getGuestList");
})

app.get('*', (req, res) => {
    res.redirect("/");
});

app.listen(80, () => {
    console.log("Server Up 'n Running!");
});