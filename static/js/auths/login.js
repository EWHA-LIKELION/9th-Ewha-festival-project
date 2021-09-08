const signupButton = document.getElementById('signup-button');
function onClickSignupButton() {
  document.location.href = '/account/signup';
}
signupButton.addEventListener('click', onClickSignupButton);
