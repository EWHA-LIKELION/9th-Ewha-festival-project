// 헤더의 뒤로가기 버튼
const goBackButton = document.getElementById("go-back-button");

function clickGoBackButton(){
    console.log("뒤로가기 버튼 클릭");
}

goBackButton.onclick = clickGoBackButton;

// 글 자세히 보기
const readMorePosts = document.querySelectorAll("#commented-posts");

function clickReadMorePost(){
    console.log("선택한 글 자세히 보기");
}

for(const readMorePost of readMorePosts){
    readMorePost.onclick = clickReadMorePost;
    }

