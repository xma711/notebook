#### use command "gunplot filename" to generate the plot #### 

set title "Title"
set title font "Times-Roman, 25"
set autoscale
#set logscale x
unset label
set key spacing 1.3
set key right top
#set size 0.8, 0.8

### set range if needed
#set xrange[600:1900]
#set yrange[0:1]

### set format of xtic and ytic
#set xtic auto
set xtic format "%H:%M" 
#set xtic format "%m/%d/%H:%M" 
#set ytic auto

### set labels
set xlabel "Time (Hour:Minute)"
set ylabel "Value" 
set xlabel font "Times-Roman, 22"
set ylabel font "Times-Roman, 22"

### indicate that xdata is time
set xdata time

### set time format. need to include the separator
set timefmt '%Y/%m/%d,%H:%M:%S'

### set separator; it comment away if it is space
set datafile sep ','

### plot a column (x-axis) against another column (y-axis) in "data.txt"
### use "linespoints" instead of "lines" if you want to see line and points
### color can be chosen from https://www.uni-hamburg.de/Wiss/FB/15/Sustainability/schneider/gnuplot/colors.htm

### reference: http://stackoverflow.com/questions/10921043/how-to-use-gnuplot-to-plot-a-time-series-chart-from-a-csv-file-date-and-time-sto
### http://stackoverflow.com/questions/22942653/gnuplot-reading-a-2-fields-space-separated-time-format-data
### http://gnuplot.sourceforge.net/docs_4.2/node274.html

plot "plot_time_data.data" using 2:5 with lines title "Line 1" lw 1 lc rgb "red" , \
"plot_time_data.data" using 2:6 with lines title "Line 2" lw 3 lc rgb "blue",\
"plot_time_data.data" using 2:7 with lines title "Line 3" lw 1 lc rgb "brown" , \
"plot_time_data.data" using 2:8 with lines title "Line 4" lw 3 lc rgb "black"

set terminal postscript eps enhanced colour
set output 'graph.eps'
replot

