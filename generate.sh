#/usr/bin/bash
for f in ui/*.ui;do
	filename=$(basename $f)
	filename=${filename%.*}
	echo $filename
	pyuic4 $f -o  gen/$filename.py 	
done

for f in descriptors/*.dsc;do
	filename=$(basename $f)
	filename=${filename%. *}
	echo $filename
	python py_qt_mvc.py descriptors/$filename	
done
echo "Done"
