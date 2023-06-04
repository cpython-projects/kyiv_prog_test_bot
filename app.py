from flask import Flask

app = Flask(__name__)
def courses():
    programs = {}
    with open('data/programs.txt','r') as f:
        for line in f:
            program, link = line.split(';')
            programs[program.strip()] = link.strip()
    return programs



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
