var x = 10;
var y = 10;
var player = rect(x,y,10,10);
var game = rect(0,540,80,50);
var red = color(255,0,0);
//var level = 1

function countPixels(array, value){
    var count = 0;
    for (var i=0; i < array.length; i++){
            if (array[i] == value){
                count +=1;
            }
        }
        return count;
    }

function makeLevel() {
  //blue rect
  background(0);
  fill(22,145,217);
  rect(0,540,80,50);

  //collision wall
  fill(100,74,34);
  rect(0,50,470,50);
  rect(30,150,490,50);
  rect(0,250,470,50);
  rect(30,350,490,50);
  rect(0,450,470,50);
  rect(70,540,470,50);
}

function player() {
  fill(255, 0, 0);
  rect(x, y, 10, 10);
}

function setup() {
  createCanvas(512, 590);
  makeLevel();
  player();
  loadPixels();//take snapshot of current canvas
  totalWall = countPixels(pixels, 100);
  totalBlue = countPixels(pixels, 217);
  totalRed = countPixels(pixels, 255);

}

function draw() {
  makeLevel();
  if (keyIsDown(LEFT_ARROW))
    x-=5;

  if (keyIsDown(RIGHT_ARROW))
    x+=5;

  if (keyIsDown(UP_ARROW))
    y-=5;

  if (keyIsDown(DOWN_ARROW))
    y+=5;

  player();

  //if(level == 1) {}

  loadPixels();
  if(countPixels(pixels, 100) < totalWall) {
  	x = 10;
  	y = 10;

  }

  else if(countPixels(pixels, 255) < totalRed) {
  	x = 10;
  	y = 10;
  }

  else if(countPixels(pixels, 217) < totalBlue){
  	//level += 1;
  }

//function makeLevel
}