def print_row(movie_info):
    info = movie_info.split("||")

    print("|--------------------|--------------------|--------------------|")
    print("|{:^20s}|{:^20s}|{:^20s}|".format(
        info[0][7:], info[1][7:], info[2][8:11]))

def print_table(movies):
    print("----------------------------------------------------------------")
    print("|       Movie        |       Genre        |       Rating       |")

    for movie in movies:
        print_row(movie)
    
    print("----------------------------------------------------------------")


if __name__ == "__main__":
    movies = [
        "Title: Bee Movie||Genre: Animation/Comedy||Rating: 6.1/10",
        "Title: Shrek||Genre: Animation/Comedy||Rating: 7.8/10",
        "Title: Revenge of the Sith||Genre: Action/Sci-Fi||Rating: 7.5/10",
        "Title: Inception||Genre: Thriller/Action||Rating: 8.8/10",
        "Title: Willy Wonka||Genre: Musical/Family||Rating: 7.8/10"
    ]

    print_table(movies)