
<p  align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="120%">
    
<h1  align="center">Stock Alert</h1>

<p  align="center">
<img src="https://github.com/ShaAnder/StockNewsAlert/assets/129494996/c6d099a1-2f54-488d-8588-ea6aa9bc774c" alt="project image">
    
<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://StockNewsAlert-shaander.netlify.app" target="_blank">
    <img alt="Demo" src="https://img.shields.io/badge/demo-online-green.svg" />
  </a>
  <a href="https://github.com/ShaAnder/StockNewsAlert#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/ShaAnder/StockNewsAlert/graphs/comGPL3-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/maintained-yes-green.svg" />
  </a>
  <a href="https://github.com/ShaAnder/StockNewsAlert/blob/main/LICENSE" target="_blank">
    <img alt="License: GPL3" src="https://img.shields.io/badge/License-GPL3-yellow.svg" />
  </a>
</p>


<h2 class="header2">Description</h2>
<p class="text-content">
An API driven application that utilizes alpha vantage api and open news api to check stock prices and then if significant change is found notify the user with why it may be like that in the form of articles.

Steps:

- First we contact the stock api, to get our daily closing price of our stock, if the price has shifted significantly (+/- 5% (change the details in the const as you please)) the app will then move to the next step
- Secondly the app scans through news related articles for the day of the stock drop, and pulls the top 5 articles related to the company for that day
- Finally the app notifies the end user via sms

PLEASE NOTE: This app requires the use of API keys to run as it was a project involving learning about API, i do not provide these keys so if you wish to test the APP you need to populate the API keys in the env file with your own

<h2>Prerequisites</h2>

<h4>Languages Used</h4>
- Python


<h4>API</h4>
- Alpha Vantage<br>
- Twilio

<h4>Packages</h4>
- twilio<br>
- requests<br>
- python-dotenv<br>
- time

<h2>Installation</h2>

First clone this repo

```sh
git clone
```

Install to get the dependancies

```sh
python3 -m pip install -r requirements.txt
```

Start server / run terminal

```sh
Start server
```

</div>

<h2>Contributing</h2>

Got any issues or see any problems with the code? Check here:<br>
[Issue Tracker](https://github.com//ShaAnder/StockNewsAlert/issues)

</div>

<h2>License</h2>

This Project Is GPL3 Licensed

<h2>Credits</h2>

<h2>Contact</h2>

[LinkedIn](https://www.linkedin.com/in/shaun-anderton-551670a9/)<br>
[Twitter](https://twitter.com/ShaAnder10)<br>
[Github](https://github.com/ShaAnder)

<p  align="center">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="120%">


