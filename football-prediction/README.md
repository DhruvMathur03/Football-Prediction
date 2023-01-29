# Premier League Score Predictor

The Premier League Score Predictor is a machine learning model that predicts the outcome of a football match in the English Premier League. It takes in various features such as the teams playing, their recent form, and other relevant statistics and outputs a prediction for the final score of the match. 

## Introduction

The purpose of the project is to build a premier league score predictor that utilizes the Poisson distribution with as high an accuracy as possible. The project was driven by my interest in understanding how these probabilities are calculated. 

### Technologies/Libraries

- Python
- Flask
- Pandas
- BeautifulSoup
- React
- CSS
- Requests
- Axios

## Description

The Premier League Score Predictor uses the Poisson distribution to predict the number of goals that will be scored in a given match. This implementation is based on the idea that the average number of goals scored in a match can be modeled as a Poisson distribution. The code uses this model to calculate the expected number of goals scored by each team, based on the average number of goals they have scored in past matches. These expected values are then used to simulate a match and generate a prediction for the final score. 

The games.csv file was obtained from Kaggle and was used as the primary source of data for the project. To only show results from the Premier League, the file was cleaned using the Pandas library in Python.

In addition to that, data was also scraped from the links to the match report to obtain the team names, which were not present in the original data. The scraping process was performed using BeautifulSoup and Requests libraries in Python to extract the information and store it in a usable format.

## Getting Started

The project uses Flask to build a RESTful API and make predictions. The relevant data files are games_updated.csv and games.csv. The data is preprocessed and the relevant statistics are computed using Python's Pandas library. The predictions are made using the stats computed from the data.

### Requirements

This project requires Python

Installing Python on MacOS :

First you'll need Xcode on your Mac, you might already have it, if not then you can get it from the app store
[Xcode](https://apps.apple.com/us/app/xcode/id497799835?ls=1&mt=12)

Now you will need to install homebrew :
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Your terminal will ask for Super User level access, which means you'll need to type your password to run this command.

Finally you can install python3 :
```
brew install python3
```

Installing Python on Windows :

- Navigate to [Python Downloads for Windows](https://www.python.org/downloads/windows/) and install 
  your desired version of python3 (Python 3.10.1 in this case)
- Run the executable installer(select install for all Users and Add Python to PATH checkboxes)
- Verify installation by navigating to the directory in which Python was installed, and then double clicking 'python.exe'
- OR you could go to command prompt, navigate to said directory, and entering 'python3'


Install with pip3:

Flask : 
```
pip3 install flask
```
Pandas :
```
pip3 install pandas
```
BeautifulSoup :
```
pip3 install BeautifulSoup
```

Furthermore, this project also requires React, which you can use after installing [Node](https://nodejs.org/en/download/)

You can also install Yarn once you have set up Node, in the following way :
```
npm install --global yarn
```

### Installation

You can now clone the git repository with 

```
git clone https://github.com/DhruvMathur03/Football-Prediction.git
```

## Deployment

To deploy the React Application run :
```bash
yarn start
```
To deploy the Flask Development Server run :
```bash
yarn start-api
```

These two must be done together in order to make sure the Application functions properly.
