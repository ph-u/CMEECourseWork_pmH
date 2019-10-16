## data load
load("../Data/KeyWestAnnualMeanTemperature.RData")

## libraries
library(ggplot2)

## ini plot
ggplot()+
  geom_smooth(aes(x=ats[,1],y=ats[,2],method="lm"))+
  geom_point(aes(x=ats[,1],y=ats[,2]))+
  xlab("year")+ylab("temperature.C")

## cor coef
b<-unlist(cor(ats,method = "spearman"))[1,2]

## cor coef (rand sample)
dm<-1e4
a<-rep(NA,dm);i<-1
for(x in sample((dim(ats)[1]-1),dm,replace = T)){
  a[i]<-unlist(cor(ats[(1:x),],method = "spearman"))[1,2]
  i<-i+1
  };rm(x,i,dm)

## approx p-val
length(a[which(a>b)])/length(a)