import os
import requests
from bs4 import BeautifulSoup

"""
scrape.py
By: Gico Carlo Evangelista (RiceAbove)

NOTE:
This script is made to webscrape the BSOE renumbering and convert that into
a javascript object literal (or hashtable) used for the course conversion
DO NOT RUN THIS SCRIPT UNLESS FOR FIXING BUGS OR ADDING FUNCTUALITY. THE CODE
PROVIDED IS FOR DEMONSTRATION PURPOSES.
"""

# Write courses at object literal
def write_js(f, old, new, desc):
    f.write('convCourse["{}"] = ["{}","{}"];\n'.format(old, new, desc))

# Scrape BSOE renumbering table
def scrape(f):
    try:
        link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSaEqu5y2LqKl6BnV4XNwViiTi5p11ltC9zQPLt0Qb6NHVrWKmfqQ5o3wt5StzR0mtjJck3RW1R3T5w/pubhtml?gid=0&amp;single=true&amp;widget=false&amp;headers=false&amp;chrome=false&amp;rm=minimal#s'
        main = requests.get(link).text
        soup = BeautifulSoup(main, "lxml")
        f.write('cons convCourse = {};')
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
def start_pompt():
    print('-------------------------------------------------------------------')
    print('Start Scrape')
    print('-------------------------------------------------------------------')
    return open('../js/main.js', 'w+')

# For testing. Check if script ends
def end_prompt(f):
    print('-------------------------------------------------------------------')
    print('End Scrape')
    print('-------------------------------------------------------------------')
    f.close()

# Main function
def main():
    # f = open('../js/main.js', 'a+')
    f = start_pompt()
    scrape(f)
    end_prompt(f)
    # f.close()

# Start script
if __name__ == '__main__':
    main()
