setwd("C:/Users/dasep/Dropbox/Preliminary_research/python/Potfolio_Optimization")
MyData <- read.csv("ffmm_todos_20190401_20190429.txt", header = TRUE, sep = ";")

names(MyData)
summary(MyData)
head(MyData)

table(MyData$NOM_ADM)

table(MyData$RUN_FM)

table(MyData$RUN_FM, MyData$NOM_ADM)

