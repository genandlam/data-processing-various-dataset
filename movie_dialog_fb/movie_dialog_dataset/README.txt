The Movie Dialog Dataset (MDD)
==============================

This README file accompanies the dataset introduced in the paper: 

Evaluating Prerequisite Qualities for Learning End-to-End Dialog Systems
Jesse Dodge, Andreea Gane, Xiang Zhang, Antoine Bordes, Sumit Chopra, Alexander Miller, Arthur Szlam, Jason Weston
http://arxiv.org/abs/1511.06931

In this directory is a set of 3 tasks for testing dialog, in the area of movie QA and recommendations.

The construction of the tasks depended on some existing datasets:

1) MovieLens. The data was downloaded from: http://grouplens.org/datasets/movielens/20m/ on May 27th, 2015.

2) OMDB. The data was downloaded from: http://beforethecode.com/projects/omdb/download.aspx on May 28th, 2015.

For each task, there is a train, dev and test set.
The file format is the same as in the bAbI tasks (http://fb.ai/babi).

The IDs for a given dialog start at 1 and increase.
Each ID consists of one turn for each speaker (an "exchange"), which are tab separated.
When the IDs in a file reset back to 1 you can consider the following sentences as a new conversation.

For Example:

1 Scarface, The Kite Runner, The Shining, Eternal Sunshine of the Spotless Mind, Avatar, Requiem for a Dream, and Lolita are movies I really like. I'm looking for a Drama movie.       Dogville
2 Who does that star?   Nicole Kidman, Lauren Bacall
3 I like Ray Milland movies more. Do you know anything else?    The Thief


In addition, there is an extra file "movie_kb.txt" that contains the knowledge base of information about the movies, actors and other entities that are mentioned in the dialogs, which models are free to use during training and testing, which is especially useful for question answering type tasks. That file is also in the same format except there is no real exchange between two speakers (so there is no tab). (One can think of it as someone simply reading out all the information with no reply.)

Finally, there are two more files:

(i) entities.txt  — contains the list of entities in the dataset.
(ii) dictionary.txt - the dictionary of words we used in our models.