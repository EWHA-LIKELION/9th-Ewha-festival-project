const headerButtons = document.querySelectorAll("#headerButtons");
for (let i = 0; i < headerButtons.length; i++) {
    headerButtons[i].addEventListener("click", function() {
        console.log("");
    });
}
const articleBox = document.querySelector("#articleBox");
function clickArticleBox() {
    console.log("");
}
articleBox.addEventListener("click", clickArticleBox);
const majorHashTag = document.querySelectorAll("#majorHashTag");
for (let i = 0; i < majorHashTag.length; i++) {
    majorHashTag[i].addEventListener("click", function() {
        console.log("");
    });
}