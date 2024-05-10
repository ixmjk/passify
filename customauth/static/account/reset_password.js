import { showAlert } from "./alert.js";

document.getElementById("submitButton").onclick = function () {
  const uid = document.getElementById("uid");
  const token = document.getElementById("token");
  const new_password = document.getElementById("new_password");
  const re_new_password = document.getElementById("re_new_password");

  if (new_password.value === "" || re_new_password.value === "") {
    showAlert("Passwords cannot be empty.", "alert-danger");
    return;
  }

  if (new_password.value !== re_new_password.value) {
    showAlert("Passwords don't match.", "alert-danger");
    return;
  }

  if (new_password.value.length < 10) {
    showAlert("Password must be at least 10 characters long.", "alert-danger");
    return;
  }

  // Check if password contains at least one uppercase letter
  if (new_password.value.search(/[A-Z]/) < 0) {
    showAlert("Password must contain at least one uppercase letter.", "alert-danger");
    return;
  }

  // Check if password contains at least one lowercase letter
  if (new_password.value.search(/[a-z]/) < 0) {
    showAlert("Password must contain at least one lowercase letter.", "alert-danger");
    return;
  }

  // Check if password contains at least one digit
  if (new_password.value.search(/[0-9]/) < 0) {
    showAlert("Password must contain at least one digit.", "alert-danger");
    return;
  }

  // Check if password contains at least one special character
  if (new_password.value.search(/[!"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]/) < 0) {
    showAlert("Password must contain at least one symbol.", "alert-danger");
    return;
  }

  fetch(`${window.location.origin}/auth/users/reset_password_confirm/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      uid: uid.value,
      token: token.value,
      new_password: new_password.value,
      re_new_password: re_new_password.value,
    }),
  })
    .then((response) => {
      if (response.status === 204) {
        showAlert("Password has changed successfully!", "alert-success");
        new_password.value = "";
        re_new_password.value = "";
      } else {
        return response.json();
      }
    })
    .then((response) => {
      // Get all messages from the response
      const messages = Object.values(response).flat().join("<br>");
      showAlert(messages, "alert-danger");
    });
};
