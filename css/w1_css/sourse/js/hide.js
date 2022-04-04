// Links
var bio = document.querySelector(`#bio`)
var edu = document.querySelector(`#edu`)
var hob = document.querySelector(`#hobbies`)

// Divs
var main = document.querySelector(`#main `)
var education = document.querySelector(`#education`)
var hobbies = document.querySelector(`#hobbies`)

bio.addEventListener(`click`,showBio )
function showBio(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    edu.classList.remove(`hide`)
    hob.classList.add(`hide`)
   

}

edu.addEventListener(`click`,showEdu )
function showEdu(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    bio.classList.remove(`hide`)
    hob.classList.add(`hide`)
   

}

hob.addEventListener(`click`,showHob )
function showHob(e)
{
    //keeps link from navigating to another URL
    e.preventDefault()
    edu.classList.remove(`hide`)
    bio.classList.add(`hide`)
   

}