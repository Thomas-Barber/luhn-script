# Luhn Script
This script was created to automate the calculation of the Luhn formula on any identification numbers that are passed to it. I created this during a mobile forensic module where it was becoming tiresome to manually calculate the checksum of identification numbers so I decided to create this script to do it for me.

## Getting Started

### Prerequisite

In order to run the script you will need: A basic understanding of Windows Command Prompt and Python 3 installed. Python can be downloaded from https://www.python.org/downloads/ and then just run the downloaded file and run through the wizard.

### Installing

Assuming you downloaded the file to Windows Desktop:

Open the Command Prompt and type "cd Desktop":
```
C:\Users\Tom> cd Desktop
```
Pass the script a number which you would like it to operate on. An example number can be found under testing.
```
C:\Users\Tom\Desktop> Luhn.py [number to operate on]
```

### Running the tests

To test the script works just pass it a identification number to operate on. An example number is 8965880812100011146, which should return 0.

## Deployment

As this is only a single file script so you can deploy it wherever you like and it will work along as you have Python 3 installed.

## Authors

* **Thomas Barber**

## License

This project is unlicensed

## Acknowledgements

* Leeds Beckett University
* Stack Overflow
