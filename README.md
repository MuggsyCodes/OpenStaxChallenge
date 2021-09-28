# OpenStaxChallenge
OpenStax interview practical exercise
Completing in response to the OpenStax interview practial exercise - completed by Charles Avila


*********** README.md instructions ******************
** Please run the main.py file to play the Opportunity with Every Roll game **

Notes regarding OER program: 
* I have comments in all files including the original refactoring_exercise.py file
* Important: Please keep in mind that I kept a LOT of commented code in tact so that you could better understand my 'sausage making process'
* In production code, I wouldn't leave so much in there

* My intent with game was two fold: 
1. Improve the mechanics of the existing code so that someone else looking at the code base could fairly easily figure out what is going on. I tried to accomplish this by:  
(I) Splitting up original Game class into two main classes Questions and Player in order to add modularity
(II) Removing redundant code
(III) Reducing a few functions by combining more functionality into others
(Iv) Improving inefficiencies like lots of if statements with switch statements 

2. Create a more fun user experience seeing how it's a game
(I) Added amazing ASCII art graphics at beginning when user is prompted 
(II) Incorporated actual questions for each category 
(III) Slowed down game play a bit
(IV) Added a score class and methods to provide 'live' updates and keep track of winners
(VI) Ability to add more than six players and choose from a player list


Things that did not quite work, but with more time should be doable:  
* Error handling when questions are exhausted 
- this is easily remedied by simply addding more questions based on the number of players
* Tried to use a wrapper function - not necessary, but perhaps a good approach 
- used nested functions instead
* Tried to use recursion to prompt user to play game over again
- I couldn't end the game how I wanted it 
* Keeping track of more game play metrics like number of wins per player
- Just ran out of time and didn't want to spend more time on minutae
* Full fledged unittesting 
- Used the VSCode debugger and in-line print statements in the separate Class files
- this works OK, but I know I plan to really get a handle on QA/QC testing when I'm part of the OpenStax Dev Team :-)








*********** Original README.md instructions ******************


OpenStax Refactoring Exercise
Overview
Welcome to the Refactoring Exercise! You are very close to the final phase of the interviewing process.

We ask that you read the instructions in full before beginning the assignment. The importance of the assignment is that you are able to demonstrate clearly your technical excellence. No frameworks or other dependencies are required, but if you wish to include libraries that will help that is fine. The choice of development environment is up to you. You should plan on spending several hours on the assignment and committing your changes as you work. The total time is up to you but we do expect the exercise to be turned in within a couple days.

Review the code closely and think about how you would improve the code. There is no ONE right answer to the exercise. When refactoring this code think about how you can include tests to reduce the risks of your changes. We are VERY interested in how you would write tests to help you refactor this code. Feel free to take notes along the way.

If you run out of time, focus on your overall implementation and stub out whatever classes and methods you have left. Place comments/docstrings, where necessary, and explain how they should work. Once you feel you have completed the assignment send the url of the GitHub repository for further review.

The code does not have to run! We'll assume that the time will exist to work out bugs and make it eventually run.

We will review your code and let you know the next steps. Be prepared to explain your decisions.

Instructions
This assignment requires you to create a GitHub repository (and account if you don't have one) and committing your changes as you work through the assignment. You can commit whenever you feel it is necessary. Our advice is that you "commit early and often." We're interested in your process of working through this problem (aka sausage making).

Create a repository on GitHub with the refactoring_exercise.py file below as an initial commit. You can name the repository however you like.
Start coding!
Commit along the way until you are happy with the result.
Send the URL of your GitHub to who sent you here =).
?
PROFIT
refactoring_exercise.py
