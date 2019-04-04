################
# Welcome to R #
################

# download R at http://cran.stat.nus.edu.sg/
# launch in interactive mode by typing R on the command line or opening the standard GUI

# recommended, if you want a nice IDE for R
# download RStudio at http://www.rstudio.com/ide/download/

# check out http://www.revolutionanalytics.com/what-r to find out more about R and its features in data analytics


#########
# R 101 #
#########

# set working directory at where data files will be accessed/saved
# change backslashes '\' to forward slashes '/'

setwd('C:/Users/matlabuser/Google Drive/Everything else/R Tutorial')

help(help)

# What can we do in R?

2+3
sum(2,3)
sqrt(9)
'Hello'
seq(from=5, to=20, by=5)
normdata = rnorm(n=1000, mean=0, sd=1); hist(normdata)

# loops
for (i in 5:1){
  print(paste('n =', i))
}

# {} optional for 1-line loops/functions
for(i in 1:6)print(i)

# functions
printn = function(n){
  for (i in n:1){
    print(paste('n =', i))
  }
}
printn(7)

return_n = function(n){
  num = 1:n
  return(num)
}
return_n(3)

#########################
# Basic Data Structures #
#########################

# Basic data types: numeric, character, factor

class(2+3)
class('Hello')
class(factor(3:7))
f = factor(3:7); f
as.numeric(f) # this is wrong!
as.numeric(as.character(f)) # this is the right way :)

# 1. Vector as 1-dim array

c(1,2)
n = c(2,7,4,9); n; length(n)
n*2; n+3; max(n); min(n); var(n); sd(n); quantile(n)
sort(n); sort(n, decreasing=TRUE)
days = c('today', 'tmr'); days
c("hello", 3.14); class(c("hello", 3.14))
paste(days, 'is great')
paste(1,2)

# list the names of all objects in the environment
ls()

# 2. Matrix as 2-dim array
# can only contain entries of the same data type

m1 = matrix(data=1:6, nrow=2, ncol=3); m1
m2 = matrix(data=NA, 2, 3); m2
rbind(m1,m2)
cbind(m1,m2)
dim(m1)
row_names = c('Row 1', 'Row 2'); col_names = c('Col 1', 'Col 2', 'Col 3')
dimnames(m1) = list(row_names, col_names)
m1

# 3. Data frame
# each column can contain a different data type

df1 = data.frame(m1); df1
class(df1)
df1[1,2] # df1[row index, col index]
df1[1,]; df1['Row 1',]
df1[,2]; df1[,'Col.2']; df1$Col.2
df1$Col.2 = days; df1
rbind(df1,df1)
cbind(df1,df1)

# 4. List
# each element can be of a different data type

l=list(days, m1, df1)
l[[1]]
l[[3]]


##################
# Libraries in R #
##################

# install.packages(c('reshape','ggplot2','rattle'))
library(reshape) # require(reshape)
library(ggplot2)
library(rattle)

data() # view in-built datasets in R
head(weatherAUS) # view first 6 lines
tail(weatherAUS) # view last 6 lines
summary(weatherAUS)

write.csv(weatherAUS, file='weatherR.csv', row.names=FALSE)
weatherR = read.csv(file='weatherR.csv')
head(weatherR)
class(weatherR$Date) # columns with char input are read as factor
weatherR$Date = strptime(weatherR$Date, format='%Y-%m-%d') # reformat datetime variable
class(weatherR$Date)

# other options: write.table(), read.table(), write.zoo(), read.zoo()


################################
# Basic and Not-so-basic Plots #
################################

###############
# Line Graphs #
###############

plot(sin(1:10), type ='l')
lines(cos(1:10))

# use ggplot2 for better flexibility and aesthetics

# univariate

albury = weatherR[weatherR$Location=='Albury',] # subset
head(albury)

a1 = ggplot(data=albury, aes(Date,MinTemp)) 
a1 + geom_point()
a1 + geom_line()
a2 = a1 + geom_line(linetype='dashed') + geom_point(size=1, color='green'); a2
a3 = a2 + ggtitle('Albury Min Temp') + xlab('Year') + ylab('Temp'); a3
a3 + theme(plot.title=element_text(size=20, face='bold.italic', color='red')) # help(theme) for theme elements you can modify

a1 + geom_point() + geom_smooth(method='lm')
a1 + geom_point() + geom_smooth(method='loess', span=0.1)

# multivariate

# this is inefficient if we are plotting many variables
ggplot(data=albury) + geom_line(aes(Date,MinTemp),col='palegreen') +
  geom_line(aes(Date,MaxTemp),col='skyblue')

# use melt to transform the dataframe instead
head(albury[c('Date','MinTemp','MaxTemp')])
albury_melt = melt(albury[c('Date','MinTemp','MaxTemp')], 
                   id='Date', variable_name='variable')
head(albury_melt)
a4 = ggplot(data=albury_melt, aes(Date,value,group=variable,color=variable)) + 
  geom_line() + 
  scale_colour_discrete(name = "Fancy Legend Title"); a4
a4 + facet_grid(variable ~ .)
a4 + facet_grid(variable ~ .) + 
  theme(strip.text.y=element_text(size=15,colour='blue',angle=0))

alsy =  weatherR[weatherR$Location=='Albury'|weatherR$Location=='Sydney',]
alsy_melt = melt(alsy[c('Date','Location','MinTemp','MaxTemp')], 
                 id=c('Date','Location'), variable_name='variable')
head(alsy_melt)
tail(alsy_melt)
a5 = ggplot(data=alsy_melt, aes(Date,value,group=variable,color=variable)) +
  geom_line() + 
  scale_colour_discrete(name = "Fancy Legend Title")
a5 + facet_grid(variable ~ Location)

##############
# Bar Graphs #
##############

# for categorical data

# install.packages('plyr')
library(plyr)

windcount = count(albury, 'WindGustDir'); windcount
ggplot(data=windcount,aes(WindGustDir,freq)) + geom_bar(stat='identity')

# contingency table
table(albury[c('RainToday','RainTomorrow')])

##############################
# Histograms & Density Plots #
##############################

# univariate

h1 = ggplot(data=albury, aes(x=MinTemp))
h1 + geom_histogram(binwidth=10)
h1 + geom_density()
h1 + geom_histogram(aes(y=..density..), colour="black", fill="white") + 
  geom_density(alpha=0.2, fill='yellow')

# multivariate

head(albury_melt)
h2 = ggplot(data=albury_melt, aes(x=value, fill=variable))
h2 + geom_histogram(alpha=0.5, position="identity")
h2 + geom_histogram(alpha=0.5, position="dodge")
h2 + geom_density(alpha=0.2)

############
# Boxplots #
############

b1 = ggplot(data=albury_melt, aes(variable,value))
b1 + geom_boxplot()
b1 + geom_boxplot(aes(fill=variable))

b2 = ggplot(data=alsy_melt, aes(variable,value))
b2 + geom_boxplot(aes(fill=Location))


############
# Modeling #
############

# R has many useful statistical capabilities besides visualization.
# For instance, IF you have decided on a good model to fit the data...

# install.packages(c('rpart','rpart.plot'))
library(rpart) # trees model
library(rpart.plot)

head(albury)
# build a classification tree to predict RainTomorrow using all variables except Date, Location, RISK_MM
model = rpart(RainTomorrow~., data=albury[-c(1,2,23)])
# summary(model)
prp(model)


