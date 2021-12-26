function timer() {
    var counter = 4;
    var myTimer = setInterval(function() {
      document.getElementById("timer").innerHTML = counter;
      counter--;
      if (counter < 0) {
        clearInterval(myTimer);
        document.getElementById("timer").style.color = "red";
  
        // do anything then time is up. 
        window.location.href = "endgame"
      }
    }, 1000);
  }
  timer();