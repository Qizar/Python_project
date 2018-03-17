import webbrowser
import fresh_tomatoes

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    


toy_story = Movie("Toy Story",
                            "A story of a boy and his toys",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=4KPTXpQehio"
                            )

avatar = Movie("Avatar",
               
                         "A marine on an alien planet",
                         "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                         "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
                         )

school_of_rock = Movie("School of Rock",
                                 "Using rock music to learn",
                                 "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                                 "https://www.youtube.com/watch?v=3PsUJFEBC74"
                                 )

ratatouille = Movie("Ratatouille",
                              "A rat is a chef in paris",
                              "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                              "https://www.youtube.com/watch?v=c3sBBRxDAqk"
                              )

midnight_in_paris = Movie("Midnight in paris",
                                     "Going back in time to meet authors",
                                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                     "https://www.youtube.com/watch?v=BYRWfS2s2v4"
                                     )

hunger_games = Movie("Hunger Games",
                               "A really real reality show",
                               "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=4S9a5V9ODuY"
                               )

movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]

fresh_tomatoes.open_movies_page(movies)
