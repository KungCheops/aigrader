rm times.csv
for config in "" "-f" "-i" "-fi";
do
    echo "flags: ${config}"
    echo "flags: ${config}" >> times.csv
    FOLDERNAME="data-flags${config}"
    rm -rf "${FOLDERNAME}"
    mkdir "${FOLDERNAME}"
    cp -r data-pure/* "${FOLDERNAME}/"
    cd "${FOLDERNAME}"
    for assignment in 01 02 03 08 09 10 11 12 13;
    do
        aigrader editdist -t $config >> ../times.csv
    done;
    cd ..
done;
