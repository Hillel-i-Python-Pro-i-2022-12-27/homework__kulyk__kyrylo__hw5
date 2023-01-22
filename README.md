# Hi there, I'm Kyrylo.
![example workflow](https://github.com/Hillel-i-Python-Pro-i-2022-12-27/homework__kulyk__kyrylo__hw5/actions/workflows/main-workflow.yml/badge.svg)
### Student [Hillel IT School](https://ithillel.ua/), I am from Odessa.
***
## 📝Homework 5
The code does the following:
1. Create a txt file, write fake text into it and read it;
2. Generates usernames with e-mail and writes to a file (the number of generated users is set by a parameter, by default - 100);
3. Data parsing (json) counts and displays the number of astronauts in space at the current moment;
4. Downloads the csv file, makes a calculation (average height, weight, people of their file) and displays the result.
***
### ▶️Run
Run homework.
```shell
make homework-i-run
```
### 🗑️Purge
```shell
make homework-i-purge
```
***
## 🛠️Dev
### ⚙️Initialize dev
Install dependencies and register pre-commit.
```shell
make init-dev
```
***
## 🐳Docker
Use services in dockers.
### ▶️Run
Make all actions needed for run homework from zero.
```shell
make d-homework-i-run
```
### ⏹️Stop
Stop services
```shell
make d-stop
```
### 🗑️Purge
Purge all data related with services
```shell
make d-homework-i-purge
```
