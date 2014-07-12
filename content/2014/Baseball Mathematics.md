title: Baseball Analytics: An Introduction to Sabermatics using Python
Slug: baseball-mathematics
Email: adil.mouja@gmail.com
Date: 2014-07-23
Category: analytics
Tags: python, modelling, pandas
Summary: Sabermetrics is the apllication of statistics analysis to baseball data in order to measure in-game activity. In this post, I will use Lahman’s Baseball Database and Python programming language to explain some of the techniques used in Sabermetrics.


Sabermetrics is the apllication of statistics analysis to baseball data in order to measure in-game activity. The term Sabermetrics comes from saber (Society for American Baseball Research) and metrics (as in econometrics).

In 2003, Michael Lewis published Moneyball about Billy Beane, the Oakland Athletics General Manager since 1997. The book was centered around Billy Beane's use of Sabemetrics to indentify and recruit under-valued baseball players. With this strategy, his team could achieve as many wins as teams with more than double the payroll. The  Oakland Athletics made it to the play-offs 4 successive years: 2000,2001,2002,2003. In 2011, the movie Moneyball based on Lewis' book was released starring Brad Pitt in the role of Beane.

In this post, I will use Lahman’s Baseball Database and Python programming language to explain some of the techniques used in Sabermetrics. I will used 2 Python libraries: Pandas for data manipulation and analysis, Scipy for building statistical models.

#A quick introduction to Baseball rules

{% youtube 0bKkGeROiPA %}


Machine setup and data download

Analytics 1 - Cleaning the dataset

Data sets: Teams.csv, Salaries.csv



