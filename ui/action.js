function SignIn() {
    const email = document.getElementById("email").value;
    const pwd = document.getElementById("password").value;
    location.href = '/signin?email=' + email + '&pwd=' + pwd;
}

function SignUp() {
    const email = document.getElementById("email").value;
    const pwd = document.getElementById("password").value;
    const cpwd = document.getElementById("cpassword").value;
    location.href = '/signup?email=' + email + '&pwd=' + pwd + '&cpwd=' + cpwd;
}
