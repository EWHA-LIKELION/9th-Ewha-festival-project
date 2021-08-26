const backButton = document.querySelector("#back-button");

function onClickBackButton(){
    console.log("Back button clicked");
}

backButton.addEventListener("click", onClickBackButton);


const loginButton = document.querySelector("#login-button");

function onClickLoginButton(){
    console.log("Login button clicked");
}

loginButton.addEventListener("click", onClickLoginButton);


const signupButton = document.querySelector("#signup-button");

function onClickSignupButton(){
    console.log("Signup button clicked");
}

signupButton.addEventListener("click", onClickSignupButton);

