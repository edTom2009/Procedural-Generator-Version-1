function hidePassword() {
  var password = document.getElementById("password");
  
  password.addEventListener("click", () => {
    password.type = "password";
    password.value = "";
  });
  if (!password) return;
}

hidePassword();