
function start() {
    console.log("game started");
    window.location.href = "{{url_for('templates', filename='endgame.html')}}";
}
  
  function testHand() {
      return ['a', 'b', 'c', 'd', 'e', 'f'];
  }
