const searchButton = document.getElementById('search-button');
function handleSearchButtonClick() {
  console.log('search clicked');
}
searchButton.addEventListener('click', handleSearchButtonClick);

const themeHashtagButton = document.querySelectorAll('#theme-hashtag-button');
for (let i = 0; i < themeHashtagButton.length; i++) {
  themeHashtagButton[i].addEventListener('click', function () {
    console.log('hashtag button clicked');
  });
}

const likeBoothButton = document.querySelectorAll('#like-button');
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

const boothLabel = document.querySelectorAll('#booth-label');
for (let i = 0; i < boothLabel.length; i++) {
  boothLabel[i].addEventListener('click', function () {
    console.log('booth clicked');
  });
}
