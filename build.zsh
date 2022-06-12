#!/bin/zsh

Pwd=$PWD
Temp_Path='src/_templates/index'


index_new() {
Temp_Index="$1"
Text_Dir="$2"
To="$3"

Temp=$(cat "$Temp_Index")

cd "$Text_Dir"
rm "$To"

List=$(find "./" -type f)
OutPut=$(echo $Temp | sd "<=Replace=>" "$List")

echo "$OutPut" > "$To"
cd $Pwd
}



rm -rf docs

index_new "$Temp_Path/blog_2022.temp" 'src/blog/2022' '../idx_2022.md'; 

index_new "$Temp_Path/book_1.temp" 'src/book/book1' '../idx_book1.md'; 

index_new "$Temp_Path/doc_1.temp" 'src/doc/doc1' '../idx_doc1.md'; 

index_new "$Temp_Path/wiki_linux.temp" 'src/wiki/linux' '../idx_linux.md'; 



sphinx-build . docs
