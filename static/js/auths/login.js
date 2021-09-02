const signupButton = document.getElementById('signup-button');

function onClickSignupButton() {
  document.location.href = 'signup';
}

signupButton.addEventListener('click', onClickSignupButton);
