from dataclasses import dataclass
from socketserver import ThreadingUnixStreamServer
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
import sys


data = [
    {
        "id" : "1",
        "title": "The Man Who Sold the World",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/2/23/TheManWhoSoldtheWorld.jpg/220px-TheManWhoSoldtheWorld.jpg",
        "year": "1970",
        "description": "Following the largely acoustic and folk rock sound of Bowie's previous 1969 self-titled album, The Man Who Sold the World marked a shift toward hard rock, with elements of blues rock. The lyrics are also darker than his previous releases, exploring themes of insanity, religion, technology and war. Retrospectively, the album has been praised by critics for the band's performance and the unsettling nature of its music and lyrics, being considered by many to be the start of Bowie's 'classic period'.",
        "hits": ["All the Madmen", "The Man Who Sold the World"],
        "rating": "8.4",
    },
    {
        "id" : "2",
        "title": "Hunky Dory",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/4/40/David_Bowie_-_Hunky_Dory.jpg/220px-David_Bowie_-_Hunky_Dory.jpg",
        "year": "1971",
        "description": "Compared to the guitar-driven hard rock sound of The Man Who Sold the World, Bowie opted for a warmer, more melodic piano-based pop rock and art pop style on Hunky Dory. His lyrical concerns on the record range from the compulsive nature of artistic reinvention on 'Changes', to occultism and Nietzschean philosophy on 'Oh! You Pretty Things' and 'Quicksand'; several songs make cultural and literary references. He was also inspired by his stateside tour to write songs dedicated to three American icons: Andy Warhol, Bob Dylan and Lou Reed. The song 'Kooks' was dedicated to Bowie's newborn son Duncan. The album's cover artwork, photographed in monochrome and subsequently recoloured, features Bowie in a pose inspired by actresses of the Hollywood Golden Age.",
        "hits": ["Changes/Andy Warhol", "Life on Mars?", "Queen Bitch"],
        "rating": "9.2"
    },
    {
        "id" : "3",
        "title": "The Rise and Fall of Ziggy Stardust and the Spiders from Mars",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/ZiggyStardust.jpg/220px-ZiggyStardust.jpg",
        "year": "1972",
        "description": "Described as a loose concept album and rock opera, Ziggy Stardust concerns Bowie's titular alter ego Ziggy Stardust, a fictional androgynous and bisexual rock star who is sent to Earth as a saviour before an impending apocalyptic disaster. In its story, Ziggy wins the hearts of fans but suffers a fall from grace after succumbing to his own ego. Most of the album's concept was developed after the songs were recorded. The glam rock and proto-punk musical styles were influenced by Pop, the Velvet Underground, and Marc Bolan of T. Rex, while the lyrics discuss the artificiality of rock music, political issues, drug use, sexual orientation and stardom.",
        "hits": ["Starman/Sufragette City", "Rock 'n' Roll Suicide", "Moonage Daydream"],
        "rating": "9.4"
    },
    {
        "id" : "4",
        "title": "Aladdin Sane",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/DavisBowieAladdinSane.jpg/220px-DavisBowieAladdinSane.jpg",
        "year": "1973",
        "description": "Bowie wrote most of the tracks on the road in the US between shows. Because of this, many of the tracks are greatly influenced by America and Bowie's perceptions of the country. Due to the American influence and the fast-paced songwriting, the record features a tougher and raunchier glam rock sound than its predecessor. The lyrics reflect the pros of Bowie's newfound stardom and the cons of touring and paint pictures of urban decay, drugs, sex, violence and death.",
        "hits": ["The Jean Genie", "Drive-In Saturday", "Time", "Let's Spend the Night Together"],
        "rating": "8.6"
    },
    {
        "id" : "5",
        "title": "Pin Ups",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/PinUps.jpg/220px-PinUps.jpg",
        "year": "1973",
        "description": "Devised as a 'stop-gap' album to appease his record label, it is a covers album, featuring songs by British bands from the 1960s that were influential to Bowie as a teenager, including the Pretty Things, the Who, the Yardbirds and Pink Floyd. The tracks mostly stay true to their original counterparts, albeit performed in glam rock and proto-punk styles. The album was recorded from July to August 1973 at the Château d'Hérouville in Hérouville, France following the completion of the Ziggy Stardust Tour. It was co-produced by Bowie and Ken Scott, marking the final collaboration between the two.",
        "hits": ["Sorrow", "See Emily Play"],
        "rating": "6.8"
    },
    { 
        "id" : "6",
        "title": "Diamond Dogs",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/1/1f/Diamond_dogs.jpg/220px-Diamond_dogs.jpg",
        "year": "1974",
        "description": "Conceived during a period of uncertainty over where his career was headed, Diamond Dogs is the result of multiple projects Bowie envisioned at the time. One of these was a musical based on Ziggy Stardust (1972), which he ultimately scrapped. Another was an adaptation of George Orwell's 1949 novel Nineteen Eighty-Four. After being denied the rights by Orwell's widow, Bowie devised an urban apocalyptic scenario based on the writings of William S. Burroughs. Together, the songs from these projects form the theme of Diamond Dogs.",
        "hits": ["Rebel Rebel", "Diamond Dogs", "1984"],
        "rating": "7.9"
    },
    {
        "id" : "7",
        "title": "Young Americans",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/b/b5/Young_americans.jpg/220px-Young_americans.jpg",
        "year": "1975",
        "description": " The album marked a departure from the glam rock style of Bowie's previous albums, showcasing his interest in soul and R&B. Commentators have described the record as blue-eyed soul, although Bowie himself labelled the album's sound 'plastic soul. Initial recording sessions took place following the first leg of his Diamond Dogs Tour in August 1974 at Sigma Sound Studios in Philadelphia with producer Tony Visconti and a variety of musicians, including guitarist Carlos Alomar, who would become one of Bowie's most frequent collaborators. Backing vocalists included singer Ava Cherry, Alomar's wife Robin Clark and then-unknown singer Luther Vandross.",
        "hits": ["Young Americans", "Fame"],
        "rating" : "8.0"
    },
    {
        "id" : "8",
        "title": "Station to Station",
        "image": "https://upload.wikimedia.org/wikipedia/en/7/7a/David_Bowie_Station_to_Station_2010_artwork.jpg",
        "year": "1976",
        "description": "Regarded as one of his most significant works, the album was the vehicle for Bowie's performance persona, the Thin White Duke. Co-produced by Bowie and Harry Maslin, Station to Station was mainly recorded at Cherokee Studios in Los Angeles, California, in late 1975, after Bowie completed shooting the film The Man Who Fell to Earth; the cover art featured a still from the film. During the sessions, Bowie was dependent on drugs, especially cocaine, and later said that he recalled almost nothing of the production.  Musically, Station to Station was a transitional album for Bowie, developing the funk and soul of Young Americans while presenting a new direction influenced by electronic music and the German music genre of krautrock, particularly bands such as Neu! and Kraftwerk.",
        "hits": ["Station to Station", "Golden Years", "TVC 15"],
        "rating" : "9.0"
    },
    {
        "id" : "9",
        "title": "Low",
        "image": "https://upload.wikimedia.org/wikipedia/en/thumb/9/93/Low_%28album%29.jpg/220px-Low_%28album%29.jpg",
        "year": "1977",
        "description": "After years of drug addiction when living in Los Angeles, Bowie moved to France in 1976 with his friend Iggy Pop to sober up. There, Bowie produced and co-wrote Pop's debut studio album, The Idiot, featuring sounds Bowie would explore on his next record. After completing The Idiot, Bowie began recording the first of three collaborations that became known as the Berlin Trilogy with American producer Tony Visconti and English musician Brian Eno. Grounded in art rock and experimental rock and influenced by German bands such as Tangerine Dream, Neu!, Harmonia and Kraftwerk, Low features Bowie's first explorations in electronic and ambient styles.",
        "hits": ["Sound and Vision", "A New Career in a New Town", "Be My Wife", "Speed of Life", "Breaking Glass", "Art Decade"],
        "rating": "9.0"
    },
    {
        "id" : "10",
        "title": "'Heroes'",
        "image": "https://upload.wikimedia.org/wikipedia/en/7/7b/David_Bowie_-_Heroes.png",
        "year": "1977",
        "description": " After releasing Low earlier that year, Bowie toured as the keyboardist of his friend and singer Iggy Pop. At the conclusion of the tour, they recorded Pop's second solo album Lust for Life at Hansa Tonstudio in West Berlin before Bowie regrouped there with collaborator Brian Eno and producer Tony Visconti to record 'Heroes'. It was the second instalment of his Berlin Trilogy, following Low and preceding Lodger (1979). The music itself is based in art rock and experimental rock, and builds upon its predecessor's electronic and ambient approaches, albeit with more positive tones, atmospheres and passionate performances.",
        "hits": ["Heroes", "V-2 Schneider", "Beauty and the Beast", "Sense of Doubt"],
        "rating": "8.8"
    },
]

