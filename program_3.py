# Program #3: Average Rainfall
# Program #2: Movie Tix
# Author: Zepora
# Date: 9/26/2025
# Title: Movie Ticket Counter
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

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