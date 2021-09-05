const likeBoothButton = document.getElementById('like-button');
function handleLikeButtonFilled(event) {
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
likeBoothButton.addEventListener('click', handleLikeButtonClicked);

const goBackButton = document.getElementById('go-back');
goBackButton.addEventListener('click', handleGoBackButtonClicked);
function handleGoBackButtonClicked() {
  window.history.back();
}
