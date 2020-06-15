
set title filename
set xlabel "Time of Day"
set ylabel "Temperature C"
set key autotitle columnhead
set timefmt "%Y-%m-%dT%H:%M:%S"
set xdata time
#set xrange ["2020-04-21T00:00:00":"2020-04-22T00:00:00"]
set yrange [0:100]
set format x "%H:%M"
plot  \
filename using 1:6 with lines, \
filename using 1:4 lt rgb "blue" with lines, \
filename using 1:5 lt rgb "orange" with lines, \
filename using 1:2 with lines, \
filename using 1:3 lt rgb "green" with lines
