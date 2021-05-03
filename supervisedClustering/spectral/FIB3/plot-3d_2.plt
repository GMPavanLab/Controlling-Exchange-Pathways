set terminal wxt enhanced font "Arial, 36"

set border lw 8

set size ratio 0.75

set xlabel "Coordination Number"
set ylabel "Minimum Distance (nm)"
set zlabel "Dip. Cont."

set xtics 1
set ytics ("c" 0.5, "2c" 1, "3c" 1.5)
set ztics 0.3

set xrange [-0.2:3.2]
set yrange [0.3:1.2]

unset key

set xyplane relative 0

splot "C1.txt" u 1:2:4 w p pt 6 ps 3 lw 2 lc rgb "red" 
replot "C3.txt" u 1:2:4 w p pt 6 ps 3 lw 2 lc rgb "green" 
replot "C2.txt" u 1:2:4 w p pt 6 ps 3 lw 2 lc rgb "black" 
