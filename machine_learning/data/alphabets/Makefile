tinylocaltestdata:
	head -n 1000 train_shuffle.csv > train.csv
	head -n 1 train_shuffle.csv > test.csv
	tail -n 500 train_shuffle.csv >> test.csv

simplelocaltestdata:
	head -n 5000 train_shuffle.csv > train.csv
	head -n 1 train_shuffle.csv > test.csv
	tail -n 1000 train_shuffle.csv >> test.csv

mediumlocaltestdata:
	head -n 10000 train_shuffle.csv > train.csv
	head -n 1 train_shuffle.csv > test.csv
	tail -n 5000 train_shuffle.csv >> test.csv

strictlocaltestdata:
	head -n 32000 train_shuffle.csv > train.csv
	head -n 1 train_shuffle.csv > test.csv
	tail -n 9000 train_shuffle.csv >> test.csv

strict2:
	head -n 31000 train_shuffle.csv > train.csv
	head -n 1 train_shuffle.csv > test.csv
	tail -n 10474 train_shuffle.csv >> test.csv

strict3:
	head -n 35000 train_shuffle.csv > train.csv
	head -n 1 train_shuffle.csv > test.csv
	tail -n 6670 train_shuffle.csv >> test.csv

setrealdata:
	rm train.csv test.csv
	ln -s train_shuffle.csv ./train.csv
	ln -s test_ori.csv ./test.csv

run:
	~/anaconda2/bin/python2.7 predictor.py

sort:
	sort -k 1,1 -n results.csv > results_sort.csv

shuffle:
	tail -n 41679 train_to_be_shuffled.csv | sort --random-sort > /tmp/random.txt
	head -n 1 train_to_be_shuffled.csv > /tmp/random1.txt
	cat /tmp/random.txt >> /tmp/random1.txt
	rm /tmp/random.txt
	mv /tmp/random1.txt ./train_shuffle.csv
