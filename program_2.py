# Program #2: Movie Tix
# Author: Zepora
# Date: 9/26/2025
# Title: Movie Ticket Counter

def main():
    # Initialize total ticket counter
    total_tickets = 0

    # Ask how many movies they want to buy tickets for
    num_movies = int(input("How many different movies are you buying tickets for? "))

    # Loop through each movie entry
    for i in range(num_movies):
        movie_name = input(f"Enter the name of movie {i + 1}: ")
        tickets = int(input(f"How many tickets for '{movie_name}'? "))
        total_tickets += tickets

    # Display the total number of tickets
    print("Total number of tickets:", total_tickets)

if __name__ == '__main__':
    main()
