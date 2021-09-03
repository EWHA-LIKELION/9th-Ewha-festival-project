const college = {
  humanities: '인문과학대학',
  social: '사회과학대학',
  natural: '자연과학대학',
  engineering: '엘텍공과대학',
  music: '음악대학',
  art: '조형예술대학',
  edu: '사범대학',
  business: '경영대학',
  convergence: '신산업융합대학',
  nursing: '간호대학',
  scraton: '스크랜튼대학',
  hokma: '호크마교양대학',
  pharmacy: '약학대학',
};
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
