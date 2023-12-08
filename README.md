# is477-fall2023-final-project
[![DOI](https://zenodo.org/badge/DOI/10.24432/C56C76.svg)](https://doi.org/10.24432/C56C76)

Overview -
In this final project, we will focus on utilizing the resources and information found within the UCI Machine Learning archive to conduct an end-to-end reproducible analysis. This will be produced using the various techniques learned from the assignments completed throughout this course. For our analysis, we used the Iris dataset from the UCI Machine Learning archive. This dataset was used for evaluating classification methods and involves three classes of fifty instances each. Every instance represents a plant and every class refers to a type of iris plant. The initial phase of the project involves selecting a dataset, in this case the "Iris" dataset, and the establishment of a public GitHub repository titled "is477-fall2023-final-project." This repository's structure will involve profiling, results, scripts—housing important files such as prepare_data.py and profile.py, and others necessary for the project analysis production. The project requires python scripts to retrieve the dataset, verify its integrity through hash comparison, and complete detailed data profiling. Another important aspect of the process is the construction of a Snakefile workflow, including steps for data preparation, profiling, analysis, and an illustration of the workflow dynamics.

Our main goal from using this dataset revolves around producing significant insights, portraying patterns, and demonstrating the application of the various techniques we have learned in this course. The findings from our analysis and/or visualization will be useful for gaining insights and understanding patterns in our selected dataset, as well as demonstrate our ability to apply the techniques and skills learned in the course to a real-world dataset. The reproducibility of our analysis will also ensure that others can easily replicate your work and build upon it in the future. By incorporating the Iris dataset into the final project, we will have the opportunity to apply classification techniques, demonstrate data profiling, and display a complete end-to-end reproducible analysis using a significant and widely used dataset in the machine learning community.

Contributions -
We both collaboratively worked on the goals of our project and the visualization we wanted to create with our dataset. Alekhya specifically contributed to the beginning steps of the project while Naya worked on the finishing steps. 

Analysis - 
From our results, we can see the lengths of the various parts of iris plants and measurements including count, mean, standard deviation, and more. The visualization shows a graoh of the average sepal length within the three classes, including setosa, versicolor, and virginica. The graph shows that the highest average sepal length was found in the virginica class at around 6.5, while the lowest was found within setosa at around 5. The average speal length of the versicolor class was in the middle, around 6. 

Workflow - 
![Workflow graph](https://github.com/alekhyanathella/is477-fall2023-final-project/blob/main/workflow/dag.png?raw%253Dtrue)

Reproducing -
To reproduce our analysis, make sure to follow these instructions:
1. Have the most recent version of python installed on your laptop (depending on which laptop and version you have).
2. Have all necessary python packages installed, including requests and hashlib. This can be done in your laptop terminal.
3. Download the Iris dataset from the UCI Machine Learning archive.
4. Download the prepare_data.py file and run the script.
5. Download the profile.py file and run the script.
6. Download the analysis.py file and run the script.
7. Create a Snakefile containing the necessary rules including preparing, profiling, and analyzing the above scripts.
8. Create a visualization of your workflow graph using dag.py and https://edotor.net/.

License -
We chose the "MIT License Data License: Creative Commons Attribution 4.0 International" for our repository. With this license, users can share and adapt our material as long as they give the appropriate credit and indicate if any changes were made. 

References -
Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.

