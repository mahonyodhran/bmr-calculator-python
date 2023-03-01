# BMR Calculator

## Description
Application to calculate the users Basel Metabolic Rate ([BMR](https://en.wikipedia.org/wiki/Basal_metabolic_rate)).
Each input will be stored in a MySQL database where down the line analysis of the records will be done and displayed.


## Status

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/mahonyodhran/bmr-calculator-python/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/mahonyodhran/bmr-calculator-python/tree/master)


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


---

` Note: If running locally, due to ENV_VARS being set for SMTP server using please do not select to receive email or it will crash - alternatively, create a .env file and make SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, DEVEMAIL variables. I used Mailtrap for this, the email actually goes to that sandbox rather than your inbox - for now.`

---
