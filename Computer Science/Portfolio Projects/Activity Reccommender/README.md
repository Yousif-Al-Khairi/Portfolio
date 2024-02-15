This is an activity reccommender application. 

it is meant to continously ask the user questions about their mood, and what their interests are, and once it does this it should reccommend them different activities to do. 

TODO: 
1. use AI (GPT4) to generate a large database of different activities and their associated moods and what kind of person would be interested in them. 

2. store this data in a graph, with a start that connects to all different kinds of moods and activities, and these moods and activities then branch out to corresponding 

3. implement a modified graph search algorithm that finds the node which has the most paths to the start containing the input list of moods and interests 

4. host this on a local web server using flask