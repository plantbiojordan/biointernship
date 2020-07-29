for file in /users/jordanmanchengo/data2/frame*/*.png
do
  fname=${file##*/} 
  fpath=${file%/*} 
  dname=${fpath##*/}
  mv $file ${fpath}/${dname}_${fname}
done

#  echo $file
#  echo $fname
#  echo $fpath
#  echo $dname