# Program #2: Movie Tix
# Author: Zepora
# Date: 9/26/2025
# Title: Movie Ticket Counter

# Program #2: Movie Tix

total_tickets = 0
num_movies = int(input("How many movies do you want to enter? "))

for i in range(num_movies):
    
    movie = input("Enter the movie name: ")
    tickets = int(input(f"How many tickets for {movie}? "))
    total_tickets += tickets
    
    print("Total number of tickets desired:", total_tickets)