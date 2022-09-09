$(document).ready(function () {

    $(document).on('click', '.album', function() {
        let id = $(this).attr('id')
        window.location.href = '/view/' + id
    })

    $(document).on('click', '#add', function() {
        window.location.href = '/add'
    })

    $("#submit").on("click", function() {

        let search_term = $("#textinput").val()

        console.log(search_term)

        if (search_term.trim() == '') {
            $("#textinput").val("")
            $("#textinput").focus()
        } else {
            window.location.href = '/search/' + search_term
        }
    })

    $("#textinput").on("keyup", function(e) {
        var code = e.keyCode || e.which
        if (code == 13){
            $("#submit").click()
        }
    })
});