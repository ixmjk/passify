import { showAlert } from "./alert.js";

document.getElementById("submitButton").onclick = function () {
  const uid = document.getElementById("uid");
  const token = document.getElementById("token");

  fetch(`${window.location.origin}/auth/users/activation/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      uid: uid.value,
      token: token.value,
    }),
  })
    .then((response) => {
      if (response.status === 204) {
        showAlert(
          "Your account has been successfully activated!",
          "alert-success"
        );
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