current_id = 10


# ROUTES

@app.route('/')
def render_welcome():
   return render_template('welcome.html', albums=data)

@app.route('/view/<id>')
def render_view(id):
    global data

    albums = [x for x in data if x["id"] == id]

    if len(albums) == 0:
        albums.append(data[0])

    return render_template("template.html", data = albums[0])

@app.route('/edit/<id>')
def render_edit(id):
    global data

    albums = [x for x in data if x["id"] == id]

    return render_template("edit.html", data=albums[0])

@app.route('/add')
def render_add():
    global data

    return render_template("add.html")

@app.route('/edit/submit', methods=['GET', 'POST'])
def do_edit():
    global data

    json_data = request.get_json()

    id = int(json_data["id"])

    edited_album = {
        "title": json_data["title"],
        "image": json_data["image"],
        "year": json_data["year"],
        "hits": json_data["hits"],
        "rating": json_data["rating"],
        "description": json_data["description"]
    }

    data[id-1].update(edited_album)

    albums = [x for x in data if x["id"] == str(id)]

    return jsonify(data=albums[0])


@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    global data
    global current_id

    json_data = request.get_json()

    current_id += 1

    new_album = {
        "id": str(current_id),
        "title": json_data["title"],
        "image": json_data["image"],
        "year": json_data["year"],
        "description": json_data["description"],
        "hits": json_data["hits"],
        "rating": json_data["rating"],
    }

    data.append(new_album)

    albums = [x for x in data if x["id"] == str(current_id)]

    return jsonify(data=albums[0])


@app.route('/search/<search_term>/')
def render_search(search_term):
    global data

    titles = []
    hits = []
    desc = []

    for album in data:

        if search_term.lower() in album["title"].lower():
            titles.append(album)


        found = False
        this_hits = []
        for hit in album["hits"]:
            if search_term.lower() in hit.lower():
                this_hits.append(hit)
                if not found:
                    found = True
        if found:
            hits.append((album, this_hits))
        

        if search_term.lower() in album["description"].lower():
            text = album["description"].lower()
            word = search_term.lower()
            idx = text.index(word)
            if (idx-15) < 0:
                begin = 0
            else:
                begin = idx-15
            if (idx+len(word)+15)>(len(text)):
                end = len(text)
            else:
                end = idx+len(word)+15
            desc.append((album, album["description"][begin:end]))

    return render_template("search.html", titles=titles, hits=hits, desc=desc, search_term=search_term)


if __name__ == '__main__':
   app.run(debug = True)




