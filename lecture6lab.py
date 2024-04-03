"""
In this excercise, we will attempt to (sort of) simulate the Median Voter Theorm
model. It will require you to use all of the things we've learned in the last few
weeks. The aim is to bring everything together and give you a deeper understanding
of both programming and modeling.

The "position" of voters and politicians is represented by an integer from 1 to 100

No error handling is required for this excercise.

There are bonus problems at the end of this excercise should you want more
practice. Doing a large project is the best way to get comfortable with
programming.
"""

""""
1. Define a class named 'Politician', each instance of which will have the properties 
'name' and 'position', accepted as inputs. Then define a list named 'politicians' 
which will have two Politician objects, each with a name and an ideological position. 
Use the following names and positions: Alice has position 10, and Bob has position 70.

Hint: you'll be able to tell this works if 

print(politicians[0].name) # gives you Alice and
print(politicians[0].position) # gives you 10

"""


"""
2. Define a class called 'Voter'. The class should have a property named 
'preferred_point' that it will accept as an input. Then, in your main code,
define a list named 'voters'; this will be used to hold the voter objects.
Use a loop to create a set of 100 Voter objects with preferred_point values 
evenly distributed from 1 to 100. Thus, will be a voter 
with preferred_point = 1 and so on.

Hint: You should be able to test whether you've done this correctly if

print(voters[13].preferred_point) # gives you 14 and so on
"""


"""
3. Go back to the class Voter and create a method named 'will_vote_for()' that 
accepts a list of Politician objects as an input and returns the name 
of the politician with the position closest to that voter. 
Take the list of politicans as an input named 'politicians'

You can attempt this yourself as a challenge, or implement the steps below:

a. Create a variable called closest_politician whose initial value will be None
and a variable called smallest_distance whose initial value will be 200

b. Iterate over each object in politicians. For each politician, create a variable
called distance which measures the absolute distance between the politician and 
that voter. Hint: the code is 

distance = abs(self.preferred_point - politician.position)

c. Compare this distance to smallest_distance. If it's strictly smaller, 
replace smallest_distance with the distance, and closest_politician with the 
object being examined
"""


"""
4. Consider the following dictionary that will be used to keep a tally of which
politicians will get how many votes:

tally = {"Alice": 0, "Bob":0} 

Initially they are set at 0

Iterate over the voters object. For each voter, find the name of the politican
they will most likely vote for using the method you defined earlier. 
Then update that politician's value in the tally dictionary. 
Print tally. Who will win?
"""


"""
5. Our model is now ready to be played with ... er ... I mean used to generate
actionable insight.

Alice needs to reposition herself so that she isn't on the fringes. Find the
smallest value of position for Alice such that she will win the election. Do
so by manually modifiying the number that is currently 10 in the line where you
define Alice and rerun the code. Is she closer to winning? Repeat this until
she wins the election outright. 

Hint: it might be easier for you to read and modify the code in a separate window
if you copy-paste whatever work you have done thus far and remove the comments!

Bonus: what's the position that maximizes her tally?

This part will not be auto-graded
"""


"""
BONUS PROBLEMS

Bonus 1: What happens if we add a 3rd politician? Reset Alice to 10 and 
add a politician named "Coco" whose position is 70. Who is winning now?
What does this tell you about "splitting the vote"?
    
Bonus 2: You've probably spotted a problem with the algorithm in 3 - in case of 
a tie Alice always beats Bob just because her name was first!

To prevent this, use the shuffle command from the random package to randomize
the order of names in the politicians list before optimization.

Reference: https://www.w3schools.com/python/ref_random_shuffle.asp

Bonus 3: Create a function called find_winner that will take tally as an input
and return the name of the politician with the most votes. In case of a tie 
in the winner, it returns "Tie"

Bonus 4a: Let's automate the process of finding the optimal position. Using a loop
from 1 to 100, find the position that maximizes Alice's tally. Heads up - this
will require you to rewrite your code, moving the class and function definitions 
to the start of the code for ease of readability.

Bonus 4b: Let's move the process of finding the optimal position to a function
that takes in the following arguments: 

- voters (a list of instances of class Voter)
- politicians (a list of instance of class Politician)
- the name of a particular politician (a string)

and returns the position that *should* be occupied by the named politician to
maximize their tally. Does this work on Alice?

Bonus 4c: Update Alice's position based on the function in 4b. Then repeat
this excercise for Bob, then repeat the excercise for Alice and so on. Do
you see any convergence in their strategies

Bonus 4d: (very hard) Find the Nash Eqilibrium of these two agents.
To do so, automate 4c using a loop so each is taking turns optimizing their strategy
and this continues until niether would change their strategy. 
"""