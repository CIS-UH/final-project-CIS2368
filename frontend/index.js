const express = require('express')
var path = require('path');
var bodyParser = require('body-parser');
const { default: axios } = require('axios');
const app = express();
const port = 3000;
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
//setup public folder
app.use(express.static('./public'));
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
// parse application/json
app.use(bodyParser.json());

app.get('/',function (req, res) {
    res.render('pages/home')
});

//LINKS PAGE

app.get('/links',function (req, res) {
    //array with items to send
    var items = [
        {name:'node.js',url:'https://nodejs.org/en/'},
        {name:'ejs',url:'https://ejs.co'},
        {name:'expressjs',url:'https://expressjs.com'},
        {name:'vuejs',url:'https://vuejs.org'},
        {name:'nextjs',url:'https://nextjs.org'}];

    res.render('pages/links',{
        links:items
    })
});

//LIST PAGE (UC)

app.get('/investor',function (req, res) {
    //array with items to send
    var apiurl = "http://127.0.0.1:5000/api/investor/all";
    axios.get(apiurl)
        .then((response) => {
            let investorArray = response.data.investors;
            res.render('pages/investor.ejs', {
                investorArray: investorArray,
            });
        })
        .catch((error) => {
            console.error("Error fetching investor data:", error);
            res.status(500).send("Error fetching investor data"); // More specific error
        });
        
   // var items = ['node.js','expressjs','ejs','javascript','bootstarmie'];
    //res.render('pages/list',{
     //   list:items
    //})
});

app.get('/portfolio', (req, res) => {
    res.render('pages/portfolio'); // Render the base template for now
});

app.get('/editinvestor', (req, res) => {
    res.render('pages/editinvestor'); // Render the base template for now
});

app.get('/createinvestor', (req, res) => {
    res.render('pages/createinvestor');
});





app.post('/api/investor', (req, res) => {
    const { investorId } = req.body;
    if (!investorId) {
        return res.status(400).json({ message: 'Investor ID is required' });
    }
    console.log(`Received Investor ID: ${investorId}`);
    res.json({ message: `Investor ID ${investorId} processed successfully!` });
});

//TABLE PAGE

app.get('/table',function (req, res) {
    //array with items to send
    var items = [
        {name:'node.js',url:'https://nodejs.org/en/'},
        {name:'ejs',url:'https://ejs.co'},
        {name:'expressjs',url:'https://expressjs.com'},
        {name:'vuejs',url:'https://vuejs.org'},
        {name:'nextjs',url:'https://nextjs.org'}];

    res.render('pages/table',{
        table:items
    })
});

//our alert message midleware
function messages(req,res,next){
    var message;
    res.locals.message = message;
    next();
}

//FORM PAGE

app.get('/form',messages,function (req, res) {
    res.render('pages/form');
});

app.post('/form',function (req, res) {
    var message=req.body;
    res.locals.message = message;
    res.render('pages/form');
});

app.listen(port, () => console.log(`MasterEJS app Started on port ${port}!`));
