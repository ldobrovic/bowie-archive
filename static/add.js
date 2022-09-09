function display_songs(songs) {

    $("#potentials").empty()

    if (songs.length == 0) {
        return
    }

    $("#songerr").remove()

    for (let i=0; i<songs.length; i++) {
        song = songs[i]
        $("#potentials").append("<span class='potential_song' id="+i+">"+song+"<span>")
    }
}

function save_album(new_album) {
    $(".success").remove()
    $.ajax({
        type: "POST",
        url: "add_entry",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_album),
        success: function(result){
            let album = result["data"]
            let id = album["id"]
            let title = album["title"]
            $("#announce").append("<span class='success'>    New item successfully created: </span>")
            $("#announce").append(("<span class='album success add_highlight' id="+id+"> <u>click here to view</u></span>"))
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


$(document).ready(function () {

    songs = []

    $("#add_song").on("click", function() {
        song = $("#hits").val()

        $("#hits").val("")

        if (song.trim() === '') {
            $("hits").focus()
            return
        } 

        songs.push(song)
        display_songs(songs)
    });

    $("#hits").on("keydown", function(key) {
        if (key.which == 13) {
            $("#add_song").trigger("click")
        }
    });

    $(document).on('click', '.potential_song', function() {
        let idx = parseInt($(this).attr('id'))
        songs.splice(idx, 1)
        display_songs(songs)
    })

    $("#submit_entry").click(function() {

        $(".err").remove()

        foundIssue = false

        desc = $("#desc").val()
        if (desc.trim() == '') {
            $("#desc").focus()
            $("#desc").after('<span class="err">This field is required.</span>');
            foundIssue = true
        }

        if (songs.length == 0) {
            $("#hits").focus()
            $("#add_song").after('<span class="err" id="songerr">This field is required.</span>');
            foundIssue = true
        }

        rating = $("#rating").val()
        if (rating == "") {
            $("#rating").focus()
            $("#rating").after('<span class="err">This field is required.</span>');
            foundIssue = true
        } else if (rating > 10 || rating < 0) {
            $("#rating").focus()
            $("#rating").after('<span class="err">Please enter a rating between 0 and 10</span>')
            foundIssue = true
        }

        year = $("#year").val()
        if (year == "") {
            $("#year").focus()
            $("#year").after('<span class="err">This field is required.</span>');
            foundIssue = true
        }

        image = $("#image").val()
        if (image.trim() == '') {
            $("#image").focus()
            $("#image").after('<span class="err">This field is required.</span>');
            foundIssue = true
        }

        title = $("#title").val()
        if (title.trim() == '') {
            $("title").focus()
            $("#title").after('<span class="err">This field is required.</span>');
            foundIssue = true
        }

        if (foundIssue) {
            return
        }

        $("#desc").val("")
        $("#hits").val("")
        $("#potentials").empty()
        $("#rating").val("")
        $("#year").val("")
        $("#image").val("")
        $("#title").val("")
        $("#title").focus()


        let new_album = {
            "title": title,
            "image": image,
            "year": year,
            "description": desc,
            "hits": songs,
            "rating": rating
        }

        songs = []

        save_album(new_album)
    })

});