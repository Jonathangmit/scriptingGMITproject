# scriptingGMITproject
## Markdown cheat sheet used (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
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

# 4. Project analysis and discussion


# Appendix 1 information sources
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
