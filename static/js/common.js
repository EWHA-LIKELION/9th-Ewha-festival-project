/*뒤로가기 버튼*/
const backButton = document.getElementById('back-button');
function handleBackButtonClick() {
  console.log('뒤로가기 클릭');
  window.history.back();
}
backButton ? backButton.addEventListener('click', handleBackButtonClick) : '';

/*홈버튼*/
const homeButton = document.getElementById('home-button');
function handleHomeButtonClick() {
  window.location.href = '/';
}
homeButton ? homeButton.addEventListener('click', handleHomeButtonClick) : '';

/* 검색버튼 */
const searchButton = document.getElementById('search-button');
function handleSearchButtonClick() {
  console.log('search clicked');
  document.location.href = '/festival/search';
}
searchButton
  ? searchButton.addEventListener('click', handleSearchButtonClick)
  : '';

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
  committee: '중앙운영위원회',
};
document.documentElement.addEventListener(
  'touchstart',
  function (event) {
    if (event.touches.length > 1) {
      event.preventDefault();
    }
  },
  false
);

var lastTouchEnd = 0;

document.documentElement.addEventListener(
  'touchend',
  function (event) {
    var now = new Date().getTime();
    if (now - lastTouchEnd <= 300) {
      event.preventDefault();
    }
    lastTouchEnd = now;
  },
  false
);
