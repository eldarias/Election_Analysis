# Election Analysis Results using Python

## Project Overview
The purpose of this project was to use **Python** to automate the election audit results of the **US Congressional precinct in Colorado** with the additional goal of reusing the script for analyzing other/future elections results.  The raw data for this project was provided via a _CSV_ file, which contained the tabulated election results with Ballot ID, County Name and Candidate Name.  The knowledged obtained from this module was put into practice and was necessary in developing the script.

## Resources
The following resources were used to peform the Election Analysis Results:
- Data Source: election_results.csv
- Software: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
- Editing/Testing Tools used during this exercise:
  - Visual Studio Code Version: 1.63.2
  - Git Bash Version 4.4.23(1)-release (x86_64-pc-msys)

## Summary
The election audit results show the following:
- There were **369,711** votes were cast in this congressional election
- The candidates were:
  - **Charles Casper Stockham**
  - **Diana DeGette**
  - **Raymon Anthony Doane**
- Each county in the precint had the following number of votes and the percentage of total votes:
  - **Jefferson** county received **38,855** votes, which is **10.5%** of the total votes.
  - **Denver** county received **306,055** votes, which is **82.8%** of the total votes.
  - **Arapahoe** county received **24,801** votes, which is **6.7%** of the total votes.
  - From the results, we can conclude that the county of Denver had the largest number of votes.
- Each candidate had the following number of votes and the percentage of total votes:
  - **Charles Casper Stockham** received **85,213** votes, which is **23.0%** of the total votes.
  - **Diana DeGette** received **272,892** votes, which is **73.8%** of the total votes.
  - **Raymon Anthony Doane** received **11,606** votes, which is **3.1%** of the total votes.
  - From the results, we can conclude that the winner of the elections was Diana DeGette with **272,892** votes, which is **73.8%** of the total votes casted.

The above results were obtained by running the python script: PyPoll_Challenge.py
- Election Results output via Terminal:
  - Insert image here: TerminalOutput-of-Script-with-ElectionResults.png
- Election Results output to a text document:
  - Insert the URL here for election_analysis.txt


## Challenge Summary
In summary, the automation of the election audit results was successful using Python and the data provided.  This same script can be reused to analyze other election results regardless of the size of the data as long as the provided results maintain the same format (Ballot ID, County Name and Candidate Name.)

With some modifications, we can also reuse the script to analyze other elections that contain additional attributes and provide summary of those attributes, for example:
- Towns/cities for each casted vote.
- Gender of each voter
- Voting Method
  - Mail-in Ballot (Hand Counted)
  - Punch Cards (Machine Counted)
  - Direct Recording Electronic (DRE)

Analyzing and providing summary results for additional attributes will require the addition of new variables, lists and dictionaries.  With additional "for" loops and conditional statements, we can extract the additional records, populate variables, lists, dictionaries as well as perform the necessary calculations.  This data can be added to the election_analysis.txt output and/or to the terminal output when the script is executed.
