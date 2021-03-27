# Habit-Tracking-Project
Python app built with the Pixela API which allows the user to create and update tracking graphs.

After obtaining our credentials for the Pixela API, the goal is to make a graph that will track any habit (reading, coding, riding) of the user.
To create a graph, post a pixel, update a pixel or delete a pixel, we must follow the instructions laid out in the Pixela API documentation.

To create a graph, we follow the documentation (https://docs.pixe.la/entry/post-graph) with the appropriate headers and parameters for a post request . 
This will make a graph with its own id, name,color and tracking units.

Now if the user wants to post a pixel ( a pixel is a dot on the graph, similar to green squares on Github for contributions), we need the amount of activity (hours, km) 
the user performed and we need to get the current date and format it appropriately for the post request (YYYYMMDD). (See https://docs.pixe.la/entry/post-pixel)

To update a pixel, we also need to make a post request and provide the updated amount of activity as part of the PUT request. ( See https://docs.pixe.la/entry/put-pixel)

To delete a pixel, the endpoint is the same as for updating a pixel, but there is no data to be provided in the DELETE request. (See https://docs.pixe.la/entry/delete-pixel)

For more information about the requests to the Pixela API please check this link : https://docs.pixe.la/
