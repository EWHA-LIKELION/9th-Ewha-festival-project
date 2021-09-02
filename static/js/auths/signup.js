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