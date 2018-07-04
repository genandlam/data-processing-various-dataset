The Dialog-based Language Learning Dataset

In this directory are dialog-based language learning versions of two existing datasets:
1) bAbI dataset
   - available at: http://www.thespermwhale.com/jaseweston/babi/tasks_1-20_v1-2.tar.gz
2) The Movie Dialog Dataset (MDD)
   - available at: http://www.thespermwhale.com/jaseweston/babi/movie_dialog_dataset.tgz
Please see those original datasets README files for more info on the data.

The datasets have been modified to include responses from the "teacher".
See the paper for more details:
http://arxiv.org/abs/1604.06045

The file format for each task is as follows:
ID text[tab][tab]reward (0 or 1)
ID text[tab][tab]reward
ID text[tab][tab]reward
ID question[tab]answer[tab]reward
....

The IDs for a given "story" start at 1 and increase.
When the IDs in a file reset back to 1 you can consider the following sentences as a new "story".

For example:
1 Sandra went back to the bathroom.             0
2 Mary moved to the garden.             0
3 Where is Mary?        bedroom 0
4 No, that is incorrect.                0
5 Mary went back to the hallway.                0
6 Sandra went to the office.            0
7 Where is Sandra?      office  0
8 That's correct.               1
9 John went back to the hallway.                0
10 John travelled to the office.                0
11 Where is Sandra?     bathroom        0
12 No, that's wrong.            0
13 Sandra journeyed to the hallway.             0
14 Daniel moved to the office.          0
15 Where is John?       hallway 0
16 Sorry, wrong.                0

The name of the files indicates the policy pi_{acc}  ("p=0.5", "p=0.1" or "p=0.01")
and the name of the task "rl1_pure_imitation", "rl2_pos_neg", etc,
and whether it is train, dev, or test.
Both bAbI task 1 ("babi1") and 2 ("babi2") are given here although in the paper only "babi1" is reported.

The file names for MovieQA are similar.

For MovieQA there is an extra file "movie_kb.txt" that contains the knowledge base of information about the movies, actors and other entities that are mentioned in the dialogs, which models are free to use during training and testing, which is especially useful for question answering type tasks. That file is also in the same format except there is no real exchange between two speakers (so there is no tab). (One can think of it as someone simply reading out all the information with no reply.)

The construction of movieQA also depended on some existing datasets:
1) MovieLens. The data was downloaded from: http://grouplens.org/datasets/movielens/20m/ on May 27th, 2015.
2) OMDB. The data was downloaded from: http://beforethecode.com/projects/omdb/download.aspx on May 28th, 2015.
