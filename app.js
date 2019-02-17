
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

  console.log("hit /show");
  var roster = ""
  const spawn = require("child_process").spawn;
  const pythonProcess = spawn('python3',['./pokemonpy.py', pref["HP"], pref["Atk"], pref["Def"],pref["SpAtk"], pref["SpDef"], pref["Spd"]])
  pythonProcess.stdout.on('data', function(data) {
    // Do something with the data returned from python script
    // console.log(data + "node")
    var arr = Array.from(data.toString().split("-----------------------"))
    console.log(arr)
    counter = 0
    arr2 = []
    for (pk in arr){
      arr2[counter] = Array.from(arr[pk].split("|")).slice(1,4)

      counter += 1
    }

    console.log(arr2)
    arr = arr2
    res.render("show", {
      roster: arr
    })

  });



});

app.listen(8080, function () {

  console.log('App listening on LocalHost:8080!');

});
