const mypageButton = document.getElementById("mypage-button");

function onClickMypageButton(){
    console.log("Mypage button clicked");
}

mypageButton.addEventListener("click", onClickMypageButton);


const searchWordInput = document.getElementById("search-word");

function onChangeSearchWordInput(){
    console.log("Search word input changed");
}

searchWordInput.addEventListener("input", onChangeSearchWordInput);


const departmentButton = document.getElementById("department-board");

function onClickDepartmentButton(){
    console.log("Department button clicked");
}

departmentButton.addEventListener("click", onClickDepartmentButton);


const centralCommitteeButton = document.getElementById("central-committee-board");

function onClickCentralCommitteeButton(){
    console.log("Central Committee button clicked");
}

centralCommitteeButton.addEventListener("click", onClickCentralCommitteeButton);


const boothButton = document.getElementById("booth-board");

function onClickBoothButton(){
    console.log("Booth button clicked");
}

boothButton.addEventListener("click", onClickBoothButton);

