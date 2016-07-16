from random import *

input("Welcome to MASH! Name's Lenovo, and I'm gonna be your game's host! Since I can only produce prompts at the moment, you'll have to move on to what else I'm programmed to say by typing whatever's in the little box and then clocking OK. So do that!") 
input("Hm, what is MASH, you ask? Well, MASH is a game where you can learn about what your life has in store for you!") 
input("A simple and random method will tell you whether you will live in your life in absolute luxury, where all your dreams come true...") 
input("...or if you'll just live a regular basic life like everybody else. Or worse. Could be anything, really!")
input("This method of fortune-telling madness works 100% OF THE TIME...none of the time. It's mind-blowing what elementary school kids can come up with these days.")
input("BUT ENOUGH WITH THE SEMANTICS! TELL ME, GOOD KIND SIR. Or madam. Or anywhere in between. Sorry, dont want to offend anyone right off the bat.")

nameInput = input("What's your name? Tell me by typing in the box!")
nameResponse = input("Splendid! Now I'm just gonna ask a bunch of questions. PAY ATTENTION! Your life will be determined by these! They will generate the random numbers that are the keys to your future! Oh, um, type anything in that lil box there and click OK to continue.")
houseInput = input("So, what kind of place do you want to live in? Could be anything, from a mansion to nothing at all!")
carInput = input("What car would you like to drive someday? Be bold and daring!")
childrenInput = input("How many chldren would you like to have? I have to ask this because humans apparently need to procreate. Not like there are 7 billion of them already.")
incomeInput = input("So, how much money would you like to make a month? Think very hardly and carefully! Or not.")
print("And now for the results of all that typing! Here we go! Let's test your luck! Grab any lucky charms if you need to!")

houseList = [houseInput + ". Congrats, you got what you wanted! Hope you're happy!", 
"a mansion. Ah, yes. You've got an amazing house to look forward to. You might just get lost in all its splendor and glory. Good job!",
"a shack. WELP. Shack isn't too bad. Least you're not homeless or living in a shelter.",
"an apartnemt. Congratulations! You are officially part of the working class. Just like the other 99%.", 
"a house. Nice and above average. Hope you dont have too many kids though. That'll be a fire hazard. But that's for me to determine!"]

carList = [carInput + ". Congrats, you got what you wanted! Hope you're happy!",
 "2016 Lamborghini Aventador. LUCKY BASTARD. Dang, man! You got the best one outta all of them!",
 "2017 Audi R8. Pretty good, man! Sweet car, too! Show it off!", 
 "2017 Ford Mustang. That's quite nice.", 
 "2016 Toyota Corolla. Heh, pretty average, man. Could be worse though!",
 "1971 Ford Pinto. One of the worst cars of all time. I dunno how you would get the car to begin with, but... Yeeeaaahhh....good luck with that."] 


childrenList = [childrenInput + ". Congrats, you got what you wanted! Hope you're happy!", 
"None. Either you and your wife just decided not to be sexually active to each other at all, or whenever you do, you've been painstakingly making sure to protect yourself.",
"one. That's neat! Sounds like a pretty manageable family!",  
"two. A typical American family. Be proud! You're really becoming part of this proud country of the USA. 'MURICA!", 
"sixty-eight. If you're trying to beat the record for the most children ever birthed by one person, you failed. The record is 69...heh heh. Seriously, look it up! And let that motivate you!",   
"two thousand, four hundred and twenty seven. Are...are you and your wife rabbits?"]


incomeList = [incomeInput + ". Congrats, you got what you wanted! Hope you're happy!", 
"$1,000 a month. Dude, that's...below poverty, man. I hope you get by. Unless you HAD money and then spent it, as determined to 100% accuracy by this game. In that case, it's your fault for being so reckless.",
"$10,000 a month. Barely enough to get by. Hope you survive, from me to you. Wait, I'm a computer, I cant have hope. Nevermind! Carry on!", 
"$100,000 a month. About a million a year. Welp, you're a millioniare. Just like you wanted to be. So freaking bad. That may or may not be a reference.", 
"$1,000,000 a month. WOAH, THATS A LOT OF MONEY. And yet it isn't. Only 12 million a year? People make BILLIONS, man! Work harder! And dont do anything illegal!"]

house = randrange(0, len(houseList))
car = randrange(0, len(carList))
children = randrange(0, len(childrenList))
income = randrange(0, len(incomeList))

print("The type of resedential establishment that you will be living in is", houseList[house])
print("The type of car that you will be driving in one say is a", carList[car])
print("The amount of children that you will have in your life is", childrenList[children])
print("You will make approximately or exactly", incomeList[income])