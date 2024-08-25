function toggleFields() {
    var option = document.getElementById("options").value;
    document.getElementById("logoFields").style.display = option === 'logo' ? 'block' : 'none';
    document.getElementById("textFields").style.display = option === 'text' ? 'block' : 'none';
}

window.onload = function() {
    toggleFields();  // Ensure correct fields are displayed on load
}