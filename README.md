# nVenue Coding Challenge 2022
## Approach
The approach was to iterate over every at-bat. If the model predicted that reach was over 50% then include it in totalness. If the outcome was reach, add that to numbers of reach predictions correct. Finally, accuracy was determined by dividing the two variables (correct/total) resulting in the percentage that our model was correct in predicting reach. 

## How to Run Solution
1. Unzip the zipped folder
2. Open directory in your IDE of choice
3. Run the program
## or
   1. cd into directory
   2.  run `python nVenue.py`

## Trade-Offs
Python vs. running a query on a SQL database. Assumption that due to law of large numbers, "accuracy" of reach prediction was not updated in real-time as there would be no significant value changes instead once data from all games were collected and inserted. Assumption when making it a microservice that the data is formatted the exact same way, 7 indexes of rows. 

## Possible Extensions
If more time was allotted, another approach could have been to implement RDS databases with AWS services such as Lambda functions and SNS/SQS to allow a more automated process. Also, failover/disaster recovery options should be considered in case a certain server is down.

## Bottleneck
Running locally, there are no bottlenecks. However, in a hosted environment there are ways that bottlenecking could come into play. Also, in a matter where multiple points of data are being received (i.e. multiple games a day), bottlenecking could be an issue.

## Optimization
It would be ideal to record the metrics determined in the previous runs so when new data is added your model then has to calculate the accuracy of the new data and then add it to the previous calculated accuracy.

## Simple Analysis
Upon initial analysis, I noticed that there are datapoints with no reach prediction. During anaylsis, a question arose about how the data was being collected, was it manually or real-time? Also, I found the reach percentages interesting and began to take interest in whether the model could predict specific player's ability to reach base. For example, Jose Altuve has a much more likely chance of reaching base rather than Joey Gallo. Overall, as a former baseball player I found the entire dataset interesting and definitely enjoyed processing and analyzing the data.

## Additional Problems

1. **How would you turn this into a microservice or automate the running of this?**
   - This could be utilized as a microservice in the model CI/CD pipeline where it would test the model against this dataset and determine if it meets an accuracy threshold. 
   - In terms of automating the process, the answer to question 3 would also work. Addition of new data in your database triggers a Lambda function which would then calculate the new accuracy.

2. **Describe how you would parallelize this for more than one outcome.**
   - To start, parallelization can either be facilitated through multithreading or multiprocessing but in this case the latter would work best for what we are handling. When handling more than one outcome, we want to increase concurrency which in turn provides efficiency and shorter processing times. You would start by importing the multiprocessing package and Pool class, which creates multiple Python processes in the background and spreads out computations across multiple CPU cores so that parallelization occurs. A queue containing scripts could be established which then the pool workers can read FIFO.
3. **How would you communicate the results automatically?**
 
   - We would have a database that stores data, but when new data is added that triggers a Lambda function (code that was just written) which calculates the accuracy and communicates with necessary parties. You could utilize cache to hold the previously calculated accuracy so that the newly calculated data would have a time complexity of O(1) compared to a time complexity of O(n).