import { showAlert } from "./alert.js";

function validateEmail(email) {
  let regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

document.getElementById("submitButton").onclick = function () {
  const uid = document.getElementById("uid");
  const token = document.getElementById("token");
  const new_email = document.getElementById("new_email");
  const re_new_email = document.getElementById("re_new_email");

  if (new_email.value === "" || re_new_email.value === "") {
    showAlert("Email field cannot be empty.", "alert-danger");
    return;
  }

  if (new_email.value !== re_new_email.value) {
    showAlert("Emails don't match.", "alert-danger");
    return;
  }

  if (!validateEmail(new_email.value)) {
    showAlert("Enter a valid email address.", "alert-danger");
    return;
  }

  fetch(`${window.location.origin}/auth/users/reset_email_confirm/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      uid: uid.value,
      token: token.value,
      new_email: new_email.value,
      re_new_email: re_new_email.value,
    }),
  })
    .then((response) => {
      if (response.status === 204) {
        showAlert("Email has changed successfully!", "alert-success");
        new_email.value = "";
        re_new_email.value = "";
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
