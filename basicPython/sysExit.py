from email import feedparser
import sys

while True:
    feedback = input('Type exit to exit : ')
    if feedback == 'exit':
        print(f'You typed {feedback} ')
        sys.exit()