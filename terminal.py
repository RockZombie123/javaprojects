#The terminal app store for any computer!
#■
import requests
import time 
import sys
import os
print("""

Welcome to the terminal app store! You may also refer to this as:
'What the app store would be like if it were in the 1980's'.

""")


ans = input('Search: ')
if ans == 'testapp':
	print('#&&TESTAPP01')
elif ans == 'testapp2':
	  print('#&&TESTAPP02')

elif len(ans) > 25:
	print('Oops. Your search was too long.')

elif ans == 'Facebook image':
	  print('1 result has been found:')
	  print('facebook.ico')
	  time.sleep(1)
	  down = input('would you like to download it now? (yes/no) ')
	  if down == 'yes':
		   for i in range(12):
                           print("Downloading:" + "■" * i)
                           sys.stdout.write("\033[F") # Cursor up one line
                           time.sleep(0.1)
		   url = 'https://www.facebook.com/favicon.ico' 
		   r = requests.get(url, allow_redirects=True)
		   open('facebook.ico', 'wb').write(r.content)
	  else:
                   print('Aborted.')

elif ans == 'Freegames':
	  exec(open('PikaGame.py').read())

elif ans == 'Delete Freegames':
	  print('Deleting Freegames...')
	  os.system('python3 -m pip uninstall freegames')


else:
	  print('''404 not found.


Check your grammar.
Check your spelling.
This app store is sensitive to caps.
This app might have been removed or it isn't available for your state.


''')
