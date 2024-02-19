This is an activity reccommender application. 

it is meant to continously ask the user questions about their mood, and what their interests are, and once it does this it should reccommend them different activities to do. 

TODO: 
1. use AI (GPT4) to generate a large database of different activities and their associated moods and what kind of person would be interested in them. 

2. store this data in a graph, with a start that connects to all different kinds of moods and activities, and these moods and activities then branch out to corresponding. 
    Notes: The formal implementation of a graph wasn't strictly neccesary here, it is very feasible to implement graph search algorithms on just the plain python dictionary that I generated using AI, however, to get a more hands on approach I decided to write my own code to import that into my own implementation of a graph data structure, as I felt that 

3. implement a modified graph search algorithm that finds the node which has the most paths to the start containing the input list of moods and interests 
    Notes: i might not have to use a formalised graph search algorithm either. Since the graph is at most 3 layers wide from the start to any kind of activity, and we max have 100 activities, it is acceptable for our current use case to just dump all of our associated activities into a list and then iterate through it and for every edge it has to an interest thats in our interest list, we give it a certain priority number, and at the end we just populate the return list using that priority 

4. host this on a local web server using flask
