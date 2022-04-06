// Links
var bio = document.querySelector(`#bio-link`)
var edu = document.querySelector(`#edu-link`)
var hob = document.querySelector(`#hob-link`)
var all = document.querySelector(`#all-link`)

// Divs
var main = document.querySelector(`#main `)
var education = document.querySelector(`#education`)
var hobbies = document.querySelector(`#hobbies`)

// Functions

bio.addEventListener(`click`, showBio)
function showBio(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    main.classList.remove(`hide`)
    education.classList.add(`hide`)
    hobbies.classList.add(`hide`)
   

}

edu.addEventListener(`click`, showEdu)
function showEdu(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    
    education.classList.remove(`hide`)
    main.classList.add(`hide`)
    hobbies.classList.add(`hide`)
   

}

hob.addEventListener(`click`, showHob)
function showHob(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    hobbies.classList.remove(`hide`)
    education.classList.add(`hide`)
    main.classList.add(`hide`)
   

}

all.addEventListener(`click`, showAll)
function showAll(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    hobbies.classList.remove(`hide`)
    education.classList.remove(`hide`)
    main.classList.remove(`hide`)
   

}