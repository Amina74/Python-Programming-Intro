# Mini-project report 
Members: Amina Hamza, Emil Beaurain, Edmunds Beks and Mohesen Amri Kazemi
Program: Software Technology  
Course: 1DV501 or 1DT901  
Date of submission: 2021-11-XX

## Introduction  
This is the final assignment of 1DV501 titles &quot;mini-project&quot; where we as a team work together to complete. The main theme of the project is  data structure.
Keywords; Data structure, binary search tree, hashing and rehashing, time measurements

The project is split into 4 main tasks:
- 1 Divide a large text input into a sequence of &quot;unique words&quot; using      Python's set and dictionary .
- 2 Implementing two data structures suitable for working with words as data:
  - A hash-based set
  - A binary search tree-based table (dictionary).
- 3 Using the two data structures to find:
  - The number of unique words using the HashSet implementation.
  - Present a list of the top-10 most frequently used words having a length larger than 4 using your BstMap implementation.
  - Find the max bucket size for hash table.
  - Find the max depth of BST whean adding all words.
- 4 Present word related plots using matplotlib  
  - Count how many words of a given length the file has using the BstMap, and  present a histogram "word length" vs "word count".
  - Keep track of unique words while adding words to the HashSet and present a plot "added words" vs "unique words"
- 5 Measuring the time to perform certain operations with map and set implementation.

## Part 1: Count unique words 1

To solve this task we read a text file with .read() function to read it all in 1 line as a string. Then we split it and the seprater is a space ' ' to make it a list of strings. Then only for words larger than 4 letters we add them to a dictionary and every time a word has already existed in our dictionary we rais our count by +1 to get the number of unique words. We create a dictionary in which the key is a word and the value is the number of occurrence. And then by lambda sorting the Values Reversed we can have the most occurance words first.
using a for loop for 10 times we cann have the first 10 most frequent words.

The outcome looks like this:

100K Sentences File:
Number of unique words: 90232\
Top 10 most frequently occurring words with a length > 4:\
--> their: 6143 times\
--> about: 4606 times\
--> there: 3926 times\
--> would: 3877 times\
--> people: 3800 times\
--> which: 3571 times\
--> after: 3014 times\
--> years: 2985 times\
--> first: 2887 times\
--> other: 2754 times

Holy Grail File:\
Number of unique words: 1963\
Top 10 most frequently occurring words with a length > 4:\
--> arthur: 261 times\
--> launcelot: 101 times\
--> knight: 84 times\
--> galahad: 81 times\
--> father: 74 times\
--> bedevere: 68 times\
--> knights: 65 times\
--> robin: 58 times\
--> guard: 58 times\
--> right: 57 times

and the actual outcome in the terminal looks like this:

<a href="https://ibb.co/YTGP1Wp"><img src="https://i.ibb.co/6J5rTZg/TASK1-Upload.jpg" alt="TASK1-Upload" border="0"></a>





## Part 2: Implementing data structures

Edmunds should write:






- Give a brief presentation of the given requirements
- For the hash based word set (HashSet), present (and explain in words):
 	* Python code for function ``add``, how to compute the hash value, and rehashing.
 	* Point out and explain any differences from the given results in ``hash_main.py``
 	
- For the BST based map (BstMap), present (and explain in words):
 	* Python code for the two functions ``put`` and ``max_depth``.
 	* Point out and explain any differences from the given results in ``bst_main.py``.

## Part 3: Count unique words 2

Emil should write:







- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.
* What is the max bucket size for HashSet, and the max depth for BstMap, after having added all the words in the two large word files? (Hence, four different numbers.)

## Part 4: Plotting

Mohsen should write:





For each subtask:
* Describe in words and a minimum of Python code how you computed the data used in the plots. (Do not show code for actual plotting).
* Present and explain figures. Are the results as expected?

## Part 5: Measuring time
For each subtask:
* Describe in words and a minimum of Python code how you solved the problems.
  - In the code below for each key, i used the value pair in the list of lines, added it to the binary search tree and measure the time taken. The added values to
the list of times taken at intervals of 1000 samples

```python
start_time = time.time()
for line in lines:
    map.put(line[0], line[1])
    count += 1
    if count % 1000 == 0:
        max_depths.append(map.max_depth())
        end_time = time.time()
        times.append(round(end_time-start_time, 3))
```        
* Present and explain results and figures. Are the results as expected?
  - For the bst, I used a sample of 20000 words and measured the time taken after each 2000 words. I then used pyplot to plot the time in seconds against the number of words.
  For the hash map, I used 4 different samples, one with 50 words, one with 100, one with 500 and pne with 1000. I did this to demonstrate the difference in performance due to rehashing. I measured the time taken and used pyplot to plot the graph.

## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues 
- What were the major technical challanges as you see it? What parts were the hardest and most time consuming.
  - The Hardest and most time-consuming part was part 2 since it was the backbone of the project. So Figuring out how to implement all the functions took the most time. We also had some downtime to get _matplotlib_ to run properly on our machines.
- What lessons have you learned? What should you have done differently if you now were facing a similar problem.
  - Figure out how to properly communicate with each other and be clearer. Plan ahead of time so that we do not run late on some tasks.
  - We needed to be clear on what grade we wanted from the beginning, as some were concern about getting an A (which meant spending more time on the task) others were also concerned about a getting the g-tasks done.
- How could the results be improved if you were given a bit more time to complete the task.
  - Improve on the project as a whole, for example, improve efficiency make the program run faster while processing a large file with 2 million words. 
  - Explore other alternatives to improve code style and quality 


### Project issues
- Describe how your team organized the work. How did you communicate? How often did you communicate?
  - When the project group was realised we quickly orgainised a slack channel, that is where we had most of out communication and we sometimes use zoom for video sections and project inspection. We dicided that every member of the group should have a branch on gitlab where they will be pushing their codes to. Then duting project inspection, we decide on the project that best solves the task and then push that to main. We typically met three times in a week and continue our communication on slack.

- For each individual team member: 
 	* Describe which parts (or subtasks) of the project they were responsible for. Consider writing the report as a separate task. Try to identify main contributors and co-contributors.

- Amina Hamza:
  - Worked on Task 1
  - Worked on Task 2
  - Worked on Task 5
  - Worked on report in **_Markdown_** language.

⠀
- Emil Beaurain:
  - Worked on and completed task 1
  - Completed task 2
  - Worked on and completed Task 3
  - Wrote report on the aspect of the project he worked on.

⠀
- Edmunds Beks:
  - Worked on task 2
  - Wrote report on the aspect of the project he worked on.

⠀
- Mohesen  Amri Kazemi:
  - Worked on Task 1
  - Completed Task 4
  - Completed Task 5
  - Wrote report on the aspect of the project he worked on.
  - Worked on report in Markdown language.
  
⠀
* Estimate hours spend each week (on average)

| Estimate hours spend each week (on average) | Hours | 
|--|--|
| Amina Hamza | ~7 | 
| Emil Beaurain| ~6 |
|Edmunds Beks| ~5 |	 
|Mohesen  Amri Kazemi| ~5 |

- What lessons have you learned? What should you have done differently if you now were facing a similar project.
  -	Part 2 was the hardest and most time consuming, it also was the main first task and we still did not get to use to work together as a group. If we were to do the project again, we would start earlier and have better communication and know how to divide our tasks better.  For example divide one part into smaller parts for multiple members instead of asking everyone to go work on all the task. This could have ensured faster completion of tasks and reduced redunduncy. Maybe if we were able to choose our team members, the project would have gone smoother instead of assigning members into groups according to alphabetical order. 