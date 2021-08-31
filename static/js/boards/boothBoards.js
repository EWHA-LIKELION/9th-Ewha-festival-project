const backButton=document.getElementById('back-button')
function handleBackButtonClick(){
    console.log("go-back clicked");
}
backButton.addEventListener("click", handleBackButtonClick);

const searchButton=document.getElementById('search-button')
function handleSearchButtonClick(){
    console.log("search clicked");    
}
searchButton.addEventListener("click", handleSearchButtonClick);

const themeHashtagButton=document.querySelectorAll("#theme-hashtag-button");
for (let i = 0; i < themeHashtagButton.length; i++) {
    themeHashtagButton[i].addEventListener("click", function() {
        console.log("hashtag button clicked");
    });
}

const likeBoothButton=document.querySelectorAll("#like-button");
for (let i = 0; i < likeBoothButton.length; i++) {
    likeBoothButton[i].addEventListener("click", function() {
        console.log("like button clicked");
    });
}

const boothLabel=document.querySelectorAll("#booth-label");
for (let i = 0; i < boothLabel.length; i++) {
    boothLabel[i].addEventListener("click", function() {
        console.log("booth clicked");
    });
}