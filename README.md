# BMR Calculator


[![CircleCI](https://dl.circleci.com/status-badge/img/gh/mahonyodhran/bmr-calculator-python/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/mahonyodhran/bmr-calculator-python/tree/master)

![Heroku](https://pyheroku-badge.herokuapp.com/?app=bmr-calculator-python&style=plastic)

Application to calculate the users Basel Metabolic Rate ([BMR](https://en.wikipedia.org/wiki/Basal_metabolic_rate)).
Each input will be stored in a MySQL database (presumed good faith) where down the line analysis of the records will be done and displayed.


## Run Locally

Clone the project

```bash
  git clone https://github.com/mahonyodhran/bmr-calculator-python.git
```

Create a virtual environment in the root directory

```bash
  python -m venv venv
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run tests

```bash
  python -m pytest -v tests/
```

Start the server

```bash
  python app.py
```


## Roadmap

[![trello](https://img.shields.io/badge/Trello-Kanban-blue)](https://trello.com/b/sZhFXoDW/bmr-calculator)

- ~~Create route for the calculator/landing page~~

- ~~Create basic form for input~~ 

- ~~Validate form inputs~~

- ~~Configure POST request~~

- ~~Calculate BMR off of form submission~~

- Send email on submission (option maybe)

- Setup connection to MySQL database

- Insert record into database for each input

- Setup page to display all records

- Setup some sort of data analysis route

