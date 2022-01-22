from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup


"""
this will start by detecting the html element in
the website, extract the words from it and then keep
a frequency count and of the words and the return the top 10 most frequent
"""

#this section detect the html elements
def start(url):
	#empty array for storing the words obtained from the web page
    wordlist =[] 
    page = urlopen(url)
	#decodes the bytes to a string
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    #print(soup)

	#looping through every word in the web-page from the staring div point, and converting it to text
    for each_text in soup.find_all('div', {'class': 'main main-page'}):
        content = each_text.text

		#change to lowercase for uniformity and split it to start the count
        words = content.lower().split()
        
		#looping through the words and adding each to the wordlist array
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

#cleaning the list by removing symbols as they will be counted as words
def clean_wordlist(wordlist):
    clean_list = []

    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

		#replace the symbols with the space
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

		#adding cleaned data to the list 
        if len(word) >0:
            clean_list.append(word)
        #print(wordlist)

    create_dict(clean_list)

#creating a dictionary to make help with counting, it accepts the clean_list as its inputs 
def create_dict(clean_list):
    word_count ={}

	#looping through word and checking if it has been counted and added or not,
	#it a word has been seen, the count is added otherwise, it set to 1
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] =1 
	#the counter operator helps with the count of the words
    c = Counter(word_count)
	#most common will help with the listing as appropriate
    top = c.most_common(10)
	#printing the output
    print(top)
    



if __name__ != '__main__':
    pass
else:
    url = 'https://www.maseno.ac.ke/application-procedure'
    start(url)
