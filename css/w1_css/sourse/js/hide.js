// Links
var bio = document.querySelector(`#bio-link`)
var edu = document.querySelector(`#edu-link`)
var hob = document.querySelector(`#hob-link`)
var all = document.querySelector(`#all-link`)

// Divs
var biojs = document.querySelector(`#bio `)
var education = document.querySelector(`#education`)
var hobbies = document.querySelector(`#hobbies`)

// Functions

bio.addEventListener(`click`, showBio)
function showBio(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    biojs.classList.remove(`hide`)
    education.classList.add(`hide`)
    hobbies.classList.add(`hide`)
   

}

edu.addEventListener(`click`, showEdu)
function showEdu(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    
    education.classList.remove(`hide`)
    biojs.classList.add(`hide`)
    hobbies.classList.add(`hide`)
   

}

hob.addEventListener(`click`, showHob)
function showHob(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    hobbies.classList.remove(`hide`)
    education.classList.add(`hide`)
    biojs.classList.add(`hide`)
   

}

all.addEventListener(`click`, showAll)
function showAll(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    hobbies.classList.remove(`hide`)
    education.classList.remove(`hide`)
    biojs.classList.remove(`hide`)
   

}