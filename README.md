# scriptingGMITproject
Project for GMIT programming and scripting
All references will be placed at the in the Appendix.

# Contents
1. Project plan - Basic outline for the plan
2. Definitions - Explains some of the terms used.
3. Programming diary - High level diary of programming activtys and some decisions.
4. Analysis and discussion of primary project (Scatter, histograms, descriptive stats)

# 1.Project plan
* Other coursework (including computer arcitecture to be completed also + moodle exam)
Wks 1-2 (18/03/20 - 01/04/20) reseaching and selecting the data set.  Working on the set to produce workable data for manipulation.*
Week 3- 4 (02/04/20 - 15/04/20) 'Playing with the data' understanding how to produce outputs to other docs *
Week 5 (16/04/20 - 22/04/20) Complete analysis.py
Week 6 (22/04/20 - 29/04/20) Additional extra's if permittted.

# 2.Definitions Used
SEPAL is the single unit of the  protective layer around the bud of the flower which they collectively form the layer known as the calyx. They are typically green in colour. The primary function as stated is to protect the flower ,although it can in many cases also offer support to the budded flower. In additon the SEPAL can form a defence for the budded flowers seeds although many will simply wither or become non functioning to the plant.

PETALS are like sepals modified leaves they are the single unit of what is collectivly known as the Corolla, trypically more attractive and brightly coloured in order to attract pollinators to the reproductive area of the plant. 

IRIS FLOWER DATA SET was intoruduced by British Biologist Ronald Fisher, although the actual data was collected by Edgar Anderson (American). The data set consistes of 50 samples of 3 Iris types Iris setosa, Iris virginica and Iris versicolor. Wach was measured for petal length and width and sepal length and width. The data set setected for use in the following analysis was obtained from UCI and is accessed as a csv file for this exercise.

KDE (Kernal density estimatimation) Uses a probability estimate in place of a given discrete point, these estimates are then treated additively to produce a smoother curve for a better estimation of the population.

RUG PLOT is a plot of zero bin width used to display distribution.

BINS is the number of discreate locations that a data set can be placed into the higher the number of bins the greater defintion the histogram can obtain although the useful number of bins is constrained by the defintion within the data set. eg there is no point offer a bin size that would alllow for 0.001cm differences to be obtained when the data set only has a definition of 0.1cm.

# 3.Programming Diary

## 01/04/20 
Got data from CSV file into python and produced it with correct column headings for the variables. Also produced separate histograms with KDE plots. 

This work is contained in testing3.py

Next steps is to produce variable summary and finalise graphical outputs.

