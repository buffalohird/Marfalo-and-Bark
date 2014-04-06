// Problem 2.  Random numbers

// TO-DO:  Expand on our HTML code for the task.
var page = createWebpageFromTemplate(
<div>Please pick a number from 1 to 10
    <img src='http://i.imgur.com/WPLAo.jpg' width="45%" alt="Image 1"></img>
    <img src='http://i.imgur.com/Sbkem.jpg' width="45%" alt="Image 1"></img>

<textarea style="width:350px;height:30px" name="newText">..</textarea>
<br></br>
 <input type="submit" value="Submit"></input>
</div>);

// TO-DO define the HIT parameters.
var hitParams = {
	title : "Pick-the-number", 
	description : "pick a number from the range 1 to 10", 
	url : page, 
	reward : 0.0,
	autoApprovalDelayInSeconds: 60,
	assignmentDurationInSeconds: 60,
	assignments: 5
}

// Create the HIT
var hit = mturk.createHIT(hitParams)
print("Hit created  : "+ hit)

//Report the results on the writeup
    