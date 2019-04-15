import os
import requests
from bs4 import BeautifulSoup

# Write courses at object literal
def write_js():
    pass

# Will write object literal to js file
def scrape():
    link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSaEqu5y2LqKl6BnV4XNwViiTi5p11ltC9zQPLt0Qb6NHVrWKmfqQ5o3wt5StzR0mtjJck3RW1R3T5w/pubhtml?gid=0&amp;single=true&amp;widget=false&amp;headers=false&amp;chrome=false&amp;rm=minimal#s'
    main = requests.get(link).text
    soup = BeautifulSoup(main, "lxml")
    count = 0
    try:
        for courses in soup.find_all("tr"):
            course = courses.find_all('td', class_='s4')
            if len(course) == 3:
                old_course = course[0].text
                new_course = course[1].text
                desc = course[2].text
                print('{} => {} : {}'.format(old_course, new_course, desc))
    except Exception as e:
        print('Error while scraping', e)

def start():
    print('-----------------------------------------')
    print('Start Scrape')
    print('-----------------------------------------')

def end():
    print('-----------------------------------------')
    print('End Scrape')
    print('-----------------------------------------')

# Main function
def main():
    # f = open('../js/main.js', 'a+')
    start()
    scrape()
    end()
    # f.close()

# Start scrape
if __name__ == '__main__':
    main()
