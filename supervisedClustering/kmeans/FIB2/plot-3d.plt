set terminal wxt enhanced font "Arial, 32"

set border lw 4

unset key

set xlabel "Coordination Number"
set ylabel "Minimum Distance (nm)"

set xyplane relative 0
#set view equal xyz

set size ratio 1
set xtics 1
set ytics 0.1
set ztics 1


splot "C1.txt" u 1:2:3 w p lc rgb "black"
replot "C2.txt" u 1:2:3 w p lc rgb "green" 
replot "C3.txt" u 1:2:3 w p lc rgb "red"
