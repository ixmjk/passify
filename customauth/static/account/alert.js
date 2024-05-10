export function showAlert(alertMessage, alertType) {
  let alertElement = document.getElementById("alertMessage");
  alertElement.classList.remove("alert-success", "alert-danger");
  alertElement.classList.add("alert", alertType);
  alertElement.innerHTML = alertMessage;
}
