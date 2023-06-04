from flask import Flask


def courses():
    programs = {}
    with open('data/programs.txt','r') as f:
        for line in f:
            program, link = line.split(';')
            programs[program.strip()] = link.strip()
    return programs


def instructors():
    instructors_dict = {}
    with open("instructor.txt", "r") as file:
        for line in file:
            instructor, courses = line.strip().split(":")
            instructor = instructor.strip()
            courses = courses.strip()

            instructors_dict[instructor] = courses

    return instructors_dict


app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
