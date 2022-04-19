// Links
var biolinks = document.querySelector(`#bio-link`)
var edulinks = document.querySelector(`#edu-link`)
var hoblinks = document.querySelector(`#hob-link`)
var alllinks = document.querySelector(`#all-link`)


// Creating the variables.

var bio = document.querySelector(`bio`)
var edu = document.querySelector(`edu`)
var hob = document.querySelector(`hob`)

// Adding an a Event Listener

biolinks.addEventListener(`click`, showBio)
function showBio(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    bio.classList.remove(`hide`)
    edu.classList.add(`hide`)
    hob.classList.add(`hide`)
   

}

edulinks.addEventListener(`click`, showEdu)
function showEdu(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    
    edu.classList.remove(`hide`)
    bio.classList.add(`hide`)
    hob.classList.add(`hide`)
   

}

hoblinks.addEventListener(`click`, showHob)
function showHob(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    hob.classList.remove(`hide`)
    edu.classList.add(`hide`)
    bio.classList.add(`hide`)
   

}

alllinks.addEventListener(`click`, showAll)
function showAll(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    hob.classList.remove(`hide`)
    edu.classList.remove(`hide`)
    bio.classList.remove(`hide`)
   

}