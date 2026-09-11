#!/usr/bin/bash
python warning_popup.py
rm -rf test-report.txt

AZL_VERSION=$(cat azl.version)
CUR_DATE=$(date "+%d.%m.%Y")
CUR_TIME=$(date "+%H:%M:%S")
MACHINE=$(uname -s -r -o)

startTest(){
  echo "== AzuraLang $AZL_VERSION Test Report ==" >> test-report.txt
  echo "reportStartHeader]" >> test-report.txt
  echo "[reportStartTime: $CUR_DATE-$CUR_TIME" >> test-report.txt
  echo "reportOS: $MACHINE." >> test-report.txt
}

testTest1() {
  python3 test1.py
  echo -e "Were all the different labels differently styled?"
  read -r -p "[y/n]>" aa
  case $aa in
    [yY])
    echo ""
    ;;
    [nN])
    pass
    ;;
  esac
}

python printart.py
startTest
echo -e "This is the AzuraLang test script. \nThis script will run all test*.py scripts and try to test all the components."
echo -e "After every single test you'll be asked questions and you need to answer them."
echo -e "After everything, a new file will appear in your working directrory called \"test-report.txt\"."
echo -e "You're help is important to us. If you want to help us,\n make an issue at https://github.com/AzuraCorp/issues with this file attached to. "
read -r -p "Do you want to continue? (y/n)" a
case $a in
  [yY])
  testTest1
  ;;
  [nN])
  exit 0
  ;;
esac
