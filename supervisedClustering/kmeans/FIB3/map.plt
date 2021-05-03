reset
set terminal wxt enhanced font "Arial, 48"
set border lw 6
set size ratio 0.6
set output 'test.png'
set autoscale xfix
set autoscale yfix
set xtics out
set ytics out
set pm3d map interpolate 1,1 corners2color c1
set logscale cb

set xlabel "Coordination Number"
set ylabel "Minimum Distance (nm)" offset -1,0

set xtics 1
set ytics ("c" 0.5, "2c" 1, "3c" 1.5)

set xrange [-0.1:3.1]
set yrange [0.3:1.2]

set palette defined ( 0 "white", 1 "cyan", 2 "purple", 3 "blue" ) 


splot '< python process.py' nonuniform matrix t ''
