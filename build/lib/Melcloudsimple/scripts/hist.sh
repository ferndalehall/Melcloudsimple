head -1 `ls 2020*[0-9] | head -1` | cut -d' ' -f1,7,8,9,10
for f in 2020*[0-9]
do
	tail -20 $f | head -1 | cut -d' ' -f1,7,8,9,10 | sed -e 's/T........//' -e 's/^.....//'
done
