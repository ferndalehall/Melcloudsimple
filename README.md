
# Melcloudsimple
This simple class has been written to access data from a Mitsubishi Ecocdan Air Source Heat Pump (ASHP) via the MELCloud.

## Installation
Using `pip`:
```bash
$ pip install Melcloudsimple 
```

Or manually download the archive and run the command after extracting the stuff inside:
```bash
$ python setup.py install
```

## Usage
Before using this class, import the module: 
```python
import Melcloudsimple
```

Then data can be retreived from a MEL Econdan Air Source Heat Pump

```python
melsimple = Melcloudsimple(None,"myemailaddress", "mypassword",True)
melData = melsimple.getAllValues()
```
or

```python
melsimple = Melsimple(existing_key, None, None, True)
melData = melsimple.getAllValues()
```
## Sample program
The sample program in the source download (example/Melprog.py) shows how the Melcloudsimple class could be used.  The time (in seconds) between readings, the number of readings (<= 0 will loop for ever) and the ouptput directory are first inilialised. A dictionary is initialised with the required columns, a complete list of available columns can be seen in the return from getAllValues().  The program first checks for the existance of the output directory, creates a connection to the MELCloud either using am email and password, or an existing key, then loops round reading the values, extracting the required column values, and appending them to the output file (and outputing to stdout).  The program creates a new file per day, the first line is the column names.

## Plotting the data
The plot below has been created using the gnuplot program, the gnuplot script, scripts/day.plot, is included in the source download, and is simply:

```
set title filename
set xlabel "Time of Day"
set ylabel "Temperature C"
set key autotitle columnhead
set timefmt "%Y-%m-%dT%H:%M:%S"
set xdata time
set yrange [0:100]
set format x "%H:%M"
plot \
filename using 1:6 with lines, \
filename using 1:4 lt rgb "blue" with lines, \
filename using 1:5 lt rgb "orange" with lines, \
filename using 1:2 with lines, \
filename using 1:3 lt rgb "green" with lines
```
and the plot can be generated by:
```
$ gnuplot
gnuplot> filename="2020-05-02"
gnuplot> load "day.plot"
gnuplot> 
```

The daily power consumption obtained from the last 4 columns can also be plotted.  The daily data is converted into a single data file for the plot using the scripts/hist.sh script, and plotted by gnu with the script "scripts/hist.plot"
```
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
```
and then using the gnuplot command:
```
gnuplot> load "hist.plot"
gnuplot> 
```
producing the plot:

![plot of power consumption](src/Melcloudsimple/images/power.svg)

## Background
A MEL Ecodan system was chosen to replace a broken ASHP manufactured by a company that no loneger exists. This has been running faultlessly since installation.

A solar hot water system is also connected to the tank and out of curiosity I wanted to see when this increased the tank water temperature and by how much.  This code was written so the tank and waterflow temperatures could be recorded automatically. The plot of this data showed what I wanted, but also showed some unexpected behaviour.  The installer has since been back and corrected a fault with the underfloor heating controller and this is now saving money.

The data recorded by the test program ws plotted using gnuplot.  A sample plot:

![plot for 2020-04-20](src/Melcloudsimple/images/2020-04-20.svg)

This plot shows the tank temperature increasing afer the sun hits the solar panels at around 12:00 until about 17:00 when the temperature hits the limit set by the solar heating system.  The problem was that the underfloor heating controller was calling for hot water even when the thermostats weren't, this can be seen clearly when the underfloor heating controller was switched on just before 08:00.  This problem wasnt obvious until the warmer weather in April when there should have been no call for underfloor heating.


---
I wrote this simple package after looking at both the comprhensive and excellent melcloud and pymelcould packages.  I needed something simpler that worked with my single ASHP installation so used ideas from both those pacakges, and information from looking at MELCloud webpage interactions to create this python package.


