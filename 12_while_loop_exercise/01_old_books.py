book = input()
book_count = 0
next_book = input()

while next_book != 'No More Books':
    command = next_book
    if book == command:
        print(f'You checked {book_count} books and found it.')
        break
    book_count += 1
    next_book = input()
else:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')
