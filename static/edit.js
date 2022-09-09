original_album = {}
songs = []

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

function edit_album(edited_album) {
    $.ajax({
        type: "POST",
        url: "/edit/submit",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(edited_album),
        success: function(result){
            window.location.href = '/view/' + original_album["id"]
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function populate_text() {

    $("#title").val(original_album["title"])
    $("#image").val(original_album["image"])
    $("#year").val(original_album["year"])
    $("#rating").val(original_album["rating"])
    songs = [...original_album["hits"]]
    console.log(original_album["hits"])
    display_songs(songs)
    $("#desc").val(original_album["description"])
}


$(document).ready(function () {

    original_album["title"] = album.title
    original_album["id"] = album.id
    original_album["image"] = album.image
    original_album["year"] = album.year
    original_album["rating"] = album.rating
    original_album["hits"] = album.hits
    original_album["description"] = album.description

    populate_text()

    $("#dialog").dialog({
        autoOpen: false,
        dialogClass: "no-close",
        modal: true,
    });

    $(document).on('click', "#discard_changes", function() {
        $("#dialog").dialog('open');
        $("#dialog").focus()
    })

    $("#yes").on("click", function() {
        window.location.href = '/view/' + original_album["id"]
    })

    $("#no").on("click", function() {
        $("#dialog").dialog("close")
    })

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

        let edited_album = {
            "id": original_album["id"],
            "title": title,
            "image": image,
            "year": year,
            "description": desc,
            "hits": songs,
            "rating": rating
        }

        songs = []

        edit_album(edited_album)
    })

});