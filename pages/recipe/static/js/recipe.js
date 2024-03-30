window.onload = function () {
  const form = document.querySelector("#commentForm");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const comment = form.elements["comment"].value;
    if (comment.length === 0) alert("שגיאה! \nיש להכניס תגובה");
    else {
     form.submit();
    }

    return false;
  });
};