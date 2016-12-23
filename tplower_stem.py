with open('tweet_text.txt', 'r') as fileinput:
	lines = [line.lower() for line in fileinput]


with open('tweet_text_lower.txt', 'w') as out:
    out.writelines((lines))
