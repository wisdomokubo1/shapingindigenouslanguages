// JavaScript code 

function search_nigerianlanguage() { 

    let input = document.getElementById('searchbarnigeria').value 

    input=input.toLowerCase(); 

    let x = document.getElementsByClassName('nigerianlanguages'); 

      

    for (i = 0; i < x.length; i++) {  

        if (!x[i].innerHTML.toLowerCase().includes(input)) { 

            x[i].style.display="none"; 

        } 

        else { 

            x[i].style.display="list-item";                  

        } 

    } 
} 

// JavaScript code for Degema Language
function search_degemalanguage() { 

    let input = document.getElementById('searchbardegema').value 

    input=input.toLowerCase(); 

    let x = document.getElementsByClassName('degemalanguage'); 

      

    for (i = 0; i < x.length; i++) {  

        if (!x[i].innerHTML.toLowerCase().includes(input)) { 

            x[i].style.display="none"; 

        } 

        else { 

            x[i].style.display="list-item";                  

        } 

    } 
} 