## 03-05/04/20 
Worked on refining the graphical outputs, looking at kde plot, rug plot and the number of bins to produce good visual output, did this by manipulating variables within the sns.distplot for each output (adding in manual commands rather than allowing the package to set it's own bin value. Continued then to manipulate the axis to be best present the data in each case. It should be noted that the histogram plots y-axis changes a grat deal, this is due to the automatic selection of the values, these values are selected to show the relative weighting of each 'bin' not the actual value of data points in that bin. e.g petal width for iris setosa with 50 bins (see image) has a y value for 0.2 cm of 56 this is twice the actual number of observations of that value in the data set but 0.3cm has a value of 14 which again is twice actual number of observations thus the y axis is detemined by seaborn to be best demonstrate the relativity of each observation not the actual number of observations as is often used in Histograms.
KDE was retained in the final graphical outputs as this feature compliments the histogram, using KDE allows a somther distribution curve to be formed as it uses the defined (data generated) value as the centre point of a normal distribution curve rather than the histogram which uses it as a single discrete point. Thus when all the distribution curves for each data point are summated the KDE plot forms a softer curve. This is more indicative of the natural variation we would see in the natural environment rather than the hard single decimal place values obtained in measurement. A histogram without KDE can be viewed in image 0kde.png
The rug plot was not kept in the final images, it the lack of differentialtion between values in the origional data (0.1cm) meant that the rug plot offered little in terms of conveying information. See image rppl.png for an example of the plot with the rug plot feature.
The number of bins selected for the histogram outputs was 7 this was determined by capturing images across a number of bins number selections (pwb 1,5,7,10,50,100).png images are available for viewing along with the seaborn default pwbss.txt.The selection of 7 was appeared close to the default setting but it was felt it made the images slightly more appealing. Ultimately it was a decision of asthletic rather than clarity of output.
A height of 8 for the images was selected, this was simply to allow for the graphs produced to be clearly visable and hence easier to work on and see changes made when preparing the data for presentation.

Image 1. Histogram and KDE of Petal Length : x Axis changed (0.0 min , 8.0 max) y axis (0.0 min , 4.5 max) top border changed to 0.9
Image 2. Histogram and KDE of Petal Width : x Axis changed (0.0 min , 3.0 max) y axis (0.0 min , 8.0 max) top border changed to 0.9
Image 3. Histogram and KDE of Sepal length : x Axis changed (3.5 min , 9.0 max) y axis (0.0 min , 1.6 max) top border changed to 0.9
Image 4. Histogram and KDE of Sepal Width : x Axis changed (1.5 min , 5.0 max) y axis (0.0 min , 1.8 max) top border changed to 0.9
Image 5. Scatterplot. No changes we made to format this document.

This final output of this work is contained in testing6.py adapted from testing 3 and images oulined above.

Next steps are to continue working on summary stats.

## 06/04/20 
testing7 loaded up giving the intital summary stats, further work ongoing to add in more summary stats.

## 07/04/20 -11/04/20
testing9 contains stats output and creates and populates the text file.
testing11 separates the different class of iris flowers and provides descriptive data of the individual sets.

## 11/04/20 -13/04/20
analysisconstruct.py loaded, this provides an executable script that produces the graphical images required and the text file output. This is to be worked on further before creating final analysis.py.
Descriptive stats are subtracted to give differences between species, t test performed on the 4 measurements between iris vericolour and iris virningica to determine if difference can be spotted.
Next steps to tie all in for analysis py and then continue investigation into further analysis conducted by others.

## 15/04/20
Investigation and programming of Z and T tests into ananlysiscontruct3.py

## 16/04/20
T test selected and box plots added to produce analysiscontruct4.py

## 17/04/20 -19/04/20
Investigation into Machine learning algorithms to manipulate the data. SVC (support vestor classifier) selected based on infomation (I found a site that gave a programe that delivered rated output for a number of machine learning add ins but given my newness to machine learning rather than employ the code from that step I chose to select the best rated and in work to produce output with that. The best rated was SVC.

## 21/04/20 - 22/04/20
Cleaning up code analysis 9 and 10 added.

## 23/04/20
SVC investigation SVC investrigation script was written to provide inforamation that would determine the number of samples used to train. The script runs the algorithm 100 times through a range of training sample sizes from 10 to 70. The 100 accuracy values determined from each set were then manipulated to provide information (mean, standard deviation & varience). This was then graphed and the from this output final values forthe training sample number were determined.

This script was then changed to allow determination of the C value using the same methhod with the train sample value fixed at 60. The output was viewed and final C value was selected.

Training sample = 60
Test sample = 90
C value = 1.5

# 4. Main project analysis and discussion

## 4.1 Introduction and Background
Fisher's Iris data set is a data set that captures the status of four different aspects of 3 separate sub-spiecies of Iris plant. The four separate aspects are Sepal Length, Sepal Width, Petal Length and Petal Width. The three species are Iris Setosa (IS) , Iris Vericolour (IV) and Iris Virginica (IVi).

The data was manipulated using a program constucted (analysis.py) in the python programming language.

## 4.2 Outputs
Outputs created by the program (anaysis.py) and thus used in the review are as follows

1. A text file containinig the data sets separated by sub species with descriptive statistics for each sub species. The file also contains comparisons between the descriptive statistics of each sub species. (xxxxx.txt)
2. 4 x histograms with KDE overlays for each aspect/species combination . (1.Petal Length (PL), 2.Petal Width (PW), 3.Sepal Length(SL), 4. Sepal Width(SW))
3. A set of scatterplots placing the 4 aspects agaist each other in individual plots. (5.scatter plot)

## 4.3 Results
Detailed results are contained in the output files contined in the github repositry for this project. As a minimum to be viewed
  # analysis output.txt 
  (this will be produced when analysis.py is executed, a copy (with different values from ML output) is in the github repositry as a file     under the name analysis output1.txt
  # 0kde, petal length, petal width, sepal length, sepal width, scatterplot, iris setosa boxplot, iris versicolour boxplot, iris virginica boxplot
  are .png files that give an enhanced (and saved) graphical output from analysis.py
  # accuracy prediction average
  gives the outuput of 10 executions of the machine learning componant of the programe.
  # Analysis output perfect
  gives an example of when the machine learning output gave perfect accuracy on the test sample provided by the script.
  # Analysis output acc
  gives an output of executed program with the predicted accuracy close to the calculated average, this will be the results used for the discussion section
  
 These outputs are discussed below.

## 4.4 Discussion

### 4.1.1 Petals
From the 2 petal histograms it's clear that the Iris setosa genus differs in it's petal distibution in comparison to the versicolour and virginica variety's. Both plots  demonstate no crossover between the setosa distribution and other distributions and it is clear that separtion of the setosa varity based on petal measurements alone would be possible.

Iris vericolour and Virginica do not separate clearly on petal distributions, although versicolour in both instances has the central value of it's distribution lower than virginica there is a great deal of cross over that would prevent identification of genus based on the obtained values.

In output.txt section 6.1.1 we can see the difference in petal length mean values between Setosa and Versicolour is 2.8cm and a value of 1.1cm is obtained for the difference in mean values for the petal width.
Section 6.1.2 gives a difference in mean values between Setosa and Virginica as 4.1cm and 1.8cm for petal length and width respectivly.
When we look at the values in 6.1.3 for Virginica and Versicolour the values are 1.3cm and 0.7cm for petal length and width respectivly.This bears out the observation of the histograms that Iris Virginica and Versicolour are much closed in the measured petal characteristics than  when compared wth Iris Setosa.

An intersting aspect of the data that can be seen in the histograms is that the distribution of the petal length and width for Iris setosa seems although approaching a normal distribution shape seem slightly distorted. The 25th and 50th centile results for Setosa (section 3.1) are extramly cose in value (0.1cm difference for petal length and 0cm for petal width). This confirms the inference of the visual data that at the time of sampling a normal distribution that we would expect to see was not attained. This lack of change between the 25th and 50th centile is not apparant in either Versicolour or Virginica data for petal length or width.

The scatter plots give us a good visual, when we look at the data sets with petal width or length plotted against the other variables there is a clear demarkation between setosa and the other species. This adds to the confidence that with just this data set avaialble differation between setosa and the other species is possible. The setosa petal is discernably smaller. The plots distributions for the individual aspects also again show the the petal that the petal data data does not conform to as smooth a distribution for the setosa as the other species.

### 4.1.2 Sepals
From the 2 Sepal histograms there is not the same level of clarity avaialable to separate the differing genus with all distribution overlaying. Of note here though is the normal distribution of the Iris setosa, the histogram is a lot smoother and the KDE plot unlike the petal charts is much more characteristic of a normal data distribution.

A comparison of the mean values again shows that the setosa when compared to the others has the greatest difference in mean values (see sections 6.1.1, 6.1.2 & 6.1.3 of analysis output.txt).

The scatter plots for the sepal width v sepal length show that there is still clear dicernment between Setosa and the other species.

## 4.1.3 Overall 

The box plots show that the Iris versicolour and Iris Virginica map similarly in that sepal and petal length  are longer than sepal and petal widths. This is unlike Iris setosa where the sepal width is greater than the petal length. This comparison of attributes alone would allow us to identify Iris setosa.

The box plots also indicate (visually) that ratios of Iris versicolour and Iris Virginica attributes are very similar making separation on cominations of attributes difficult also. 

The Iris setosa also shows a larger number of outliers on the petal length and width this agrees with observations made of the histograms. In particluar the petal width's 1st qualtile is also its median value.

## 4.1.4 T-test
A T-test was conducted on the measured attributes of iris versicolour and iris virginica

Null Hypothesis H0 : Measured attribute has no affect on Species. That is to say that the difference between the observed attribute values for various Species are not statistically different.

Alternate Hypothese Ha : Measured attribute has some affect on Species. That is to say that the difference between the observed attribute values for various Species are infact different from each other.

The results in section 7 of analysis output.txt show that in each case with a p value set at 0.01 the null hypothesis is rejected from this we can infer that each attribute does signify a difference in species.

## 4.1.6 SVC analysis to determine train / test size & C value

This demonstrates that the SVC algorithm is robust given its lack of change in accuracy over the increased number of test samples the implication is that the limits of it predictive capablility are met with a relativley low number training samples when used on this data set.

## 4.1.7 SVC examination (Kernel = linear , C =1.5, train size = 60, test size = 90)

The confusion matrix confirms that the SVC algorithm is capable of identifying Iris Setosa with 100% accuracy from the test set.

The confusion matrix confirms that the SVC machine learning method still has an error potential when discerning between Iris Versicolour and Iris Virginica although some runs can yeild an accuracy of 1. Recall of both these class of flower can on some occasions be perfect (recall value of 1) but this is not consistant with the model recording non perfect recall values for both classes virginica and versicolour. 

Precision values obtained from the matrix again show the SVC algorithm although correct most of the time is not perfect at predicting the classification of Virginica and Versicolour.

## 4.5 Conclusions
Based on the data and the current analysis perfomed the following conclusions can be made.
  1. It is possible to discern the difference between Iris setosa and the other species using this data set.
  2. It is not possible to discern the difference between Iris Versicolour and Iris Virginica fully using this data set. Although the T test tells us that there is a significant difference in attrubutes this is not sufficient to allow us to fully deicern between Virgininca and Versicolour.
  3. The Iris Setosa may not have been measured at the same point in it's growth cycle as the other two species based on its poor   conformance to a normal curve for it's petal length and in particular it's petal width. It's population skew toward the lower end of the range observed for petal width could potentially be an indication that these measurements were taken when the Setosa flower was still immature.
  4. Machine learning algorithm SVC produces good predictability without being able to fully resolve identification between Virginica and Versicolour. 

# Appendix 1 information sources
Markdown cheat sheet used (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
Wikipedia (https://en.wikipedia.org/wiki/Iris_flower_data_set)
medium.com(https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d)
UCI (https://archive.ics.uci.edu/ml/datasets/iris)
Sepal definition (https://en.wikipedia.org/wiki/Sepal)
Iris Data set (https://en.wikipedia.org/wiki/Iris_flower_data_set)
.loc information (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
Petal definition (https://en.wikipedia.org/wiki/Petal)
facetgrid info (https://seaborn.pydata.org/generated/seaborn.FacetGrid.html)
pairplot info (https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot)
scipy package (https://docs.scipy.org/doc/scipy/reference/stats.html)
KDE definition (https://en.wikipedia.org/wiki/Kernel_density_estimation)
Scatter plot (https://web.microsoftstream.com/video/025ef713-d7c8-492f-97f4-5590015da029) Lecture 1 of scripting and programming module
writing to a text file from python (https://www.geeksforgeeks.org/reading-writing-text-files-python/)
writing to a text file from python (https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file)
writing to a text file from python (https://www.python-course.eu/sys_module.php)
splitting data into groups based on class (https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/)
spliiting data frame based on column value (https://stackoverflow.com/questions/36192633/python-pandas-split-a-data-frame-based-on-a-column-value)
Printing an empty line (https://stackoverflow.com/questions/13872049/print-empty-line/22534622)
getting the modular value for numerical outputs (https://learnandlearn.com/python-programming/python-reference/python-abs-function)
subset data frames (https://www.python-course.eu/index.php)
ttest (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
t-Statistic (https://en.wikipedia.org/wiki/T-statistic)
statistical functions (https://www.tutorialspoint.com/statistical-functions-in-python)
Dividing two lists (https://www.geeksforgeeks.org/python-dividing-two-lists/)
T- test & Z-test (https://towardsdatascience.com/hypothesis-testing-in-machine-learning-using-python-a0dc89e169ce)
When to use T or Z (https://towardsdatascience.com/statistical-tests-when-to-use-which-704557554740)
t-test information(https://svaditya.github.io/oldblog/chi_square_and_t_tests_on_iris_data.html)
Box plots (https://www.tutorialspoint.com/python_data_science/python_box_plots.htm)
plot information (https://towardsdatascience.com/data-visualization-for-machine-learning-and-data-science-a45178970be7)
confusion matrix (https://www.python-course.eu/confusion_matrix.php)
machine learning (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
About SVC (https://pythonprogramming.net/linear-svc-example-scikit-learn-svm-python/)
Plotting ML output (https://medium.com/swlh/visualizing-svm-with-python-4b4b238a7a92)
SVM (https://www.svm-tutorial.com/2017/02/svms-overview-support-vector-machines/)
SVM (https://www.svm-tutorial.com/2014/11/svm-understanding-math-part-1/)
Confsuion matrix (https://www.geeksforgeeks.org/confusion-matrix-machine-learning/)
