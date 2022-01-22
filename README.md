The purpose of this small piece of script is:
   ---- do a web page crawl
   ---- detect the html elements
   ---- extract words from the html elements
   ---- return the top 10, 20 words in ascending order

for it to work properly edit the url to your needs, then moeve over to that web-page inspect and specify from which main class, you want to get the html element, take that class name and add it in the code (line 14) then run to get your desired results

This scrawls any website then goes ahead to count the frequency of words in that specific web page

The first function on top fetches information from any website and then pushes the contents to a wordlist, the first wordlist helps with this.
Teautifulsoap helps to pings the url request for data.
The second function helps remove the symbols obtained from the web-page