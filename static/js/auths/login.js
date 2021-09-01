const loginForm = document.getElementById("login-form");
const loginInputID = document.querySelector("#login-id-form input");
const loginInputPW = document.querySelector("#login-pw-form input");
//const loginSubmitButton = document.querySelector("#login-submit-form button");

function onLoginSubmit(event){
    event.preventDefault();
    console.log("Login Submit");
}

loginForm.addEventListener("submit", onLoginSubmit);


const signupButton = document.getElementById("signup-button");

function onClickSignupButton(){
    console.log("Signup button clicked");
}

signupButton.addEventListener("click", onClickSignupButton);



