import threading
from prettytable import PrettyTable

# Sample data for books and authors
books_data = [
    ["BookID", "Title", "Genre", "Year", "Publisher"],
    [1, "The Great Gatsby", "Fiction", 1925, "Charles Scribner's Sons"],
    [2, "To Kill a Mockingbird", "Fiction", 1960, "J. B. Lippincott & Co."],
    [3, "1984", "Dystopian", 1949, "Secker & Warburg"],
    [4, "Pride and Prejudice", "Romance", 1813, "T. Egerton, Whitehall"],
    [5, "The Catcher in the Rye", "Coming-of-age", 1951, "Little, Brown and Company"],
    [6, "Animal Farm", "Political satire", 1945, "Secker & Warburg"],
    [7, "Brave New World", "Dystopian", 1932, "Chatto & Windus"],
    [8, "The Hobbit", "Fantasy", 1937, "George Allen & Unwin"],
    [9, "Lord of the Flies", "Allegory", 1954, "Faber and Faber"],
    [10, "The Grapes of Wrath", "Realistic fiction", 1939, "The Viking Press"],
    [11, "Harry Potter and the Philosopher's Stone", "Fantasy", 1997, "Bloomsbury Publishing"],
    [12, "A Brief History of Time", "Non-fiction", 1988, "Bantam Books"]
]

authors_data = [
    ["BookID", "Author", "Nationality", "Birthplace"],
    [1, "F. Scott Fitzgerald", "American", "Minnesota"],
    [2, "Harper Lee", "American", "Alabama"],
    [3, "George Orwell", "British", "India"],
    [4, "Jane Austen", "British", "England"],
    [5, "J.D. Salinger", "American", "New York"],
    [6, "George Orwell", "British", "India"],
    [7, "Aldous Huxley", "British", "England"],
    [8, "J.R.R. Tolkien", "British", "Africa"],
    [9, "William Golding", "British", "England"],
    [10, "John Steinbeck", "American", "California"],
    [13, "J.K. Rowling", "British", "England"],
    [14, "Stephen Hawking", "British", "England"]
]

# Function to perform join operation for a range of rows
def parallel_join(result, start, end):
    for i in range(start, end):
        for j in range(1, len(books_data)):
            if books_data[j][0] == authors_data[i][0]:
                result.append([books_data[j][0], books_data[j][1], books_data[j][2], books_data[j][3], books_data[j][4], authors_data[i][1], authors_data[i][2], authors_data[i][3]])

# Number of threads
num_threads = 4
result = []

# Split data range for each thread
chunk_size = len(authors_data) // num_threads
ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_threads - 1)]
ranges.append(((num_threads - 1) * chunk_size, len(authors_data)))

# Create and start threads
threads = []
for start, end in ranges:
    thread = threading.Thread(target=parallel_join, args=(result, start, end))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Display the result in a table format
books_table = PrettyTable(books_data[0])
for row in books_data[1:]:
    books_table.add_row(row)

authors_table = PrettyTable(authors_data[0])
for row in authors_data[1:]:
    authors_table.add_row(row)

result_table = PrettyTable(["BookID", "Title", "Genre", "Year", "Publisher", "Author", "Nationality", "Birthplace"])
for row in result:
    result_table.add_row(row)

print("Books Table:")
print(books_table)
print("\nAuthors Table:")
print(authors_table)
print("\nJoin Result:")
print(result_table)
