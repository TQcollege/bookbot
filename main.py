import sys
from stats import count_words, character_count, sort_dict

def get_book_text(book_path):
	try:
		with open(book_path) as f:
			file_contents = f.read()
	except FileNotFoundError as e:
		print("ERROR. FILE NOT FOUND")
		sys.exit(1)
	return file_contents


def main():
	if len(sys.argv) > 2 or len(sys.argv) < 2:
		print(f"Error: expected 1 argument, recieved {len(sys.argv) - 1}")
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		bookpath = sys.argv[1]

	try:
		contents = get_book_text(bookpath)
		word_count = count_words(contents)
		char_count = character_count(contents)
	except Exception as e:
		print(e)
		sys.exit(1)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {bookpath}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	sort_dict(char_count)
	print("============= END ===============")

	return 0

main()
