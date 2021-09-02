const commentedPostListButton = document.getElementById('commented-post-list');
function handleCommentedPostListButtonClick() {
  document.location.href = '/';
  //link 아직 없음
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
  document.location.href = '/';
  //link 아직 없음
}
commentedBoothListButton.addEventListener(
  'click',
  handleCommentedBoothListButtonClick
);

const likedBoothListButton = document.getElementById('liked-booth-list');
function handleLikedBoothListButtonClick() {
  console.log('liked-booth-list clicked');
  document.location.href = '/';
  //link 아직 없음
}
likedBoothListButton.addEventListener('click', handleLikedBoothListButtonClick);
