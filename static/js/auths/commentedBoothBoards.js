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