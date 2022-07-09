

var restart = document.querySelector('#b');

let symbol='X'

// Grab all the squares
var squares = document.querySelectorAll("td");


// Clear Squares Function
function clearBoard() {


  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }
  symbol='X'




}
restart.addEventListener('click',clearBoard)


// Create a function that will check the square marker
function changeMarker(){

  
    if(this.textContent === ''){

      if(symbol==='X'){
        this.textContent = 'X';
        symbol='O'

      }else if(symbol==='O'){
        this.textContent = 'o';
        symbol='X'}
 
    }
    chkWinner();
    
};




function chkWinner(){

  let sym=[];
  
  let val = squares[0].textContent+squares[1].textContent+squares[2].textContent;
  sym.push(val);

   val = squares[3].textContent+squares[4].textContent+squares[5].textContent;
   sym.push(val);
   
  val = squares[6].textContent+squares[7].textContent+squares[8].textContent;
  sym.push(val);
  val = squares[0].textContent+squares[3].textContent+squares[6].textContent;
  sym.push(val);
  val = squares[1].textContent+squares[4].textContent+squares[7].textContent;
  sym.push(val);
  val = squares[2].textContent+squares[5].textContent+squares[8].textContent;
  sym.push(val);
  val = squares[0].textContent+squares[4].textContent+squares[8].textContent;
  sym.push(val);
  val = squares[2].textContent+squares[4].textContent+squares[6].textContent;
  sym.push(val);


    for ( let i=0; i< sym.length ;i++){
     

      if(sym[i]==='XXX' || sym[i]==='ooo'){
        alert('You are the winner::'+sym[i][0]);
      }

    }

  }
  



// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changeMarker);
}
