const backButton = document.getElementById("back-button");

function onClickBackButton(){
    console.log("Back button clicked");
}

backButton.addEventListener("click", onClickBackButton);


const homeButton = document.getElementById("home-button");

function onClickHomeButton(){
    console.log("Home button clicked");
}

homeButton.addEventListener("click", onClickHomeButton);


const signupForm = document.getElementById("signup-form");
const signupInputName = document.getElementById("signup-name");
const signupInputNickname = document.getElementById("signup-nickname");
const signupInputID = document.getElementById("signup-id");
const signupInputPW = document.getElementById("signup-pw");
const signupInputMail = document.getElementById("signup-mail");
const signupInputPhone = document.getElementById("signup-phone");

function onSignupSubmit(event){
    event.preventDefault();
    console.log("Signup Submit");
}

signupForm.addEventListener("submit", onSignupSubmit);