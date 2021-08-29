const A=document.getElementById=("collegebutton")
function aa(event){
    event.preventDefault();
    console.log(event.srcElement);
}
A.addEventListener('click', aa);