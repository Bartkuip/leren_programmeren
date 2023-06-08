
fruitLijst = ['strawberry', 'banana', 'apple', 'raspberry', 'pear', 'grape', 'orange', 'apricot', 'lychee', 'cherry'];
fruitLijstBottom = ['strawberry', 'banana', 'apple', 'raspberry', 'pear', 'grape', 'orange', 'apricot', 'lychee', 'cherry'];
fruitLijst = shuffle(fruitLijst);
fruitLijstBottom = shuffle(fruitLijstBottom);
currentCardTop = "";
currentCardBottom = "";



function shuffle(array){
    let currentIndex = array.length, randomIndex;
    while (currentIndex != 0){
        randomIndex = Math.floor(Math.random() * currentIndex)
        currentIndex--;
        [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }
    return array;
}

for (let i = 0; i < 10; i++) {
    var button = document.createElement('button');
    button.memoryNameTop = fruitLijst[i];
    button.src = "background.png";
    var images = document.getElementById("images");
    images.appendChild(button);
    button.id = "buttonTop" +i;
    button.addEventListener("click", function() {
        document.getElementById("buttonTop" +i).style.backgroundImage = "url('"+ fruitLijst[i] +".jpg')"; 
        currentCardTop = fruitLijst[i];
        
      });
}


for (let x = 0; x < 10; x++) {
    var button = document.createElement('button');
    button.memoryNameBottom = fruitLijst[x];
    button.src = "background.png";
    var images = document.getElementById("images");
    images.appendChild(button);
    button.id = "buttonBottom" +x;
    button.addEventListener("click", function() {
        document.getElementById("buttonBottom" +x).style.backgroundImage = "url('"+ fruitLijstBottom[x] +".jpg')";
        currentCardBottom = fruitLijstBottom[x];
        if (currentCardTop == currentCardBottom ){
            console.log("klopt")
        } else {
            document.getElementById("buttonBottom" +x).style.backgroundImage = "url('"+ fruitLijstBottom[x] +".jpg')";
            setTimeout(function(){
                document.getElementById("buttonBottom" +x).style.backgroundImage = "url('background.png')";
              }, 1000);
            
        }
      });
}








