#!/usr/bin/bash
python ./tests/printart.py
echo -e "This is the AzuraLang test script. \nThis script will run all test*.py scripts and try to test all the components."
echo -e "After every single test you'll be asked questions and you need to answer them."
echo -e "After everything, a new file will appear in your working directrory called \"test-report.txt\"."
echo -e "You need to make an issue at https://github.com/AzuraCorp/issues with this file attached to. "
echo -e "(OPTIONAL, BUT RECOMMENDED) Add a fastfetch/neofetch output for better issue fixing."
read -r -p "Do you want to continue? (y/n)" a
case $a in
  [yY])
  echo
  ;;
  [nN])
  exit 0
  ;;
esac