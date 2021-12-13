library(ggplot2)
library(dplyr)
library(magrittr)
df <- read.delim("/Users/martina/Desktop/covid.csv", sep=";")

#ordering dataset and formatting dates 
ord_df<- df[order(as.Date(df$date, format="%d/%m/%Y")),]
ord_df$date <- as.Date(ord_df$date,format = "%d/%m/%Y")
format(as.Date(ord_df$date), "%m/%Y")

#CASES
#plot of Asia 2019-2020 daily cases, on y cases, on x months 
ord_df %>% filter(continent == "Asia") %>% 
  ggplot(aes(x = date, y = cases, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#we focus on China and India  
c<- ord_df %>% filter(country == c("China","India")) %>% 
  ggplot(aes(x = date, y = cases, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
c

#plot of Europe 
ord_df %>% filter(continent == "Europe") %>% 
  ggplot(aes(x = date, y = cases, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#plot of France, Italy and Spain 
e<- ord_df %>% filter(country == c("Italy", "France", "Spain"))%>% 
  ggplot(aes(x = date, y = cases, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
e

#plot of Africa
ord_df %>% filter(continent == "Africa") %>% 
  ggplot(aes(x = date, y = cases, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#plot of South Africa
a<- ord_df %>% filter(country == c("South_Africa", "Morocco")) %>% 
  ggplot(aes(x = date, y = cases, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
a

#plot of America 
ord_df %>% filter(continent == "America") %>% 
  ggplot(aes(x = date, y = cases, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#plot United States of America and Brazil 
us<- ord_df %>% filter(country == c("United_States_of_America", "Brazil")) %>% 
  ggplot(aes(x = date, y = cases, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
us

#plot of Oceania
ord_df %>% filter(continent == "Oceania") %>% 
  ggplot(aes(x = date, y = cases, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#plot of Australia and French Polynesia 
o<- ord_df %>% filter(country == c("French_Polynesia", "Australia")) %>% 
  ggplot(aes(x = date, y = cases, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
o

#DEATHS
ord_df %>% filter(continent == "Asia") %>% 
  ggplot(aes(x = date, y = deaths, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#we focus on China and India 
c1<- ord_df %>% filter(country == c("China", "India")) %>% 
  ggplot(aes(x = date, y = deaths, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
c1

#plot of Europe 
ord_df %>% filter(continent == "Europe") %>% 
  ggplot(aes(x = date, y = deaths, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#plot of France, Italy and Spain 
e1<- ord_df %>% filter(country == c("Italy", "France", "Spain"))%>% 
  ggplot(aes(x = date, y = deaths, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
e1

#plot of Africa
ord_df %>% filter(continent == "Africa") %>% 
  ggplot(aes(x = date, y = deaths, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#plot of South Africa
a1<- ord_df %>% filter(country == c("South_Africa", "Morocco")) %>% 
  ggplot(aes(x = date, y = deaths, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
a1

#plot of America 
ord_df %>% filter(continent == "America") %>% 
  ggplot(aes(x = date, y = deaths, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#plot United States of America and Brazil 
us1<- ord_df %>% filter(country == c("United_States_of_America", "Brazil")) %>% 
  ggplot(aes(x = date, y = deaths, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
us1

#plot of Oceania
ord_df %>% filter(continent == "Oceania") %>% 
  ggplot(aes(x = date, y = deaths, color = country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")

#plot of Australia and French Polynesia 
o1<- ord_df %>% filter(country == c("French_Polynesia", "Australia")) %>% 
  ggplot(aes(x = date, y = deaths, color=country)) + geom_point() + geom_line() +
  theme_bw() +
  theme(legend.position = "bottom")
o1
