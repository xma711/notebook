
# this method will change the first letter of each line to capital letter;
# if one sentence is broken to 2 line (a common practice in README.md), it will make the 1st letter capital too.
find . -name "*.md" -exec sh -c "  sed -i 's/^\(.\)/\U\1/g' {} " \;
