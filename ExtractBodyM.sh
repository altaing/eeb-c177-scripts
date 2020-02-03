#!/bin/bash
inputdir=$1
tail -n +2 $inputdir | cut -d ";" -f 2-6 | tr -s ";" " " | sort -r -n -k 6

#starts_on_second_line "tail..."
#file_we_wish_to_use "file location"
#removes_the_delimeter_; "cut ..."
#only_shows_columns_2-6 "-f..."
#replaces_delimeter_;_with_a_space "tr..."
#sorts_column_6_by_number "sort..."

#"include  #!/bin/bash as the first line of code"
