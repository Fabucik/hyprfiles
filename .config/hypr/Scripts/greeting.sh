h=`date +%-H`

if [[ $h -lt 12 ]] && [[ $h -gt 5 ]]; then
  echo Good morning, $USER
elif [[ $h -lt 18 ]] && [[ $h -gt 12 ]]; then
  echo Good afternoon, $USER
elif [[ $h -lt 22 ]] && [[ $h -gt 18 ]]; then
  echo Good evening, $USER
else
  echo Good night, $USER
fi
