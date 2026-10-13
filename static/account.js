function setupPlaceholderField(inputId, placeholderText, isPassword = false) {
  var input = document.getElementById(inputId);

  if (!input) return;

  input.value = placeholderText;
  input.dataset.hasTyped = "false";

  input.addEventListener("focus", () => {
    if (input.dataset.hasTyped !== "true" && input.value === placeholderText) {
      input.value = "";
    }

    if (isPassword) {
      input.type = "password";
    }
  });

  input.addEventListener("input", () => {
    input.dataset.hasTyped = "true";
  });

  input.addEventListener("blur", () => {
    if (input.dataset.hasTyped !== "true") {
      input.value = placeholderText;

      if (isPassword) {
        input.type = "text";
      }
    }
  });
}

setupPlaceholderField("username", "Username");
setupPlaceholderField("password", "Password", true);