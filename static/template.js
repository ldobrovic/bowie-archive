let prev = 1
let next = 1

function load_buttons(data) {

    let id = parseInt(data.id)

    if (id == 1) {
        prev = 1;
    } else {
        prev = id-1
    }

    next = id+1

    $("#arrows").append("<button type='submit' id='prev'>Previous Album</button>")
    $("#arrows").append("<button type='submit' id='next'>Following Album</button>")

}


$(document).ready(function() {

    console.log("Wow")

    load_buttons(data)

    $(document).on('click', "#prev", function() {
        window.location.href = '/view/' + prev
    })

    $(document).on('click', "#next", function() {
        window.location.href = '/view/' + next
    })

});