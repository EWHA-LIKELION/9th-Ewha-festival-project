// 글 자세히 보기
const readMorePosts = document.querySelectorAll("#commented-posts");

function clickReadMorePost(){
    console.log("선택한 글 자세히 보기");
}

for(const readMorePost of readMorePosts){
    readMorePost.onclick = clickReadMorePost;
    }

