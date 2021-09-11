const likeBoothButton = document.getElementById('like-button-icon');
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
likeBoothButton.addEventListener('click', handleLikeButtonClicked);

const collegeTag = document.getElementById('college-tag');
collegeTag.classList.add('booth-hashtag-filled');
// 댓글의 신고 아이콘
const summaryIcons = document.querySelectorAll('#summary-icon');

function clickSummaryIcon() {
  console.log('1');
  window.location.href =
    'https://docs.google.com/forms/d/1XfP9Mgii0t1BJ-ZwvIz8zDFbN4jJ2YFIQIYPYkqdaLs/';
}

summaryIcons.forEach((report) =>
  report.addEventListener('click', clickSummaryIcon)
);
