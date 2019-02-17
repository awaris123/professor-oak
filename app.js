
var express = require('express');
var app = express();
var body = require('body-parser');
var path = require('path');

// Body Parser MiddleWare
app.use(body.json());
app.use(body.urlencoded({extended:false}));

// View Engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Set Static Path
app.use(express.static(path.join(__dirname, 'static')))

// Main Route
app.get('/', function (req, res) {

  res.render('index');

});


app.get('/generate', function(req, res){

  res.render('gen');

});

app.post('/show', function(req, res){

  var pref = {
    "HP":req.body.HP,
    "Atk": req.body.Attack,
    "Def": req.body.Defense,
    "SpAtk": req.body.SpAttack,
    "SpDef": req.body.SpDefense,
    "Spd": req.body.Speed,
  }

  const spawn = require("child_process").spawn;
  const pythonProcess = spawn('python',["pokemonpy.py", pref])
  pythonProcess.stdout.on('data', function(data) {
        console.log(data.toString());
      })


  console.log(pref)

  res.render("show")

});



app.listen(8080, function () {

  console.log('App listening on LocalHost:8080!');

});
