const mypageButton = document.getElementById('mypage-button');

function handleMyPageButtonClicked() {
  console.log('Mypage button clicked');
  document.location.href = 'account/mypage';
}

mypageButton.addEventListener('click', handleMyPageButtonClicked);

const departmentButton = document.getElementById('department-board');

function handleDepartmentButtonClicked() {
  console.log('Department button clicked');
  document.location.href = '/festival';
}

departmentButton.addEventListener('click', handleDepartmentButtonClicked);

const centralCommitteeButton = document.getElementById(
  'central-committee-board'
);

function handleCentralCommitteeButtonClicked() {
  console.log('Central Committee button clicked');
  document.location.href = '/committee/committee';
}

centralCommitteeButton.addEventListener(
  'click',
  handleCentralCommitteeButtonClicked
);

const boothButton = document.getElementById('booth-board');

function handleBoothButtonClicked() {
  console.log('Booth button clicked');
  document.location.href = '/booth';
}

boothButton.addEventListener('click', handleBoothButtonClicked);
