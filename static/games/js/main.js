var str1= prompt('Please enter Player1 name');

var str2= prompt('Please enter Player2 name');



// $('td').eq(30).css('background-color','blue')
var player1 = {
  name:str1,
  color:'#42d9f4',
  playing:true,
  lastPos:0

}



var player2 = {
  name:str2,
  color:'#f441b5',
  playing:false,
  lastPos:0

}


var positions = []
for (var i =0; i<42;i++){
  positions.push(0);
}


function chkWinnerH(){


  for ( var i=0;i<positions.length -3;i++){
    var a=positions[i];
    var b=positions[i+1];
    var c=positions[i+2];
    var d=positions[i+3];

     var row1=Math.floor(i/7);
     var row2=Math.floor((i+3)/7);

    if(a!==0 && a === b && a === c && a===d && row1===row2){


      return true;
    }

  }
  return false;
}

function chkWinnerV(){


  for ( var i=0;i<positions.length -21;i++){
    var a=positions[i];
    var b=positions[i+7];
    var c=positions[i+14];
    var d=positions[i+21];



    if(a!==0 && a === b && a === c && a===d ){


      return true;
    }

  }
  return false;
}

function chkWinnerD(){


  for ( var i=0;i<positions.length -24;i++){
    var a=positions[i];
    var b=positions[i+8];
    var c=positions[i+16];
    var d=positions[i+24];

    if(a!==0 && a === b && a === c && a===d ){


      return true;
    }
   }


   for ( var i=0;i<positions.length -18;i++){
     var a=positions[i];
     var b=positions[i+6];
     var c=positions[i+12];
     var d=positions[i+18];

     if(a!==0 && a === b && a === c && a===d ){


       return true;
     }
    }

   return false;
}



var clr1='#42d9f4';
var clr2='#f441b5';



$('h3')[0].textContent=player1["name"] + ": it is your turn now" ;

  var clr=clr1;

for ( var i=0;i < 42;i++){

  $('td').eq(i).click(function() {

    var col=$(this)[0].cellIndex;
    console.log(col);

    var j= col + 35;


    while (positions[j]!==0 && j >=0) {
      j=j-7;}
      if( j>0){
          $('td').eq(j).css('background-color',clr);


          if(player1.playing===true){
            $('h3')[0].textContent=player2["name"] + ": it is your turn now"
            clr=clr2;
            player2.playing=true;
            player1.playing=false;
            positions[j]=1;
            if(chkWinnerV() || chkWinnerH() || chkWinnerD()){
              alert(player1["name"] + ' you are the winner');
            }
            console.log('***player1**');
          }else{
            $('h3')[0].textContent=player1["name"] + ": it is your turn now"
            clr=clr1;
            player2.playing=false;
            console.log('***player2**');
            player1.playing=true;
            positions[j]=2;

            if(chkWinnerH() && chkWinnerV() || chkWinnerD()){
              alert(player2["name"] + ' you are the winner');
            }
          }

      }



      })


}
