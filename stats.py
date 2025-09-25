def count_words(content):
	content = content.split()
	word_count = 0
	for word in content:
		word_count+=1
	return word_count

def character_count(content):
	char_count = {}
	for ch in content:
		c = ch.lower()
		char_count.setdefault(c, 0)
		char_count[c] += 1
	return char_count

def sort_dict(dictionary):
	for key in sorted(dictionary.keys()):
		if key.isalpha():
			print(f"{key}: {dictionary[key]}")