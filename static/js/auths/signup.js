const backButton = document.querySelector("#back-button");

function onClickBackButton(){
    console.log("Back button clicked");
}

backButton.addEventListener("click", onClickBackButton);


const homeButton = document.querySelector("#home-button");

function onClickHomeButton(){
    console.log("Home button clicked");
}

homeButton.addEventListener("click", onClickHomeButton);


const signupForm = document.querySelector("#signup-form");
const signupInputName = document.querySelector("#signup-name");
const signupInputNickname = document.querySelector("#signup-nickname");
const signupInputID = document.querySelector("#signup-id");
const signupInputPW = document.querySelector("#signup-pw");
const signupInputMail = document.querySelector("#signup-mail");
const signupInputPhone = document.querySelector("#signup-phone");

function onSignupSubmit(event){
    event.preventDefault();
    console.log("Signup Submit");
}

signupForm.addEventListener("submit", onSignupSubmit);