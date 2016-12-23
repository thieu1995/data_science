import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life",
						"http://www.ufunk.net/wp-content/uploads/2012/08/Secret-Life-of-Toys-santlov-27.jpg",
						"https://www.youtube.com/watch?v=Zw39EBSlwRo")
#print(toy_story.storyline)


avatar = media.Movie("Avatar",
					"A marine on an aline planet",
					"https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)


godfather = media.Movie("Godfather",
						"Something ... ",
						"https://en.wikipedia.org/wiki/The_Godfather_(2006_video_game)#/media/File:The_Godfather,_The_Game.jpg",
						"https://www.youtube.com/watch?v=fB_8VCwXydM")
#godfather.show_trailer()						

poh = media.Movie("The Pursuit of Happyness",
					"The Pursuit of Happyness is a 2006 American biographical drama film based on entrepreneur Chris Gardner's nearly one-year struggle being homeless. ",
					"https://en.wikipedia.org/wiki/The_Pursuit_of_Happyness#/media/File:Poster-pursuithappyness.jpg",
					"https://www.youtube.com/watch?v=00uTFVnWJMw")

movies = [toy_story, avatar, godfather, poh]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)



