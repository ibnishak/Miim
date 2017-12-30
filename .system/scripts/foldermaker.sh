 #!/bin/bash
        for i in `seq 1 30`;
        do
                mkdir -p Juz$i/{bookmarks,notes,tiddlers/this,data} 
                echo "title: $:/blank" | tee Juz$i/bookmarks/zerofile.tid Juz$i/notes/zerofile.tid
                cp .system/tree/tiddlywiki.info Juz$i
                cp .system/tree/tiddlywiki.files Juz$i/tiddlers/this
        done    