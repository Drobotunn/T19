
const languageSelect = document.getElementById('language-select');

languageSelect.addEventListener('change', function() {
  const selectedValue = languageSelect.value;
  window.location.href = window.location.href + '?lang=' + selectedValue;
});