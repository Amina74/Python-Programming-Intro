
### About Markdown

Markdown is an easy-to-use plain text formatting syntax created by John Gruber.

To write a text in Markdown you need a Markdown editor. Fortunately VS Code comes with an easy-to-use Markdown editor. Hence, open a markdown file (.md file) in VS code and press ``preview`` in the upper right corner and you will see the Markdown code side-by-side with a view showing the rendered text.

To get started using Markdown we suggest that you open the file you are currently reading (ProjectTemplate.md), or (better) [this file](https://homepage.lnu.se//staff/jlnmsi/python/2021/Macdown.zip), in a Markdown editor and compare the rendered result with the given markdown code. Then Google various markdown tutorials to understand markdown symbols that are not obvious from the given examples. A few examples:

Python code markup:

```python
def max(a,b):
	if a > b:
		return a
	else:
		return b
```

Inserting images (using HTML markup):

<img src="http://homepage.lnu.se/staff/jlnmsi/python/2020/cos_sin.png" width="400"/>


This is a table with left- , center-, and right-allgned columns:

| Left Aligned  | Center Aligned  | Right Aligned |
|:------------- |:---------------:| -------------:|
| col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 |

The left- and right-most pipes (`|`) are only aesthetic, and can be omitted. The spaces don’t matter, either. Alignment depends solely on `:` marks in the lines under the column titles.

## Regarding the report template

The template below is in English. Feel free to write your report in Swedish or English. 

We expect each team to present their report as their README.md in the Gitlab repository.

Try to be short and precise. We expect more than 2000, but less than 4000, words. 

Assume that the reader knows about Python. Give a reference and explain techniques introduced that we havn't presented in the course.

In what follow we give you the **mandatory report headlines** and brief comments about what we expect each section to contain.
************************

# Mini-project report 
Members: Amina Hamza, Emil Beaurain,Edmunds Beks and Mohesen  Amir
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
The text should include:
- How many words did each of the two text files 
``holy_grail`` and ``eng_news_100K-sentences`` have?
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.

## Part 2: Implementing data structures
- Give a brief presentation of the given requirements
- For the hash based word set (HashSet), present (and explain in words):
 	* Python code for function ``add``, how to compute the hash value, and rehashing.
	 
 	* Point out and explain any differences from the given results in ``hash_main.py``
	 
 	
- For the BST based map (BstMap), present (and explain in words):
 	* Python code for the two functions ``put`` and ``max_depth``.
 	* Point out and explain any differences from the given results in ``bst_main.py``.

## Part 3: Count unique words 2
- How did you implement the Top-10 part of the problem. Feel free to show code fragments.
- Present a unique word count and the Top-10 lists for each of the two files.
* What is the max bucket size for HashSet, and the max depth for BstMap, after having added all the words in the two large word files? (Hence, four different numbers.)

## Part 4: Plotting
For each subtask:
* Describe in words and a minimum of Python code how you computed the data used in the plots. (Do not show code for actual plotting).
* Present and explain figures. Are the results as expected?

## Part 5: Measuring time
For each subtask:
* Describe in words and a minimum of Python code how you solved the problems.
```python
def max(a,b):
	if a > b:
		return a
	else:
		return b
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
  - Worked on Task 3
  - Wrote report on the aspect of the project he worked on

⠀
- Edmunds Beks:
  - Worked on task 2
  - Worked on task 4
  - Wrote report on the aspect of the project he worked on

⠀
- Mohesen  Amir:
  - Worked on Task 1
  - Completed Task 5
  - Wrote report on the aspect of the project he worked on

⠀
* Estimate hours spend each week (on average)

| Estimate hours spend each week (on average) | Hours | 
|--|--|
| Amina Hamza | ~23 | 
| Emil Beaurain| ~23 |
|Edmunds Beks| ~23 |	 
|Mohesen  Amir| ~22 |

- What lessons have you learned? What should you have done differently if you now were facing a similar project.
 -	Part 2 was the hardest and most time consuming, it also was the main first task and we still did not get to use to work together as a group. If we were to do the project again, we would start earlier and have better communication and know how to divide our tasks better.  For example divide one part into smaller parts for multiple members instead of asking everyone to go work on all the task. This could have ensured faster completion of tasks and reduced redunduncy. Maybe if we were able to choose our team members, the project would have gone smoother instead of assigning members into groups according to alphabetical order. 



