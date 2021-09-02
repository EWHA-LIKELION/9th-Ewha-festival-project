/*뒤로가기 버튼*/
const backButton = document.getElementById('back-button');
function handleBackButtonClick() {
  console.log('뒤로가기 클릭');
  window.history.back();
}
backButton ? backButton.addEventListener('click', handleBackButtonClick) : '';

/*홈버튼*/
const homeButton = document.getElementById('home-button');
function handleHomeButtonClick() {
  window.location.href = '/';
}
homeButton ? homeButton.addEventListener('click', handleHomeButtonClick) : '';

/* 검색버튼 */
const searchButton=document.getElementById('search-button')
function handleSearchButtonClick(){
    console.log("search clicked");    
    document.location.href="/festival/search";
}
searchButton ? searchButton.addEventListener("click", handleSearchButtonClick):'';
