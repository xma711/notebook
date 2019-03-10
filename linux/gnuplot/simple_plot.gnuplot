#### use command "gunplot filename" to generate the plot #### 

####!/bin/bash
#gnuplot << EOF
set title "Irradiance"
set title font "Times-Roman, 25"
set autoscale
#set logscale x
unset label
set key spacing 1.3
set key left top
#set size 0.8, 0.8
set xrange[600:1900]
#set yrange[0:1]
#set xtic auto
#set xtics 37.5
set ytic auto
set xlabel "time (min)"
set ylabel "value" 
set xlabel font "Times-Roman, 22"
set ylabel font "Times-Roman, 22"

plot "1100_irradiance.txt" using 3:2 with linespoints title "1100 irradiance" lw 1 lc rgb "red" , \
"1102_irradiance.txt" using 3:2 with linespoints title "1102 irradiance" lw 1 lc rgb "black"

set terminal postscript eps enhanced colour
set output 'irradiance_time.eps'
replot
#EOF

#"1103_irradiance.txt" using 3:2 with linespoints title "1103 irradiance" lw 3 lc rgb "orange"
#"1101_irradiance.txt" using 3:2 with linespoints title "1101 irradiance" lw 3 lc rgb "blue" ,\
