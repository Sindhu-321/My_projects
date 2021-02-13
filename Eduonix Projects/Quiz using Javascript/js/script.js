function submitAnswers(){
    var total=5;
    var score=0;

//get user input
    var q1=document.forms["quizForm"]["q1"].value;
    var q2=document.forms["quizForm"]["q2"].value;
    var q3=document.forms["quizForm"]["q3"].value;
    var q4=document.forms["quizForm"]["q4"].value;
    var q5=document.forms["quizForm"]["q5"].value;

    //validation
    
    for(var i=1; i<=5;i++){
    
        if(eval('q'+i)==null|| eval('q'+i)==''){
            alert('Please Select question '+i+"!")
            return false;
        }

    }

    //set answers using array
    var answers=["a","a","d","b","d"];
    //check answers

    for(var i=1;i<=5;i++){
        if(eval('q'+i)==answers[i-1]){
            score++;
        }
    }
//Display result
    var result=document.getElementById('results');
    result.innerHTML='<h3>You scored <span>'+score+'</span> out of <span>'+total+'</span><h3>'

    alert("Your Score: "+score+"/"+total)

    

    
    return false;//stops submission to server

}