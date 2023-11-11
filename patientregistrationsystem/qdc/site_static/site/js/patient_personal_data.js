/**
 * Created by diogopedrosa on 3/18/15.
 */

"use strict";
document.addEventListener("DOMContentLoaded", () => {
  var original_name = $("#id_name").val();
  var original_cpf = $("#id_cpf").val();
  var anonymous = $("#id_anonymous");
  var city = $("#patient_city").val();

  if (city != "") {
    $("#get_location").val(city);
  }

  // const auto_location = new autoComplete({
  //     selector: "#get_location",
  //     data: {
  //         src: async (query) => {
  //             try {
  //                 console.log(query)
  //                 // Fetch Data from external Source
  //                 const source = await fetch('/export/get_locations/?term='+query);
  //                 // Data should be an array of `Objects` or `Strings`
  //                 const data = await source.json();
  //                 console.log(data)
  //                 return data;
  //             } catch (error) {
  //                 return error;
  //             }
  //         },
  //         keys: ["value"]
  //     },
  //     threshold: 2,
  //     debounce: 300,
  //     resultItem: {
  //         highlight: true
  //     },
  //     resultsList: {
  //         destination: "#search-results-locations",
  //         element: (list, data) => {
  //             //console.log(list)
  //             console.log(data)
  //             if (!data.results.length) {
  //                 // Create "No Results" message element
  //                 const message = document.createElement("div");
  //                 // Add class to the created element
  //                 message.setAttribute("class", "no_result");
  //                 // Add message text content
  //                 message.innerHTML = `<span>Found No Results for "${data.query}"</span>`;
  //                 // Append message element to the results list
  //                 list.prepend(message);
  //             }
  //         },
  //         noResults: true,
  //     },
  //     events: {
  //         input: {
  //             selection: (event) => {
  //                 const selection = event.detail.selection.value.value;
  //                 console.log(event)
  //                 auto_location.input.value = selection;
  //             }
  //         }
  //     },
  // });

  // // Get city from the database
  // $('#get_location').autocomplete({
  //     serviceUrl: "/export/get_locations",
  //     onSelect: function (event, ui) {
  //         $("#get_location").val(ui.item.value);
  //         // $('ul').empty();
  //     },
  //     // close: function () {
  //     //   $("#get_location").val("");
  //     //     $("#get_location").attr('placeholder', 'Enter a city');
  //     // }
  // });

  // Disable fields that identify a person when creating an anonymous user
  anonymous.on("change", function () {
    if ($(this).is(":checked")) {
      $("#id_name").prop("disabled", true);
      $("#id_name").prop("required", false);
      $("#id_cpf").prop("disabled", true);
      $("#id_origin").prop("disabled", true);
      $("#id_medical_record").prop("disabled", true);
      $("#id_rg").prop("disabled", true);
      $("#id_zipcode").prop("disabled", true);
      $("#id_street").prop("disabled", true);
      $("#id_address_number").prop("disabled", true);
      $("#id_address_complement").prop("disabled", true);
      $("#id_email").prop("disabled", true);
      $("#id_telephone_set-0-number").parents(".telephones").hide();
      $("#div_name").removeClass("form-group has-error");
      $("#div_name_message").children("ul:first").remove();
    } else {
      $("#id_name").prop("disabled", false);
      $("#id_name").prop("required", true);
      $("#id_cpf").prop("disabled", false);
      $("#id_origin").prop("disabled", false);
      $("#id_medical_record").prop("disabled", false);
      $("#id_rg").prop("disabled", false);
      $("#id_zipcode").prop("disabled", false);
      $("#id_street").prop("disabled", false);
      $("#id_address_number").prop("disabled", false);
      $("#id_address_complement").prop("disabled", false);
      $("#id_email").prop("disabled", false);
      $("#id_telephone_set-0-number").parents(".telephones").show();
      $("#div_name").attr("class", "form-group");
    }
  });

  anonymous.each(function () {
    if ($(this).is(":checked")) {
      $("#id_name").prop("disabled", true);
      $("#id_name").prop("required", false);
      $("#id_cpf").prop("disabled", true);
      $("#id_origin").prop("disabled", true);
      $("#id_medical_record").prop("disabled", true);
      $("#id_rg").prop("disabled", true);
      $("#id_zipcode").prop("disabled", true);
      $("#id_street").prop("disabled", true);
      $("#id_address_number").prop("disabled", true);
      $("#id_address_complement").prop("disabled", true);
      $("#id_email").prop("disabled", true);
      $("#id_telephone_set-0-number").parents(".telephones").hide();
    }
  });

  // Ajax to search for homonym patient by name
  $("#id_name").on("blur", async function () {
    var new_name = $("#id_name").val();

    if (new_name != original_name) {
      fetch_post(
        "/patient/verify_homonym/",
        {
          search_text: new_name,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        searchSuccessHomonym
      );

      fetch_post(
        "/patient/verify_homonym_excluded/",
        {
          search_text: new_name,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        searchSuccessHomonymExcluded
      );

      // $.ajax({
      //     type: "POST",
      //     url: "/patient/verify_homonym/",
      //     data: {
      //         'search_text': new_name,
      //         'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
      //     },
      //     success: searchSuccessHomonym,
      //     dataType: 'html'
      // });

      // $.ajax({
      //     type: "POST",
      //     url: "/patient/verify_homonym_excluded/",
      //     data: {
      //         'search_text': new_name,
      //         'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
      //     },
      //     success: searchSuccessHomonymExcluded,
      //     dataType: 'html'
      // });
    }
  });

  // Ajax to search for homonym patient by CPF
  $("#id_cpf").on("blur", function () {
    var new_cpf = $("#id_cpf").val();

    if (new_cpf != original_cpf) {
      fetch_post(
        "/patient/verify_homonym/",
        {
          search_text: new_cpf,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        searchSuccessHomonym
      );

      fetch_post(
        "/patient/verify_homonym_excluded/",
        {
          search_text: new_cpf,
          csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        searchSuccessHomonymExcluded
      );

      // $.ajax({
      //     type: "POST",
      //     url: "/patient/verify_homonym/",
      //     data: {
      //         'search_text': new_cpf,
      //         'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
      //     },
      //     success: searchSuccessHomonym,
      //     dataType: 'html'
      // });

      // $.ajax({
      //     type: "POST",
      //     url: "/patient/verify_homonym_excluded/",
      //     data: {
      //         'search_text': new_cpf,
      //         'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
      //     },
      //     success: searchSuccessHomonymExcluded,
      //     dataType: 'html'
      // });
    }
  });

  function searchSuccessHomonym(data, textStatus, jqXHR) {
    if ($("#search-results-homonym").html() != "") {
      $("#search-results-homonym").html(data);

      var myElem = document.getElementById("patient_homonym");

      if (myElem != null) {
        $("#modalHomonym").modal("show");
      } else {
        $("#search-results-homonym").html("");
      }
    }
  }

  function searchSuccessHomonymExcluded(data, textStatus, jqXHR) {
    if ($("#search-results-homonym-excluded").html() != "") {
      $("#search-results-homonym-excluded").html(data);

      var myElemExcluded = document.getElementById("patient_homonym_excluded");

      if (myElemExcluded != null) {
        $("#modalHomonymExcluded").modal("show");
      } else {
        $("#search-results-homonym-excluded").html("");
      }
    }
  }

  $("#modalHomonymCancel").on("click", function () {
    $("#search-results-homonym").html("");
  });

  $("#modalHomonymExcludedCancel").on("click", function () {
    $("#search-results-homonym-excluded").html("");
  });

  const cleaveCPF = new Cleave("#id_cpf", {
    blocks: [3, 3, 3, 2],
    delimiters: [".", ".", "-"],
    uppercase: true,
  });
  const cleaveCEP = new Cleave("#id_zipcode", {
    blocks: [5, 3],
    delimiter: "-",
    uppercase: true,
  });
  // $("#id_cpf").mask("999.999.999-99");
  //$('#id_zipcode').mask('99999-999');

  $("#savetab").on("click", function () {
    var name_value = $("#id_name").val().trim();
    var date_birth_value = $("#id_date_birth").val().trim();
    var gender_value = $("#id_gender").val().trim();
    var cpf_value = $("#id_cpf").val().trim();
    var anonymous = $("#id_anonymous");

    if (
      anonymous.is(":checked") &&
      (date_birth_value.length == 0 || gender_value.length == 0)
    ) {
      showErrorMessageTemporary(gettext("Obligatory fields must be filled."));
      jumpToElement("id_date_birth");
      if (date_birth_value.length == 0) {
        document.getElementById("id_date_birth").focus();
      } else if (gender_value.length == 0) {
        document.getElementById("id_gender").focus();
      }
    } else if (
      !anonymous.is(":checked") &&
      (name_value.length == 0 ||
        date_birth_value.length == 0 ||
        gender_value.length == 0)
    ) {
      showErrorMessageTemporary(gettext("Obligatory fields must be filled."));
      jumpToElement("id_name");
      if (name_value.length == 0) {
        document.getElementById("id_name").focus();
      } else if (date_birth_value.length == 0) {
        document.getElementById("id_date_birth").focus();
      } else if (gender_value.length == 0) {
        document.getElementById("id_gender").focus();
      }
    } else {
      var email_value = $("#id_email").val().trim();

      if (email_value.length != 0 && !validateEmail(email_value)) {
        showErrorMessageTemporary(
          gettext("Please fill the fields correctly. E-mail is invalid")
        );
      } else {
        if (!anonymous.is(":checked") && cpf_value.length == 0) {
          $("#modalNoCPF").modal("show");
        } else {
          $("#form_id").trigger("submit");
        }
      }
    }
  });

  $("#noCPF_modal").on("click", function () {
    $("#form_id").trigger("submit");
  });

  $("#more_phones").on("click", function () {
    document.getElementById("action").value = "more_phones";
    $("#form_id").trigger("submit");
  });
});

function validateEmail(email) {
  var re =
    /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}
