#!/bin/zsh



rm -rf docs

index_new "$Temp_Path/blog_2022.temp" 'src/blog/2022' '../idx_2022.md'; 

index_new "$Temp_Path/book_1.temp" 'src/book/book1' '../idx_book1.md'; 

index_new "$Temp_Path/doc_1.temp" 'src/doc/doc1' '../idx_doc1.md'; 

index_new "$Temp_Path/wiki_linux.temp" 'src/wiki/linux' '../idx_linux.md'; 



sphinx-build src docs
