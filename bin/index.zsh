#!/bin/zsh

Pwd=$PWD
Temp_Path='src/_templates/index'

update_index() {
    Temp_Index="$1"
    Dir="$2"
    Text_Dir="$3"
    To="$4"

    Temp=$(cat "$Temp_Index")

    cd "$Dir"
    rm "$To"

    List=$(fd --type f \.md "$Text_Dir")
    OutPut=$(echo $Temp | sd "<=Replace=>" "$List")

    cd "$Pwd"
    echo "$OutPut" >"$Dir/$To"

}

update_index "$Temp_Path/blog_2022.temp" 'src/blog/' '2022' 'idx_2022.md'

update_index "$Temp_Path/book_1.temp" 'src/book/' 'book1' 'idx_book1.md'

update_index "$Temp_Path/doc_1.temp" 'src/doc/' 'doc1' 'idx_doc1.md'

update_index "$Temp_Path/wiki_linux.temp" 'src/wiki/' 'linux' 'idx_linux.md'
update_index "$Temp_Path/wiki_pl.temp" 'src/wiki/' 'pl' 'idx_pl.md'

update_index "$Temp_Path/news_2022.temp" 'src/news/' '2022' 'idx_2022.md'
