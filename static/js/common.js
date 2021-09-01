/*뒤로가기 버튼*/
const backButton=document.getElementById('back-button')
function handleBackButtonClick(){
    console.log("뒤로가기 클릭");
}
backButton.addEventListener("click", handleBackButtonClick);

/*홈버튼*/
const homeButton=document.getElementById('home-button')
function handleHomeButtonClick(){
    console.log("홈버튼 클릭");
}
backButton.addEventListener("click", handleHomeButtonClick);