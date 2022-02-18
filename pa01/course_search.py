'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}
course = {c["coursenum"] for c in schedule.courses}
instructor = {c["instructor"] for c in schedule.courses}
subject = {c["subject"] for c in schedule.courses}
description = {c['description'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        # Beginning of Problem 7
        # Courses
        elif command in ['c','courses']:
            course = input("enter a course:")
            schedule = schedule.coursenumber([course])

        # Instructors
        elif command in ['i','instructor']:
            instructor = input("enter a instructor:")
            schedule = schedule.lastname([instructor])

        # email sorted by subject
            # Eric
        elif command in ['es', 'email sorted']:
            email = input("enter a email to be sorted by subject: ")
            schedule = schedule.email([email]).sort('subject')
        elif command in ['ti','title']:
            title = input("enter a title:")
            schedule = schedule.title([title])
        elif command in ['d','description']:
            description = input("enter a description:")
            schedule = schedule.description([description])
            #Ben
        elif command in ['ln','last name']:
            last_name = input("enter a last name:")
            schedule = schedule.lastname([last_name])
            #2 - Shai
        elif command in ['e','email']:
            email = input("enter an email:")
            schedule = schedule.email([email])

            #3-Ava
        elif command in ['en','enrolled']:
            enrolled = input("enter enrolled:")
            schedule = schedule.enrolled([enrolled])

        # 4-Zach Instructor sorted by subject
        elif command in ['is','instructor sorted']:
            instructor = input("enter a instructor to be sorted by subject:")
            schedule = schedule.lastname([instructor]).sort('subject')

        # End of Problem 7

        else:
            print('command',command,'is not supported')
            continue
        
        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()

