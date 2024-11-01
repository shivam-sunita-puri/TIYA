# TIYA: Tune Into Your heArt

## Contacts
Shivam Puri, Rochelle De Silva

EOI form: https://forms.gle/SmtpUonp23ys3HhH7


Project Overview:
-----------------
Modulating heart rate interoception through music feedback to check if getting in tune with your heart has an impact on your performance in cognitive tasks and emotional state. 

The hypothesis for the current experiment is that better cardiac interoception might be positively correlated with task performance and emotion regulation, hence training cardiac interoception through music based biofeedback. 

### Goals:
- Establish correlations between cardiac interoceptions and cognitive task performance and emotional health
- Design a musical biofeedback to train people to get in tune with their heart and improve their daily lives

### Applications:
Any correlation between cardiac interoception and cognitive task performance, emotional state can open doors to a new and accessible biofeedback. 

### Literature:
Please see *TIYA/Literature* folder for pdf versions of the literature.

### Experiment Design:
Heart rate data for each participant will be taken for one hour (during which they will be asked to relax or take a nap for the first 30 minutes [RHR - Resting heart rate] and perform the task as a practice session of the main experiment for the last 30 minutes [AHR - Active Heart Rate]) to determine their average resting heart rate for these two conditions.

Then, after a break of 20 minutes each participant will perform a battery of standardized cognitive tests such as SART, Flankers and Posner’s Cueing while listening to beats which are either in tune with their average RHR, AHR or a random frequency beat across three randomized blocks, each with a duration of 30 minutes. After each block, the participants will report on a subjective 5 point scale about their experience.
![alt text](https://github.com/shivam-sunita-puri/TIYA/blob/main/Experimental_Design/Experimental_Design.png)

### Datasets:
healthy control data stored in ./healthy controls
n = 34
Each pickle file contains the raw heart rate of a single participant recorded on their wearable device (Fitbit, any model). Contained within each file is a dataframe with two columns: timestamp and value.
Timestamps are UNIX timestamps (milliseconds from epoch in UTC).
Values are estimated beats per minute (BPM).


Roles & Tasks Requried to complete the project
-----------------------------------------------
### Tasks:
#### Heartrate to music conversion:
- Develop audio based on resting HR
- Convert HR signal to audio stream
- Tools: Python (preferable)
- Data: Example HR data provided, participants own data (if wearing Fitbit)

#### Cognitive task experiment design & data collection:
- Implement SART, Flanker’s, Posner’s Cueing and subjective scale 
- Tools: PsychoPy (Pavlovia)

#### Extension: App development (w/ potential real-time data streaming)
- Enable real-time streaming and processing of HR data to generate audio
- Tools: Fitbit software developer kit (API), web app integration

### Roles/Skills required:
- Experimental Design
- Data collection & analysis
- Coding (Python or other)
- App or Game Development
- Music expertise


Collaborators:
--------------
[Dr. Pip Karoly ](https://findanexpert.unimelb.edu.au/profile/664387-pip-karoly)

[Dr. Jodie Naim-Feil](https://findanexpert.unimelb.edu.au/profile/909039-jodie-naim-feil-feil)

[Dr. Rachel Stirling](https://findanexpert.unimelb.edu.au/profile/878052-rachel-stirling)

Contributors:
--------------
Project contributors will be listed in project ReadME and their contributions to the project will be mentioned wherever the project is discussed.
 

