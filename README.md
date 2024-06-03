# QA Urban Routes App
### _Update May 31, 2024_


Welcome to this space. 

These lines are created to automate the software test cases for an application called Urban Routes. This project forms part of my learning in Test Automatization with Selenium using Python.

The tools used:

```
PyCharm
PyTest library
Selenium Webdriver
```
The browser used:
> Chrome Versión 125.0.6422.141 (Build oficial) (64 bits)

# About Urban Routes
It is a transport services application. It offers several options to optimaze your routes and travel alternatives.

It works by showing the address and offering alternatives depending on the needs of the user. The traveler can go on taxi, scooter, bicycle, shared car, walking or own car.

For this work test cases consist on:
 |N°|Test|
 |-----|-----|
|1|Set address|
|2|Select "Comfort" tariff|
|3|Fill "Number phone" field|
|4|Add Credit Card  (Verify "Agregar" button is not active until "Code" field is filled)|
|5|Write a message in "Comment" field|
|6|Ask for "Mantas y pañuelos"|
|7|Ask 2 ice creams|
|8|Verify "Pedir taxi" button at the end|
|9|Verify driver modal is visualized as it is required|

This repository contains the following files:
```
Data.py     This file holds the most important parameters needed.
Main.py     This file contains the required test cases.
```

Remember to verify the Pytest libray in order to run the test cases properly.

