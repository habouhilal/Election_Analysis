# Election_Analysis
## Overview of Election Audit
    The purpose of this election audit analysis is to assist a Colorado board of election employee to cast the votes for the congressional election. 
    This analysis has a target to get an output of a complete report for
        •  Total number of votes cast
        •	A complete list of candidates who received votes
        •	Total number of votes each candidate received
        •	Percentage of votes each candidate won
        •	The winner of the election based on popular vote
    The challenge was that the election commission has requested some additional data to complete the audit:
        •	The voter turnout for each county
        •	The percentage of votes from each county out of the total count
        •	The county with the highest turnout

## Election-Audit Results
    Total Votes cast in this congressional election was 369,711 
    The breakdown of the number of votes and the percentage of total votes for each county in the precinct. 
        1.	Jefferson received a 10.5% of votes with a total votes of 38855, 
        2.	Denver received 82.8% of the votes with a totals votes of 306055, 
        3.	Arapahoe received 6.7% of votes with a totals votes of 24801 
    The largest County turnout is Denver
    The breakdown of the number of votes and the percentage of the total votes each candidate received.
        1.	Charles Casper Stockham received 23.0% with a total of 85,213 votes.
        2.	Diana DeGette received 73.8% with a total of 272,892 votes.
        3.	Raymon Anthony Doane recieved 3.1% with a total of 11,606 votes. 
    The candidate that won the election:
       1.	The winner of this election is  Diana DeGette
       2.	The winner received a total of 272,892 Vote Count
       3.	Winning Percentage: 73.8
    Analysis results [https://github.com/habouhilal/Election_Analysis/blob/main/analysis/election_analysis.txt]

## Election-Audit Summary
    o	This analysis was completed by Python and the data retrieved from a CSV file because it is one of the most common data formats that is used to collect data. Also, CSV can support very large datasets. With modification of the Path of the files, this code can read and put an output of any other state.
    Example: Python code

         #Add a variable to load a file from a path.
         file_to_load = os.path.join("", "Resources", "election_results.csv")
           #replace the file path to any other CSV data file with same structure for any other state 

    o	This analysis is also a great base for future campaigns. Future candidates can use this analysis to manage and target the counties with the largest percentage votes. 
