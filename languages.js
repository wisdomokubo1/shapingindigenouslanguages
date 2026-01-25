// JavaScript code 

function search_language() { 

    let input = document.getElementById('searchbar').value 

    input=input.toLowerCase(); 

    let x = document.getElementsByClassName('languages'); 

      

    for (i = 0; i < x.length; i++) {  

        if (!x[i].innerHTML.toLowerCase().includes(input)) { 

            x[i].style.display="none"; 

        } 

        else { 

            x[i].style.display="list-item";                  

        } 

    } 
} 

// JavaScript code for English language template

function search_language() { 

    let input = document.getElementById('searchbar').value 

    input=input.toLowerCase(); 

    let x = document.getElementsByClassName('language'); 

      

    for (i = 0; i < x.length; i++) {  

        if (!x[i].innerHTML.toLowerCase().includes(input)) { 

            x[i].style.display="none"; 

        } 

        else { 

            x[i].style.display="list-item";                  

        } 

    } 
} 