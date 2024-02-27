
document.getElementById("registerForm").addEventListener("submit", function (event) {
    var passwordInput = document.getElementById("password");
    var password = passwordInput.value;
    if (!/\d/.test(password)) {
        document.getElementById("passwordError").innerText = "Password must contain at least one digit";
        event.preventDefault();
    } else if (!/[A-Z]/.test(password)) {
        document.getElementById("passwordError").innerText = "Password must contain at least one uppercase letter";
        event.preventDefault();
    } else if (password.length < 8) {
        document.getElementById("passwordError").innerText = "Password must be at least 8 characters long";
        event.preventDefault();
    }
});
