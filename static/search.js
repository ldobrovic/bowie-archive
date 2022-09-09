function display_titles(titles, search_term) {

    if (titles.length == 0) {
        return
    }

    $("#titles_res").append("<div class='search_res'> Match in album title:</div>")

    for (let i=0; i<titles.length; i++) {
        album = titles[i]
        title = album["title"]
        id = album["id"]
        $("#titles_res").append(("<div class='album search_name' id="+id+">"+title+"</div>"))
        $(".album").mark(search_term)
    }
}

function display_hits(hits, search_term) {

    var words = [search_term]
    var reg = RegExp(words.join('|'), 'gi')

    if (hits.length == 0) {
        return
    }

    $("#hits_res").append("<div class='search_res'> Match in album's recommended songs:</div>")

    for (let i=0; i<hits.length; i++) {
        album = hits[i][0]
        title = album["title"]
        id = album["id"]
        $("#hits_res").append("<div class='album search_name search_album' id="+id+">"+title+"</div>")

        for (let j=0; j<hits[i][1].length; j++) {
            song = hits[i][1][j]
            console.log(song)
            $('#hits_res').append(("<div class='search_song'>"+song+"</div>"))
            $(".search_song").mark(search_term)
        }

        $("#hits_res").append("<div class='search_spacer'</div>")

    }
}

function display_desc(desc, search_term) {

    if (desc.length == 0) {
        return
    }

    $("#desc_res").append("<div class='search_res'> Match in album description:</div>")

    for (let i=0; i<desc.length; i++) {
        album = desc[i][0]
        title = album["title"]
        id = album["id"]
        $("#desc_res").append("<div class='album search_name search_album' id="+id+">"+title+"</div>")

        $('#desc_res').append("<div class='search_song'>..."+desc[i][1]+"...</div>")
        $(".search_song").mark(search_term)

        $("#desc_res").append("<div class='search_spacer'</div>")
    }
}



function master_display(titles, hits, desc, search_term) {

    $("#textinput").val("")

    let sum = titles.length + hits.length + desc.length

    if (sum == 0) {
        $("#search_header").prepend("<div id='search_bam'>No results found for '"+search_term+"'</div>")
        return
    } else {
        $("#search_header").prepend("<div id='search_bam'>"+sum+" search results for '"+search_term+"':</div>")
    }



    display_titles(titles, search_term)
    display_hits(hits, search_term)
    display_desc(desc, search_term)



}

$(document).ready(function () {

    master_display(titles, hits, desc, search_term)

});