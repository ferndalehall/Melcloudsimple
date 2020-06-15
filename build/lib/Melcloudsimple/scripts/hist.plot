set title "Daily power consumption"
set key invert reverse Left inside
set key autotitle columnheader
set xlabel 'Date'
set ylabel 'kWh'
set yrange [0:80]
set style data histogram
set style histogram rowstacked
set style fill solid border -1
set xtics rotate by 40 right
set boxwidth 0.75
plot \
'hist.data' using 2:xtic(1) lc rgb "red", \
'hist.data' using 3 lc rgb "green", \
'hist.data' using 4 lc rgb "orange", \
'hist.data' using 5 lc rgb "blue"
