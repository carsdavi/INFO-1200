import csv
import sys

FILENAME = "movies_test.csv" # step 4: change the  filename in the global constant to movies_test.csv

def exit_program():
    print("Terminating program.")
    sys.exit()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        #print(f"Could not find {FILENAME} file.") # comment out line
        #exit_program() # comment out line
        # step 4: return the empty movies list that's initialized in the try block
        return movies
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            # raise BlockingIOError("Test the OSError Exception Terminating Program.")
            writer = csv.writer(file)
            writer.writerows(movies)
    # step 3: Modify the write_movies() function so it also handles any OSError exceptions by displaying the class name and error message of the exception object and exiting the program.        
    except OSError as e:
        print(type(e), e) # displaying the class name and error message of the exception object and exiting the program.
        exit_program() # exiting program

            
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
    
def add_movie(movies):
    name = input("Name: ")
    while True: # step 3: Add data validation
        try:
            year = int(input("Year: "))   
            if year <= 0:  # check to make sure it's greater than zero
                print("Year must be greater than zero")
                continue
            else:
                break
        except ValueError:
            print("Invalid year. Please try again.")
            continue

    # step 3: valid integer that's greater than zero.

    
    
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
