const studentCardImg=document.getElementById("student-card");
const preview=document.querySelector(".preview");
studentCardImg.style.opacity=0;
function updateImageDisplay() {
    while(preview.firstChild) {
      preview.removeChild(preview.firstChild);
    }
    const curFiles = studentCardImg.files;
    if(curFiles.length === 0) {
      const para = document.createElement('p');
      para.textContent = '현재 선택된 파일이 없습니다.';
      preview.appendChild(para);
    } 
    else {
      for(const file of curFiles) {
        const para = document.createElement('p');
        para.textContent = `${file.name}`;
        const image = document.createElement('img');
        image.src = URL.createObjectURL(file);
        preview.appendChild(para);
      }
    }
  }
studentCardImg.addEventListener('change', updateImageDisplay);
// function onSignupSubmit(event){
//     event.preventDefault();
//     console.log("Signup Submit");
// }

// signupForm.addEventListener("submit", onSignupSubmit);