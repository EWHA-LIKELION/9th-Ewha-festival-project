const collegeWrapper=document.querySelectorAll(".college-button-wrapper");
console.log(collegeWrapper);
for (let i=0; i<collegeWrapper.length;i++){
    collegeWrapper[i].addEventListener("click", handleClickCollege);
}
function handleClickCollege(e){
    e.stopPropagation();
    console.log(e.currentTarget.id)
    document.location.href='/festival/'+e.currentTarget.id;
}