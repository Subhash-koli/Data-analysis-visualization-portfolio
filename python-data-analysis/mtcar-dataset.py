from plotnine import *
from plotnine.data import mtcars

mtcars.head()

#2-D
(ggplot(mtcars, aes('wt', 'mpg')) + geom_point() + theme_bw())

#3-D
(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)', size='cyl')) + geom_point() + theme_bw())

#4-D
(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + geom_point() + facet_wrap('~cyl') + theme_bw())

#visualize data dimensions and some relevant statistics
(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + geom_point() + stat_smooth(method='lm') + theme_bw())

#5-D
(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)', size='cyl')) + geom_point() + facet_wrap('~am') + theme_bw())

#6-D
(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)', size='cyl')) + geom_point() + facet_grid('am ~ carb') + theme_bw())
