const mypageButton = document.getElementById("mypage-button");

function handleMyPageButtonClicked(){
    console.log("Mypage button clicked");
}

mypageButton.addEventListener("click", handleMyPageButtonClicked);


const searchWordInput = document.getElementById("search-word");

function onChangeSearchWordInput(){
    console.log("Search word input changed");
}

searchWordInput.addEventListener("input", onChangeSearchWordInput);


const departmentButton = document.getElementById("department-board");

function handleDepartmentButtonClicked(){
    console.log("Department button clicked");
}

departmentButton.addEventListener("click", handleDepartmentButtonClicked);


const centralCommitteeButton = document.getElementById("central-committee-board");

function handleCentralCommitteeButtonClicked(){
    console.log("Central Committee button clicked");
}

centralCommitteeButton.addEventListener("click", handleCentralCommitteeButtonClicked);


const boothButton = document.getElementById("booth-board");

function handleBoothButtonClicked(){
    console.log("Booth button clicked");
}

boothButton.addEventListener("click", handleBoothButtonClicked);

