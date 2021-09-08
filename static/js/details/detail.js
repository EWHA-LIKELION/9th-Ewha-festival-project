// 사진 클릭
const pictures = document.querySelectorAll('#post-picture');

function handlePictureClicked() {
  console.log('사진 클릭');
}

for (const picture of pictures) {
  picture.onclick = handlePictureClicked;
}

// 댓글의 서머리 아이콘
const summaryIcons = document.querySelectorAll('#summary-icon');

function clickSummaryIcon() {
  console.log('댓글 sumarry 아이콘');
}

for (const summaryIcon of summaryIcons) {
  summaryIcon.onclick = clickSummaryIcon;
}

// //댓글 쓰기
// const commentInput = document.getElementById('comment-input');
// const commentSubmitBtn = document.getElementById('comment-submit-button');

// function commentSubmit(event) {
//   // console.log(commentInput.value);
//   let content=commentInput.value;
//   event.preventDefault();
//   let param={
//     'pk_id': '{{post.pk}}',
//     'content':content,
//   }
//   console.log(param);
//   $.ajax({
//     url:`${currentCollege}/{{post.pk}}`,
//     type:'POST',
//     headers:{
//       'X-CSRFTOKEN':'{{csrf_token}}',
//     },
//     data:JSON.stringify(param),
//     success:function(data){
//       console.log(data);
//     },
//     error:function(e){
//       console.log('error');
//       console.log({{post.pk}});
//     }

//   })
//   //commentInput.value = '';
// }

// commentSubmitBtn.onclick = commentSubmit;

const headerName = document.getElementById('header-name');
const currentPosition = document.location.pathname.split('/');
const currentCollege = currentPosition[currentPosition.length - 2];
console.log(currentCollege);
headerName.textContent = college[currentCollege];
const collegeTag = document.getElementById('college-tag');
collegeTag.classList.add(`${currentCollege}-hashtag-filled`);
