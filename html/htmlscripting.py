# !usr/local/bin/python3
# htmlscripting.py
# the script needs only to produce an html page with the following html:
# <html>
# <body>
# Stay tuned for our amazing summer sale!
# </body>
# </html>

def main():
    html = '''\
    <html>
    <body>
    Stay tuned for our amazing summer sale!
    </body>
    </html>'''
    open('test.html', 'w').write(html)
    print (html)

if __name__ == '__main__':
    main()
