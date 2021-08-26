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


const loginForm = document.querySelector("#login-form");
const loginInputID = document.querySelector("#login-id-form input");
const loginInputPW = document.querySelector("#login-pw-form input");
//const loginSubmitButton = document.querySelector("#login-submit-form button");

function onLoginSubmit(event){
    event.preventDefault();
    console.log("Login Submit");
}

loginForm.addEventListener("submit", onLoginSubmit);


const signupButton = document.querySelector("#signup-button");

function onClickSignupButton(){
    console.log("Signup button clicked");
}

signupButton.addEventListener("click", onClickSignupButton);



