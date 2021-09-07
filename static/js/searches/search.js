const postHeader = document.getElementById('post-header');
const boothHeader = document.getElementById('booth-header');
const header = document.querySelectorAll('.nav-header');
const postList = document.getElementById('post-container');
const boothList = document.getElementById('booth-container');

function changeSelectedHeader(event) {
  if (event.target.id === 'post-header') {
    postHeader.classList.add('active');
    boothHeader.classList.remove('active');
    postList.style.display = 'flex';
    boothList.style.display = 'none';
  } else {
    postHeader.classList.remove('active');
    boothHeader.classList.add('active');
    postList.style.display = 'none';
    boothList.style.display = 'flex';
  }
}

function init() {
  postList.style.display = 'flex';
  boothList.style.display = 'none';
}

header.forEach((nav) => nav.addEventListener('click', changeSelectedHeader));
init();