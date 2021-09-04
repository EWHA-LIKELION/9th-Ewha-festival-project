const majorHashTag = document.querySelectorAll('.major-hashtag-white');
function handleHashtagClicked(event) {
  console.log(event.target.id);
}
majorHashTag.forEach((hashtag) => {
  hashtag.addEventListener('click', handleHashtagClicked);
});

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
const currentCollege = document.location.pathname.split('/');
console.log(currentCollege[currentCollege.length - 2]);

const collegeName = document.getElementById('college-name');
collegeName.textContent = college[currentCollege[currentCollege.length - 2]];
