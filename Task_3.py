story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thankyou very much."
word_count = sum([1 for word in story.split() if len(word) > 4])
print(word_count)