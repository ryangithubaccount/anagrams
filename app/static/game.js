function timer() {
    var counter = parseInt(document.getElementById("timer").textContent) - 1;
    var myTimer = setInterval(function() {
      document.getElementById("timer").innerHTML = counter;
      counter--;
      if (counter < 5) {
        document.getElementById("timer").style.color = "red";
      }
      if (counter < 0) {
        clearInterval(myTimer);
        
        // do anything then time is up. 
        window.location.href = "endgame"
      }
    }, 1000);
  }
  timer();