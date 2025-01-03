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

app.get('/', function (req, res) {
    res.render('pages/home')
});

//LINKS PAGE

app.get('/links', function (req, res) {
    //array with items to send
    var items = [
        { name: 'node.js', url: 'https://nodejs.org/en/' },
        { name: 'ejs', url: 'https://ejs.co' },
        { name: 'expressjs', url: 'https://expressjs.com' },
        { name: 'vuejs', url: 'https://vuejs.org' },
        { name: 'nextjs', url: 'https://nextjs.org' }];

    res.render('pages/links', {
        links: items
    })
});

//LIST PAGE (UC)

app.get('/investor', function (req, res) {
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

app.get('/transaction', function (req, res) {
    var apiurl = "http://127.0.0.1:5000/api/investor/all";
    axios.get(apiurl)
        .then((response) => {
            let investorArray = response.data.investors;
            let message = {};  // Define an empty message object or customize it as needed
            res.render('pages/transaction.ejs', {
                investorArray: investorArray,
                message: message  // Pass message object to the template
            });
        })
        .catch((error) => {
            console.error("Error fetching investor data:", error);
            res.status(500).send("Error fetching investor data");
        });
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

app.get('/stock', function (req, res) {
    //array with items to send
    var apiurl = "http://127.0.0.1:5000/api/stock/all";
    axios.get(apiurl)
        .then((response) => {
            let stockArray = response.data.stocks;
            res.render('pages/stock.ejs', {
                stockArray: stockArray,
            });
        })
        .catch((error) => {
            console.error("Error fetching investor data:", error);
            res.status(500).send("Error fetching investor data"); // More specific error
        });
});

app.post('/api/stock', (req, res) => {
    const { stockId } = req.body;
    if (!stockId) {
        return res.status(400).json({ message: 'stock ID is required' });
    }
    console.log(`Received stock ID: ${stockId}`);
    res.json({ message: `stock ID ${stockId} processed successfully!` });
});

app.get('/editstock', (req, res) => {
    res.render('pages/editstock'); // Render the base template for now
});

app.get('/createstock', (req, res) => {
    res.render('pages/createstock');
});

app.get('/bonds', function (req, res) {
    //array with items to send
    var apiurl = "http://127.0.0.1:5000/api/bond/all";
    axios.get(apiurl)
        .then((response) => {
            let bondArray = response.data.bonds;
            res.render('pages/bonds.ejs', {
                bondArray: bondArray,
            });
        })
        .catch((error) => {
            console.error("Error fetching investor data:", error);
            res.status(500).send("Error fetching investor data"); // More specific error
        });
});

app.post('/api/bond', (req, res) => {
    const { bondId } = req.body;
    if (!bondId) {
        return res.status(400).json({ message: 'bond ID is required' });
    }
    console.log(`Received bond ID: ${bondId}`);
    res.json({ message: `bond ID ${bondId} processed successfully!` });
});

app.get('/editbond', (req, res) => {
    res.render('pages/editbond'); // Render the base template for now
});

app.get('/createbond', (req, res) => {
    res.render('pages/createbond');
});

//our alert message midleware
function messages(req, res, next) {
    var message;
    res.locals.message = message;
    next();
}

app.listen(port, () => console.log(`MasterEJS app Started on port ${port}!`));
