const main = document.querySelector('main')
const search = document.querySelector("#search")





// Event listeners
search.addEventListener('input', filterItems)



// FUNCTIONS
function filterItems(event){
  // Saving user text for comparing
  const text = event.target.value.toLowerCase();
  
  const subjects = main.querySelectorAll('h2')
  // console.log(subjects)

  subjects.forEach(subject => {
    const subjectName = subject.firstChild.textContent.toLowerCase()
    
    if((subjectName.indexOf(text)) != -1){
      console.log()
      subject.parentElement.parentElement.style.display = 'block'
    }
    else{
      console.log('not found')
      subject.parentElement.parentElement.style.display = 'none'
    }
    
  })
}