// Problem 4. Sort images

var pictures = ["WPLAo.jpg","Sbkem.jpg","SzBIk.jpg","ZiusC.jpg", "r53qG.jpg","RNfpa.jpg","XcGBz.jpg","YdL3d.jpg"]

// TO-DO: Add "http://i.imgur.com/"    at the beginning of every picture id
pictures = pictures.map(function(x){return "http://i.imgur.com/"+x});

//  Creates a webpage of two images side-by-side
function getPicsPage(pic1, pic2) {

var text=  "Which picture comes before the other chronologically? (Type 'Left' or 'Right')"

// TO-DO:   Expand on our HTML design. Do you think a different design could better?
// Provide evidence.
var webpage = createWebpageFromTemplate(<div>
        <img src={pic1} width="45%" alt="Image 1"></img>
	   <img src={pic2}  width="45%" alt="Image 2"></img>
        <ul>
            <li>People will vote whether to approve your work.</li>
        </ul>
        <textarea style="width:500px;height:50px" name="newText">{text}</textarea>
        <input type="submit" value="Submit"></input>
    </div>);

default xml namespace = "http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd";
    var q = <QuestionForm>
        <Question>
            <QuestionIdentifier>IdNuclei</QuestionIdentifier>
            <IsRequired>true</IsRequired>
            <QuestionContent>
                <FormattedContent><![CDATA[

<img src="http://i.imgur.com/WPLAo.jpg" width="45%" alt="Nuclei"></img>
<img src="http://i.imgur.com/Sbkem.jpg" width="45%" alt="Nuclei"></img>

]]></FormattedContent>
            </QuestionContent>
            <AnswerSpecification>
                <FreeTextAnswer>
                    <Constraints>
                    </Constraints>
                    <NumberOfLinesSuggestion>1</NumberOfLinesSuggestion>
                </FreeTextAnswer>
            </AnswerSpecification>
        </Question>
    </QuestionForm>

	return q;
}
// Returns True if pic1 before pic2

function comparePics(pic1, pic2) {
    var webpage = getPicsPage(pic1, pic2);

    var h = {title : "Compare Two Pictures", 
        desc : "Decide which photo was taken earlier", 
        question: webpage,
        reward : 0.05,
        assignments : 5}

    var hit = mturk.createHIT(h)

    var voteResults = mturk.vote(hit, function (answer) {return (answer.bestOption) })

    print(voteResults.toLowerCase());
    voteResults = voteResults.toLowerCase();
    // if there is not l in the string, answer must have been right, return false
    if(voteResults.indexOf('l') === -1) 
        return false;
    else 
        return true;

}

// Adapted insertion sort algorithm from Wikipedia: http://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort#JavaScript
function insertionSort (a) {
    for (var i = 0; i < a.length; i++) {
        var k = a[i];
        for (var j = i; j > 0 && comparePics(k, a[j - 1]); j--)
            a[j] = a[j - 1];
        a[j] = k;
    }
    return a;
}

sorted_pics = insertionSort(pictures)

// TO-DO : Create a comparison HIT


// TO-DO: Expand code to order all provided images.