const majorHashTag = document.querySelectorAll('#majorHashTag');
for (let i = 0; i < majorHashTag.length; i++) {
  majorHashTag[i].addEventListener('click', function () {
    console.log('major hashtag clicked');
  });
}

const collegePost = document.querySelectorAll('.board-wrapper');
collegePost.forEach((post) => {
  post.addEventListener('click', handlePostClicked);
});

//대학 링크도 가변적으로 수정해야함
function handlePostClicked(event) {
  event.stopPropagation();
  console.log(event.currentTarget);
  document.location.href = `${event.currentTarget.id.toString()}`;
}
