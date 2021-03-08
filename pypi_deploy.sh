# NOTE: Make sure to update version number
# pip install twine wheel
echo "We remove unecessary files/folders"
echo "----------------------------------"
rm -rf build/*
rm -rf dist/*
rm -rf *-info
echo "----------------------------------"

echo "python3 setup.py sdist bdist_wheel"
python3 setup.py sdist bdist_wheel
echo "python3 -m twine upload dist/*"
python3 -m twine upload dist/*
echo "----------------------------------"

echo "We remove unecessary files/folders"
rm -rf build/*
rm -rf dist/*
rm -rf *-info
echo "----------------------------------"

