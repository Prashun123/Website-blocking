from googlesearch import search

query = input("Enter your field: ")

website_lists =[]
for i in search(query, tld="com", num=1000, stop=1000, pause=2):
    website_lists.append(i[7:(len(i)-1)])

print(website_lists)
