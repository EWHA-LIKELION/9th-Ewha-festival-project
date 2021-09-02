const commentedPostListButton = document.getElementById('commented-post-list');
function handleCommentedPostListButtonClick() {
  console.log('commented-post-list clicked');
}
commentedPostListButton.addEventListener(
  'click',
  handleCommentedPostListButtonClick
);

const commentedBoothListButton = document.getElementById(
  'commented-booth-list'
);
function handleCommentedBoothListButtonClick() {
  console.log('commented-booth-list clicked');
}
commentedBoothListButton.addEventListener(
  'click',
  handleCommentedBoothListButtonClick
);

const likedBoothListButton = document.getElementById('liked-booth-list');
function handleLikedBoothListButtonClick() {
  console.log('liked-booth-list clicked');
}
likedBoothListButton.addEventListener('click', handleLikedBoothListButtonClick);
