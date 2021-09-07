const currentLocation = document.location.pathname.split('/');
const currentCollege = currentLocation[currentLocation.length - 2];

let tagList = [];
const TAG_LS = `${currentCollege}`;

const collegeName = document.getElementById('college-name');
collegeName.textContent = college[currentCollege];

function saveToLS() {
  localStorage.setItem(TAG_LS, JSON.stringify(tagList));
}

function loadSelectedTags() {
  const selectedTag = localStorage.getItem(TAG_LS);
  if (selectedTag !== null) {
    const parseTags = JSON.parse(selectedTag);
    parseTags.forEach((tag) => {
      tagList.push(tag);
      const collegeTag = document.getElementById(tag);
      collegeTag.classList.add(`${currentCollege}-hashtag-filled`);
    });
  }
  filterPosts();
}

const majorHashTag = document.querySelectorAll('.major-hashtag-item');
function handleHashtagClicked(event) {
  if (
    event.currentTarget.classList.value.indexOf(
      `${currentCollege}-hashtag-filled`
    ) === -1
  ) {
    event.currentTarget.classList.add(`${currentCollege}-hashtag-filled`);
    tagList.push(event.currentTarget.id);
  } else {
    event.currentTarget.classList.remove(`${currentCollege}-hashtag-filled`);
    tagList = tagList.filter((tag) => tag !== event.currentTarget.id);
  }
  saveToLS();
  filterPosts();
}
majorHashTag.forEach((hashtag) => {
  hashtag.addEventListener('click', handleHashtagClicked);
  hashtag.classList.add(`${currentCollege}-hashtag-outline`);
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
loadSelectedTags();

function filterPosts() {
  const filteredElement = document.querySelectorAll('.board-wrapper');
  const filterList = JSON.parse(localStorage.getItem(TAG_LS));
  if (filterList.length) {
    filteredElement.forEach((element) => {
      if (filterList.includes(element.className.split(' ')[1])) {
        element.style.visibility = 'visible';
      } else {
        element.style.visibility = 'hidden';
      }
    });
  } else {
    filteredElement.forEach((element) => {
      element.style.visibility = 'visible';
    });
  }
}
