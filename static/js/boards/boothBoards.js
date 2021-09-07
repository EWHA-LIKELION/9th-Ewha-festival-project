const currentLocation = document.location.pathname.split('/');
const currentUrl = currentLocation[1];

let tagList = [];
const TAG_LS = `${currentUrl}`;

function saveToLS() {
  localStorage.setItem(TAG_LS, JSON.stringify(tagList));
}

function loadSelectedTags() {
  const selectedTag = localStorage.getItem(TAG_LS);
  if (selectedTag !== null) {
    const parseTags = JSON.parse(selectedTag);
    parseTags.forEach((tag) => {
      tagList.push(tag);
      const boothTag = document.getElementById(tag);
      boothTag.classList.add(`${currentUrl}-hashtag-filled`);
    });
  }
  filterPosts();
}

function filterPosts() {
  const filteredElement = document.querySelectorAll('.booth-list-wrapper');
  const filterList = JSON.parse(localStorage.getItem(TAG_LS));
  if (filterList && filterList.length) {
    filteredElement.forEach((element) => {
      if (filterList.includes(element.className.split(' ')[1])) {
        element.style.visibility = 'visible';
      } else {
        element.remove();
      }
    });
  } else {
    filteredElement.forEach((element) => {
      element.style.visibility = 'visible';
    });
  }
}

const themeHashtagButton = document.querySelectorAll('.major-hashtag-item');
themeHashtagButton.forEach((tag) => {
  tag.addEventListener('click', handleBoothTagClicked);
  tag.classList.add(`${currentUrl}-hashtag-outline`);
});

function handleBoothTagClicked(event) {
  location.reload();
  if (
    event.currentTarget.classList.value.indexOf(
      `${currentUrl}-hashtag-filled`
    ) === -1
  ) {
    event.currentTarget.classList.add(`${currentUrl}-hashtag-filled`);
    tagList.push(event.currentTarget.id);
  } else {
    event.currentTarget.classList.remove(`${currentUrl}-hashtag-filled`);
    tagList = tagList.filter((tag) => tag !== event.currentTarget.id);
  }
  saveToLS();
  filterPosts();
}

const likeBoothButton = document.querySelectorAll('#like-button-icon');
for (let i = 0; i < likeBoothButton.length; i++) {
  likeBoothButton[i].addEventListener('click', handleLikeButtonClicked);
}

function handleLikeButtonClicked(event) {
  if (event.target.src) {
    if (event.target.src.indexOf('empty') !== -1) {
      event.target.src = event.target.src.replace('empty', 'filled');
    } else {
      event.target.src = event.target.src.replace('filled', 'empty');
    }
  } else {
    if (event.srcElement.innerHTML.indexOf('empty') !== -1) {
      event.srcElement.innerHTML = event.srcElement.innerHTML.replace(
        'empty',
        'filled'
      );
    } else {
      event.srcElement.innerHTML = event.srcElement.innerHTML.replace(
        'filled',
        'empty'
      );
    }
  }
}

const boothPosts = document.querySelectorAll('.booth-list-wrapper');
boothPosts.forEach((booth) => {
  booth.addEventListener('click', handlePostClicked);
});

function handlePostClicked(event) {
  if (event.target.id === '') {
    console.log('page move!');
    document.location.href = `${event.currentTarget.id}`;
  }
}
loadSelectedTags();
