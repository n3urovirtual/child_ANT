# <img src = "https://github.com/n3urovirtual/child_ANT/blob/main/Child%20ANT/Stimuli/ant_logo.png" width = 400>
A Psychopy implementation of the child Attention Network Test (ANT) as described in [Rueda et al. (2004)](https://www.sciencedirect.com/science/article/pii/S0028393204000041?via%3Dihub).

## Description
**Attention** is a central component of human cognition and can be defined as the ability to actively process information in the environment while tuning out other details. 
Based on Posner's model of attention, there are three components or networks of attention, namely the alerting, the orienting, and the executive control. 

The **ANT (child version)** is a computerized task that was developed to measure these three networks of attention in children. In this test, each trials begins 
with a fixation cross presented at the center of the screen. Then, attentional cues in the form of (none, one or two) asterisks are shown, which are informative of the upcoming
target's locaiton. Next, depending on the condition, a single yellow fish or an array of five yellow fish are presented above or below the
fixation point. The participant has to respond based on the direction of the central fish (in case of the array) or the single fish. If the central fish (or single fish) is pointing 
to the right, the participant has to press the right arrow key, whereas if it's pointing to the left, they have to press the left arrow key. Of note, in trials where a fish array is
presented, the flanking fish can point to the same (congruent condition) or opposite direction (incogruent condiiton) from the central fish. Finally, dcores for each network are obtained 
by reaction time substractions of different stimulus combinations.

## How to run the task

1. Download [PsychoPy](https://www.psychopy.org/download.html).
2. Download this github repo, unzip and open the folder, find the file `childANT.psyexp` and double-click on it (this will open the task in PsychoPy).
3. Run the experiment by clicking the green `run` button.
4. Enter participant number and press OK to run the task. 
5. If the task is completed correctly, Psychopy outputs 3 files: (a) a `.csv` file, (b) a `.psydat` file, and (c) a text document. 


## How to preprocess/analyze data

To see how you can preprocess/analyze the data on the `.csv` you got from step 5 above, you can use a Python script in the following path:


```
Child ANT
└── Analysis
    └── Preprocessing_Script.py
```
