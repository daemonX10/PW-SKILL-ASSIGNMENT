// Function to check if password and confirm password fields match
const checkPassword = () => {
    // Get password and confirm password values
    let password = document.getElementById('password').value;
    let confirmPass = document.getElementById('Cn-Password').value;

    // Log password and confirm password values
    console.log("password", password, '\n', "confirmPass", confirmPass);

    // Get message element
    let message = document.getElementById('message');

    // Check if password is not empty
    if (password.length != 0) {
        // If password and confirm password match
        if (password === confirmPass) {
            // Set message text and background color
            message.textContent = "Password Match";
            message.style.backgroundColor = "#1dcd59";
        }
        // If password and confirm password don't match
        else {
            // Set message text and background color
            message.textContent = "Password don't match";
            message.style.backgroundColor = "#ff4d4d";
        }
    }
    // If password is empty
    else {
        // Show alert and set message background color
        alert("Password can't be empty!");
        message.style.backgroundColor = "#F70000";
    }
}