const goBackButton = document.getElementById("goback-button");
function handleGoBackButtonClicked() {
    console.log("goback button clicked");
}
goBackButton.addEventListener("click", handleGoBackButtonClicked);

const homeButton = document.getElementById("home-button");
function handleHomeButtonClicked() {
    console.log("home button clicked");
}
homeButton.addEventListener("click", handleHomeButtonClicked);

const articleBox = document.getElementById("articleBox");
function handleArticleBoxClicked() {
    console.log("article box clicked");
}
articleBox.addEventListener("click", handleArticleBoxClicked);

const majorHashTag = document.querySelectorAll("#majorHashTag");
for (let i = 0; i < majorHashTag.length; i++) {
    majorHashTag[i].addEventListener("click", function() {
        console.log("major hashtag clicked");
    });
}