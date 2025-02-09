/**
 * Created by diogopedrosa on 3/10/15.
 */
"use strict";

ready(function () {
  $("form").on("submit", function (event) {
    if (checkPass()) event.preventDefault();
    if (passwordForce() < 20 && $("#id_new_password1").val()) {
      showErrorMessageTemporary(
        gettext(
          "Password must contain at least 8 characters, including at least one uppercase letter, digit or special character."
        )
      );
      event.preventDefault();
    }
  });
});
