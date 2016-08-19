//setting variables for game mechanics
var ballX = 480;
var ballY = 270;
var xSpeed = 3;
var ySpeed = 3;
//var paddleX = 480;
var paddleY = 506.25;
var gameover = false;

//Setting variables and reference for storing data
var database = firebase.database().ref();
var score = 0;
//var TimesPlayed = 0;
//var phase = 1;

function setup() {
	createCanvas(960, 540);
	background(0);
}

function draw() {
	background(0);
	noStroke();
	fill(255);
	var ball = ellipse(ballX, ballY, 11.25, 11.25);
	var paddle = rect(mouseX, paddleY, 75, 7.5);
	ballX = ballX + xSpeed;
	ballY = ballY + ySpeed;

	//scoring
	textSize(11.25)
	fill(255)
	text(score, 3.75, 11.25)

	if(ballX < 7.5 || ballX > 952.5) {
		xSpeed = xSpeed * -1;
	}
	if(ballY < 7.5) {
		ySpeed = ySpeed * -1;
	}

	if(ballY >= paddleY){
		if(mouseX <= ballX <= (100 + mouseX)) {
			if(ballY > paddleY) {
				ySpeed = ySpeed * 1;
				gameover = true;
			}
			else {
				ySpeed = ySpeed * -1;
				score = score + 10;
			}
		}
	}
}

//function keyPressed() {
	//if(keyCode == 39 && paddleX > 37.5 && paddleX < 922.25) {
		//paddleX = paddleX + 10;
	//}
	//if(keyCode == 37 && paddleX > 37.5 && paddleX < 922.25) {
		//paddleX = paddleX - 10;
	//}
//}

