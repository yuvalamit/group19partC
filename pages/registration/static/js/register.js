window.onload = function () {
    const form = document.querySelector("#regiform");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        let errors = ["שגיאה!"];

        const password = form.elements["password"].value;
        if (!passValid(password)) {
            errors.push('"a-z", "A-Z" סיסמא חייבת להכיל לפחות 10 תווים ואותיות');
        }
        if (!PassConfirm(password, form.elements["confirm_password"].value)) {
            errors.push("סיסמאות אינן תואמות");
        }

        if (!emailValid(form.elements["email"].value)) {
            errors.push("אימייל לא תקין");
        }

        if (errors.length > 1) {
            alert(errors.join("\n"));
        } else {
            form.submit();
        }
        return false;
    });

    function passValid(password) {
        if (password.length >= 10) {
            if (/[a-zA-Z]/.test(password))
                //checks minimum one letter
                return true;
        }
        return false;
    }

    function PassConfirm(password, confPass) {
        if (password === confPass) return true;
        return false;
    }

    function emailValid(mail) {
        return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
            mail
        );

    }
};