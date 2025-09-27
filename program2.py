# Program #2: Movie Tix
# Author: Zepora
# Date: 9/26/2025
# Title: Movie Ticket Counter

# program2.py
total_tickets = 0
num_movies = int(input())

for i in range(num_movies):
    movie = input()
    tickets = int(input())
    total_tickets += tickets

print(total_tickets)