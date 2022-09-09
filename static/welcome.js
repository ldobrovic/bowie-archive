function display_starters(albums) {

    best_albums = ["The Rise and Fall of Ziggy Stardust and the Spiders from Mars", "Station to Station", "Low"]

    for (var i=0; i<albums.length; i++) {
        album = albums[i]

        let title = album["title"]
        let id = album["id"]
        let src = album["image"]
        let rtg = album["rating"]

        if (best_albums.includes(title)) {
            $("#putithere").append("<div class='col-md-4'><div id="+id+" class=album><img src=" + src + 
            " class='welcome_img' alt='Album cover for " + title + "'><br>" + 
            "<span class=welcome_title>" + title + "</span> - " + 
            "<span class=welcome_rating>" + rtg + "/10</span></div></div>")
        }
    }

}

$(document).ready(function () {

    display_starters(albums)

});