import os
import re
import shutil
import requests
from bs4 import BeautifulSoup

"""
scrape.py
By: Gico Carlo Evangelista (RiceAbove)

NOTE:
This script is made to webscrape the BSOE renumbering table and convert that into
a javascript object literal (or hashtable) used for the course conversion
DO NOT RUN THIS SCRIPT UNLESS FOR FIXING BUGS OR ADDING FUNCTUALITY.
"""

# Write courses at object literal
def write_js(f, old, new, desc, type):
    if type == '!scrape':
        f.write('convCourse["{}"] = ["{}","{}"];\n'.format(old, new, desc))
    else:
        f.write('convCourse["{}"] = ["{}","{}"];\n'.format(new, old, desc))

# For testing. Check if script stars
def start_scrape():
    print()
    print('-------------------------------------------------------------------')
    print('Start Scrape')
    print('-------------------------------------------------------------------')
    return open('../js/main.js', 'a+')

# Scrape BSOE renumbering table
def scrape(link, type):
    try:
        f = start_scrape()
        main = requests.get(link).text
        soup = BeautifulSoup(main, "lxml")
        for courses in soup.find_all("tr"):
            course = courses.find_all('td', class_=re.compile("s[14]"))
            if len(course) >= 3:
                old_course = course[0].text
                old_course = re.sub(' 0+', ' ', old_course)
                new_course = course[1].text
                new_course = re.sub(' 0+', ' ', new_course)
                desc = course[2].text
                if "Moving to " in new_course and type != "!scrape":
                    new_course = re.sub('Moving to ', "", new_course)
                    old_course = "Moved from " + old_course
                print('{}   \t{}   \t{}'.format(old_course, new_course, desc))
                write_js(f, old_course, new_course, desc, type)
    except Exception as e:
        print('Error while scraping', e)
    end_scrape(f)

# For testing. Check if script ends
def end_scrape(f):
    print('-------------------------------------------------------------------')
    print('End Scrape')
    print('-------------------------------------------------------------------')
    print()
    f.close()

# Checks how many classes are being webscraped
def count(link):
    try:
        class_count = 0
        main = requests.get(link).text
        soup = BeautifulSoup(main, "lxml")
        print()
        print('*******************************************************************')
        print('Counting...')
        for courses in soup.find_all("tr"):
            course = courses.find_all('td', class_=re.compile("s[14]"))
            if len(course) >= 3:
                class_count += 1
                new_course = course[1].text
                print('{}   \t{}'.format(class_count, new_course))
        print()
        print('Number of courses: {}'.format(class_count))
        print('*******************************************************************')
        print()
    except Exception as e:
        print('Error while counting')

# Check if the website is up
def check(link):
    check_link = requests.get(link)
    status_code = check_link.status_code
    print()
    print('*******************************************************************')
    print('Status Code:\t {}'.format(status_code))
    print('Up & running?:\t {}'.format(status_code == requests.codes.ok))
    print('*******************************************************************')
    print()

# Prints available commands
def help():
    print()
    print('*******************************************************************')
    print('List of commands:')
    print('*******************************************************************')
    print('!help\t    - List all of the commands for scrape.py')
    print('!check\t    - Checks the response status code of the table')
    print('!scrape\t    - Scrapes BSOE data & adds it to main.js | Old course --> New course')
    print('!rev_scrape - Does the same thing as scrape except New course --> Old course')
    print('!count\t    - Counts how many classes are being scraped')
    print('!exit\t    - Exit program')
    print()

# Prints successful start of script
def start():
    print()
    print('*******************************************************************')
    print('scrape.py for BSOE New Course Search')
    print('Type "!help" for list of commands')
    print('*******************************************************************')
    print()
    try: 
        shutil.copy('../js/main-blank.js','../js/main.js')
    except Exception as e:
            print("Error while creating template file.", e)

# Main function
def main():
    user_input = None
    link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSaEqu5y2LqKl6BnV4XNwViiTi5p11ltC9zQPLt0Qb6NHVrWKmfqQ5o3wt5StzR0mtjJck3RW1R3T5w/pubhtml?gid=0&amp;single=true&amp;widget=false&amp;headers=false&amp;chrome=false&amp;rm=minimal#s'
    start()
    while(user_input != '!exit'):
        user_input = str(input('> '))
        if user_input == '!help':
            help()
        elif user_input == '!check':
            check(link)
        elif user_input == '!scrape' or user_input == '!rev_scrape':
            scrape(link, user_input)
        elif user_input == '!count':
            count(link)
        elif user_input == '!exit':
            print('\nExiting scrape.py')
        else:
            print('Invalid command. Try again')


# Start script
if __name__ == '__main__':
    main()
