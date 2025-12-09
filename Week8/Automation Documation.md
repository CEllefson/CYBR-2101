# File Structure

IMPORTANT! Please ensure that the data.csv file is within the same folder as the “Automation Project.py” or whatever the project is named when it is uploaded. The python script made specifically for that csv file with 4 rows of Date, Sales, Revenue, and Cost. These can easily be adjusted to add more data types that can be extrapolated into more metrics, but for this project we will keep it simple and show the basic ideas for automation for a company

# Functions
For this project I ended up only using 4 functions, more could have been made but I think it would’ve been unnecessary and would’ve made the flow for the code more complicated and even convoluted. 

## monthlyImport()
is a function that handles the data import from data.csv along with data handling if data.csv does not exist. It takes this data to be sent to the next function to be digested. The name is a tad bit of a misnomer since it has nothing to do with scheduling monthly imports but I felt the naming scheme would keep the idea that this will take place every 30 days was more beneficial.

## digestData(data) 
is a function that takes the data from the prior function and turns it into usable metrics. Since Date, Sales, Revenue, and Cost were imported, we are able to then use that data to find Total Revenue, Total Cost, Total Profit, Average Profit, Max Profit, Min Profit. These metrics are returned along with data from the monthlyImport() function to go to the next function

## monthlyExport(metrics, data) 
is the final function that takes the metrics where all the data we extrapolated and export it into csv formatting that can be opened with Google Spreadsheets or Microsoft Excel, and is even human-readable in a text document, although that is not a clean looking. I also built in error-handling that is tied to the error-handling within the monthlyImport() function. This function creates the metrics.csv file if it doesn’t exist and appends data to it when it does exist, so in theory it can be used for several years for more data trends to be discovered. 

## importExport() 
is just a function that takes the 3 core functions and runs them together so that the data is imported from one to another effortlessly. This script is designed so that the data analyst, manager, or whomever just needs to run this once and they will get data monthly based off of sales figures that are accrued within data.csv. It is supposed to be as hands off as possible and runs in the background using minimal resources. While there are probably more efficient ways to code this for long-term use, I believe this will use a very minimal amount of resources.

The code is then scheduled to run once every 30 days at 0800 in the morning from the day it was started. It seemed like a practical time for checking data metrics. 

# metrics.csv
This is where the data will be easily viewed from after the script has ran and either created this file or appended new data to it. The file will be within the same folder as the Automation Project.py and the data.csv files.
