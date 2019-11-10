import unittest

def test_random_movie():
    Random = Movies.random_movie()
    assert Random == Title_Movie

def test_add_movie():
    Add = append.add_movie
    assert Add == Movies("Spider Man Homecoming")

def test_choose_by_genre():
    Animated = Movies.choose_by_genre
    assert Animated == choose_by_genre(Animated)