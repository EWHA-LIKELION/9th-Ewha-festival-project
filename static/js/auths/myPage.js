const commentedPostListButton=document.getElementById('commented-post-list-button')
function handleCommentedPostListButtonClick(){
    console.log("commented-post-list clicked");
}
commentedPostListButton.addEventListener("click", handleCommentedPostListButtonClick);

const commentedBoothListButton=document.getElementById('commented-booth-list-button')
function handleCommentedBoothListButtonClick(){
    console.log("commented-booth-list clicked");
}
commentedBoothListButton.addEventListener("click", handleCommentedBoothListButtonClick);

const likedBoothListButton=document.getElementById('liked-booth-list-button')
function handleLikedBoothListButtonClick(){
    console.log("liked-booth-list clicked");
}
likedBoothListButton.addEventListener("click", handleLikedBoothListButtonClick);