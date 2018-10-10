function changePar() {
    var x, y;
    x = 5;
    y = 6;
    z = x + y;
    document.getElementById("changeable").innerHTML =
      "Paragraph changed to "+z+".";
}
function populateDiv() {
  parToShow = "<h2>Populated!</h2><p>Ahi ch'a dir qual era è cosa dura</p>"
  document.getElementById("d-container").innerHTML = parToShow
}
var benji = {
  name: "Benji",
  iq: 12,
  height: 175,
  weight: 999,
  sayHi: function() {
    return "Hi, I am"+this.name+"!";
  }
}
function printBenji() {
  document.getElementById("benjipar").innerHTML =
    benji.sayHi()+
    "<br>"+
    "Benji is "+benji.iq+", is "+benji.height+" cm tall and weighs "+
    benji.weight+" kg.";
  document.getElementById("benji-button").style.display = "none";
}
