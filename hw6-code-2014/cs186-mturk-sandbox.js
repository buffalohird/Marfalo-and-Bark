print("Hello World")
print("Your balance is: " + mturk.getAccountBalance())

// Problem 2.  Random numbers

// TO-DO:  Expand on our HTML code for the task.
var page = createWebpageFromTemplate(
<div>Please pick a number from 1 to 10
<textarea style="width:350px;height:30px" name="newText">..</textarea>
<br></br>
 <input type="submit" value="Submit"></input>
</div>);

// TO-DO define the HIT parameters.
var hitParams = {
	title: "Pick a number",
	desc: "Just Pick one",
	url: page,
	reward: 0.0,
	autoApprovalDelayInSeconds: 60,
	assignments: 5, 
	assignmentDurationInSeconds: 60,
}

// Create the HIT
var hit = mturk.createHIT(hitParams)
print("Hit created  : "+ hit)

//Report the results on the writeup