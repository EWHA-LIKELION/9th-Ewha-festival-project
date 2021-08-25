// 헤더의 뒤로가기 버튼
const goBackIcon = document.getElementById("go_back_icon");

function clickGoBackIcon(){
    console.log("뒤로가기 버튼 클릭");
}

goBackIcon.onclick = clickGoBackIcon;

// 사진 클릭
const picture = document.getElementById("gallery")

function clickGallery(){
    console.log("갤러리 클릭");
}
picture.onclick = clickGallery;

// 댓글의 서머리 아이콘
const summaryIcons = document.querySelectorAll("#summary-icon");

function clickSummaryIcon(){
    console.log("댓글 sumarry 아이콘");
}

for(const summaryIcon of summaryIcons){
    summaryIcon.onclick = clickSummaryIcon;
}

// 댓글 쓰기 
const commentInput = document.getElementById("comment-input");
const commentSubmitBtn = document.getElementById("comment-submit-button");

function commentSubmit(event){
    console.log(commentInput.value); 
    commentInput.value = ""; 
}

commentSubmitBtn.onclick = commentSubmit;