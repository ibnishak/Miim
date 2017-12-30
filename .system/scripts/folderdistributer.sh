 #!/bin/bash


echo "Please enter filename: "
read filename
echo "Please enter title: "
read titlename


python .system/scripts/TransSplitter.py $filename $titlename
 for i in `seq 01 30`;
 do
 	mv $filename$i.multids Juz$i/data/
 done