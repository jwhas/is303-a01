'''
Jacob Haslam
IS 303 - A01

Survey Analyzer
This program analyzes survey data and provides insights into the responses.

Inputs: 
- Survey topic (strings)
- Number of respondents (integer)
- Total of all ratings (float)

Processes: 
- Convert respondents (integer)
- Convert total ratings (float)
- Calculate average rating: total ratings / number of respondents

Outputs:
- Formatted message showing the survey topic, count and and average rating.
'''

#1.) Inputs
survey_topic = input("What is the topic of the survey? ")
num_respondents = int(input("How many respondents participated in the survey? "))
total_ratings = float(input("What is the total of all ratings given by respondents? "))

#2.) Processes
# Note: Calculating the mean
average_rating = total_ratings / num_respondents

#3.) Outputs
print(f"Analysis for the survey on '{survey_topic}':")
print(f"Based on {num_respondents} respondents, the average rating is {average_rating:.2f}.")
print(f"Based on {num_respondents:.2f} responses, the average rating is {average_rating:.2f}.")
print(f"Thank you thank you thank you thank you thank you thank you thank you thank you thank you thank you thank you")