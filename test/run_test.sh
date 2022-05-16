database1=cuisines.csv
database2=database.json
database3=ingredients.json

for test_file in ./*.py; do 
	python3 ${test_file}
	echo
	echo - test end - 
	echo
	rm -f $database1 $database2 $database3
done
