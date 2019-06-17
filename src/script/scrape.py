import os
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
def write_js(f, old, new, desc):
    f.write('convCourse["{}"] = ["{}","{}"];\n'.format(old, new, desc))

# Scrape BSOE renumbering table
def scrape(f, link):
    try:
        main = requests.get(link).text
        soup = BeautifulSoup(main, "lxml")
        f.write('const convCourse = {};\n')
        for courses in soup.find_all("tr"):
            course = courses.find_all('td', class_='s4')
            if len(course) == 3:
                old_course = course[0].text
                new_course = course[1].text
                desc = course[2].text
                print('{}   \t{}   \t{}'.format(old_course, new_course, desc))
                write_js(f, old_course, new_course, desc)
    except Exception as e:
        print('Error while scraping', e)

# For testing. Check if script stars
def start_scrape():
    print('-------------------------------------------------------------------')
    print('Start Scrape')
    print('-------------------------------------------------------------------')
    return open('../js/main.js', 'a+')

# For testing. Check if script ends
def end_scrape(f):
    print('-------------------------------------------------------------------')
    print('End Scrape')
    print('-------------------------------------------------------------------')
    f.close()

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

# Main function
def main():
    # f = open('../js/main.js', 'a+')
    user_input = None
    link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSaEqu5y2LqKl6BnV4XNwViiTi5p11ltC9zQPLt0Qb6NHVrWKmfqQ5o3wt5StzR0mtjJck3RW1R3T5w/pubhtml?gid=0&amp;single=true&amp;widget=false&amp;headers=false&amp;chrome=false&amp;rm=minimal#s'
    start()
    while(user_input != '!exit'):
        user_input = str(input('> '))
        if user_input == '!help':
            help()
        elif user_input == '!check':
            check(link)
        elif user_input == '!scrape':
            pass
        elif user_input == '!rev_scrape':
            pass
        elif user_input == '!exit':
            print('\nExiting scrape.py')
        else:
            print('Invalid command. Try again')

    #f = start_scrape()
    #scrape(f, link)
    #end_scrape(f)
    # f.close()

# Start script
if __name__ == '__main__':
    main()
