const collegeWrapper=document.querySelectorAll(".college-button-wrapper");
console.log(collegeWrapper);
for (let i=0; i<collegeWrapper.length;i++){
    collegeWrapper[i].addEventListener("click", handleClickCollege);
}
function handleClickCollege(e){
    console.log(e.target.id)
    document.location.href='/festival/'+e.target.id;
}