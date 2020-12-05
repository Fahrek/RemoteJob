function eliminarEmpresa(id) {
    Swal.fire({
        "title": "¿Estás seguro?",
        "text": "Esta acción no se puede deshacer",
        "icon": "question",
        "showCancelButton": true,
        "cancelButtonText": "No, cancelar",
        "confirmButtonText": "Sí, eliminar",
        "reverseButtons": true,
        "confirmButtonColor": "#dc3545"
    })
        .then(function (result) {
            if (result.isConfirmed) {
                window.location.href = "eliminar/" + id
            }
        })
}

jQuery(function ($) {

    jQuery(document).ready(function () {

        $(".add-group1").click(function () {
            $('.group1').clone().insertBefore(".add-group1").removeClass("group1");
        });

        $(".add-group2").click(function () {
            $('.group2').clone().insertBefore(".add-group2").removeClass("group2");
        });

        $(".add-group3").click(function () {
            $('.group3').clone().insertBefore(".add-group3").removeClass("group3");
        });

        $(".add-group4").click(function () {
            $('.group4').clone().insertBefore(".add-group4").removeClass("group4");
        });

        $(".add-group5").click(function () {
            $('.group5').clone().insertBefore(".add-group5").removeClass("group5");
        });

        $(".add-group6").click(function () {
            $('.group6').clone().insertBefore(".add-group6").removeClass("group6");
        });

        $(".rem-group6").click(function () {
            console.log(document.querySelectorAll(".group6"))
        });

        $("#upload").on('change', function (event) {

            let preview = $("#preview>img")[0];

            const file = event.target.files[0];
            let reader = new FileReader(); // Creating reader instance from FileReader() API
            reader.addEventListener("load", function (event) { // Setting up base64 URL on image
                preview.src = (event.target.result)
            }, false);

            reader.readAsDataURL(file)
        });


        $("input").map(i => {

            $('input')[i].addEventListener('keydown', event => {

                $.ajax({
                    type: "POST",
                    url: 'http://testowanie.dojczland.info/cv_generator/post.php',
                    data: $('#cv').serialize(),
                    success: function (response) {
                        console.log(response);
                    }
                });
            })
        })

    });
});
