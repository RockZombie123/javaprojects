#Browser 'if' statements. (not to be confused with elif.)

print('This browser does not have posts, and thus answers will come directly from the dev.')
print('This browser will have updates including new features, bugfixes, and new search results.')

ans = input('Search something: ')

if ans == 'upupdowndownleftrightleftrightBA':
	print('Psst... Search: Konami Code.')
	with open('konamicode.txt') as f:
                contents = f.read()
                print(contents)

elif len(ans) > 100:
	print('Oops. Your search was too long.')

elif ans == 'Python':

	with open('python.txt') as f:
    		contents = f.read()
    		print(contents)

elif ans == 'Joe Biden':
	  with open('biden.txt') as f:
		  contents = f.read()
		  print(contents)

elif ans == 'help':
	  with open('help.txt') as f:
		  contents = f.read()
		  print(contents)


elif ans == '✓✓✓':
	  print('''You are amazing & unique.

	 Don't forget that. :)''')

elif ans == 'Konami Code':
          with open('konamicode.txt') as f:
                  contents = f.read()
                  print(contents)

else:

	print('''404 not found.

	Try checking your spelling.
	Try checking your grammar.
	This browser is case sensitive.
	Try to avoid things like: 'who the heck' or 'lol' to your search.
	Try requesting for the search result(s) you expected for a future update.''')


