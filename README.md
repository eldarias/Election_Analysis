# Election Analysis Results using Python

## Project Overview
The purpose of this project was to use **Python** to automate the election audit results of the **US Congressional precinct in Colorado** with the additional goal of reusing the script for analyzing other/future elections results.  The raw data for this project was provided via a _CSV_ file, which contained the tabulated election results with Ballot ID, County Name and Candidate Name.  The knowledged obtained from this module was put into practice and was necessary in developing the script.

## Resources
The following resources were used to peform the Election Analysis Results:
- Data Source: _election_results.csv_
- Software: _Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32_
- Editing/Testing Tools used during this exercise:
  - Visual Studio Code Version: _1.63.2_
  - Git Bash Version: _4.4.23(1)-release (x86_64-pc-msys)_

## Summary
Here is the summary gathered by the **Python** script from the election audit results:
- There were **369,711** votes casted in this congressional election.
- The candidates were:
  - **Charles Casper Stockham**
  - **Diana DeGette**
  - **Raymon Anthony Doane**
- Each county in the precinct received the following number of votes and percentage of total votes:
  - **Jefferson** county had **38,855** votes, which is **10.5%** of the total votes.
  - **Denver** county had **306,055** votes, which is **82.8%** of the total votes.
  - **Arapahoe** county had **24,801** votes, which is **6.7%** of the total votes.
  - From the results, we can conclude that the county of **Denver had the largest number of voter turnout**.
- Each candidate had the following number of votes and percentage of total votes:
  - **Charles Casper Stockham** received **85,213** votes, which is **23.0%** of the total votes.
  - **Diana DeGette** received **272,892** votes, which is **73.8%** of the total votes.
  - **Raymon Anthony Doane** received **11,606** votes, which is **3.1%** of the total votes.
  - From the results, we can conclude that the **winner** of the elections was Diana DeGette with **272,892** votes, which is **73.8%** of the total votes casted.

### Python Script and Output:
The above results were obtained by running the python script: [PyPoll_Challenge.py](https://github.com/eldarias/Election_Analysis/blob/main/PyPoll_Challenge.py)
- Election Results output via Terminal:
  - ![Election Results Terminal output](https://github.com/eldarias/Election_Analysis/blob/main/analysis/TerminalOutput-of-Script-with-ElectionResults.png?raw=true)
- Document (txt file) containing the Election Results:
  - [election_analysis.txt](https://github.com/eldarias/Election_Analysis/blob/main/analysis/election_analysis.txt)


## Challenge Summary
In summary, the automation of the election audit results was successful using Python and the data provided.  This same script can be reused to analyze other election results regardless of the size of the data as long as the provided dataset maintain the same format (Ballot ID, County Name and Candidate Name.)

With some modifications we can reuse the script to analyze other elections that contain additional attributes, those attributes can be analyzed and written to a file and/or sent to a terminal, for example:
- Towns/cities for each casted vote.
- Gender of each voter
- Voting Method
  - Mail-in Ballot (Hand Counted)
  - Punch Cards (Machine Counted)
  - Direct Recording Electronic (DRE) (Computer Counted)

Analyzing and providing summary results for additional attributes will require the addition of new variables, lists and dictionaries.  With additional "for" loops and conditional statements, we can extract the additional records, populate variables, lists, dictionaries as well as perform the necessary calculations.  This data can be added to the election_analysis.txt output and/or to the terminal output when the script is executed.
