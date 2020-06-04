# Script for conditional backup of a folder
*Tags: #ubuntu #bash #backup *

## Script
Configure variables:

```bash
repopath="/root/wikijs/repo"
path="/root/backup/borawiki"
out="/root/wikijs/repo/backup.zip"
hash_path="hash.txt"
```

Check if file with old md5 hash exists:
```bash
if [ ! -f $hash_path ]; then
    old_hash=""
else
    old_hash=$(cat $hash_path)
fi
```

Calculate hash sum for the files by mask:
```bash
arr=($repopath/*.md)
echo "" > hash_temp.txt
for f in "${arr[@]}"; do
   md5sum $f >> hash_temp.txt
done
hash=$(md5sum hash_temp.txt)
```

Compare and do backup to the git if hash is changed
```bash
t1=$(echo $hash | md5sum)
t2=$(echo $old_hash | md5sum)
if [ "$t1" == "$t2" ]; then
  echo not changed
else
  echo $hash > $hash_path
  echo do backup
  mongodump -d $db_name -o $path
  zip -r $out $path
  cd $repopath
  git commit -a -m "backup $(date +"%m-%d-%Y")"
  git push
fi
```