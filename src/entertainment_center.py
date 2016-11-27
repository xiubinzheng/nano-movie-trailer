'''
Created on Nov 26, 2016

@author: xzheng
'''
import Media
import fresh_tomatoes

toy_story = Media.Movie("Toy Story",
                        "toys come alive and show what it really means about friendship",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
                        , "https://www.youtube.com/watch?v=KYz2wyBy3kc")

rocky_movie = Media.Movie("Rocky", "An underdog boxer overcome the odds of million to one",
                          "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
                          "https://www.youtube.com/watch?v=7RYpJAUMo2M")

forrest_gump_movie = Media.Movie("forrest gump", "it tells the story of a man with an IQ of 75 and his epic journey through life.",
                                 "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                                 "https://www.youtube.com/watch?v=bLvqoHBptjg")

jerry_maguire_movie = Media.Movie("Jerry Maquire", "it tells the story of a man with an IQ of 75 and his epic journey through life.",
                                 "https://upload.wikimedia.org/wikipedia/en/e/ea/Jerry_Maguire_movie_poster.jpg",
                                 "https://www.youtube.com/watch?v=bLvqoHBptjg")

pumping_iron_movie = Media.Movie("Pumping Iron", "Documentray about the sport of bodybuilding.",
                                 "https://upload.wikimedia.org/wikipedia/en/6/61/Pumping_Iron_movie_poster.jpg",
                                 "https://www.youtube.com/watch?v=e1vprTwGQ4M")

men_of_honor_movie = Media.Movie("Men of Honor", "true story of a men", 
                                 "https://upload.wikimedia.org/wikipedia/en/d/dd/Men_of_honor_ver1.jpg", 
                                 "https://www.youtube.com/watch?v=m6xGjp0U9Dc")

movie_list = [toy_story, rocky_movie, forrest_gump_movie, jerry_maguire_movie, pumping_iron_movie, men_of_honor_movie]

fresh_tomatoes.open_movies_page(movie_list)
