
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var path = require('path');


// Body Parser MiddleWare
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));



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
  const spawn = require("child_process").spawn;
  const pythonProcess = spawn('python',["pokemonpy.py"])
  pythonProcess.stdout.on('data', function(data) {
        console.log(data.toString());
      } )
  var pref = {
    "HP":req.body.HP,
    "Atk": req.body.Attack,
    "Def": req.body.Defense,
    "SpAtk": req.body.SpAttack,
    "SpDef": req.body.SpDefense,
    "Spd": req.body.Speed
  }
  console.log(pref)
});



app.listen(8080, function () {
  console.log('App listening on LocalHost:8080!');
});
