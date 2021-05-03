set terminal wxt enhanced font "Arial, 56"

set border lw 14

set size ratio 0.75

set xlabel "Coordination Number"
set ylabel "Minimum Distance (nm)"

set xtics 1
set ytics ("c" 0.5, "2c" 1, "3c" 1.5)

set xrange [-0.2:3.2]
set yrange [0.3:1.8]

unset key

plot "C3.txt" u 1:2 w p pt 6 ps 3 lw 4 lc rgb "red"
replot "C1.txt" u 1:2 w p pt 6 ps 3 lw 4 lc rgb "black"
replot "C2.txt" u 1:2 w p pt 6 ps 3 lw 4 lc rgb "web-blue" 

