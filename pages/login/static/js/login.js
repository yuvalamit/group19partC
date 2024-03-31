window.onload = function () {

    const form = document.querySelector("form");
    form.addEventListener("submit", (event) => {
        event.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (!email || !password || password.length < 6) {
            alert('יש למלא את כלל השדות להתחברות');
            return false; // prevent sent to server login
        }
        form.submit();
    });
};