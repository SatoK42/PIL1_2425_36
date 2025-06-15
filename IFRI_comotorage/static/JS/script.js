const input = document.querySelector("#phone");
  const iti = window.intlTelInput(input, {
    initialCountry: "bj",
    nationalMode: false,
    separateDialCode: false,
    formatOnDisplay: true,
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.17/js/utils.js"
  });

  // Avant l'envoi, on remplace la valeur par le numéro complet
  input.closest("form").addEventListener("submit", function(e) {
    if (!iti.isValidNumber()) {
      e.preventDefault();
      alert("Numéro invalide !");
    } else {
      input.value = iti.getNumber();  // +225XXXXXXXXX
    }
  });