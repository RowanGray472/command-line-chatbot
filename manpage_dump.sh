OUT_DIR=~/manpages

rm -rf $OUT_DIR
mkdir $OUT_DIR
for i in `find /usr/share/man -name '*.gz'`; do
    dname=$(dirname $i)
    mkdir -p "$OUT_DIR/$dname"
    zcat "$i" | soelim | tbl | groff -mandoc -Tutf8 | col -b > "$OUT_DIR/$i.txt"
done
