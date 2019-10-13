// Function to encode a string to base64 format
function encode(str) {
	encodedString = btoa(str);
    $scope.output.setValue(encodedString, 1);
}

// Function to decode a string from base64 format
function decode(str) {
    decodedString = atob(str);
    $scope.input.setValue(decodedString);
}

function SignIn() {
    const email = btoa(document.getElementById("email").value);
    const pwd = document.getElementById("password").value;
    location.href = '/signin?email=' + email + '&pwd=' + pwd;
}

function SignUp() {
    const email = btoa(document.getElementById("email").value);
    const pwd = document.getElementById("password").value;
    const cpwd = document.getElementById("cpassword").value;
    location.href = '/signup?email=' + email + '&pwd=' + pwd + '&cpwd=' + cpwd;
}

function AddPlan() {
    var plan = prompt("Enter your trip: ");
    location.href = '/plan?plan=' + plan;
}


