## eCSV
### Introduction
This module presents an easy way to create HTML forms from CSV files. You only need to worry about one function, which is outlined in the documentation section.
### Installation
#### Method 1
1. Navigate to dist folder and download the .whl file. Move the file into your project folder
2. Open up the terminal from your project folder (meaning you should see something like)
```
yourproject% 
```
3. Run this command
```
pip install <nameofthe.whl file>
```
4. You can delete the .whl file if you want
#### Method 2
Another way is to just download it from PyPI but in that case you need to also install pandas (v2.1.1) or higher
### Documentation
To convert your CSV file into an HTML form, here is what you do: 
1. Import the module
```
from ecsv.Converter import Converter
```
1. Create an instance of a Converter
```
myfile = Converter("path/to/your/csv/file")
```
1. Call the "into_HTML_form()" method
```
myfile.into_HTML_Form()
```
This returns the HTML form as a string
### Things you should know before converting
While it can convert any non-empty CSV file into an HTML form. There are some rules on how to structure your CSV file before converting it. Here they are:
1. No empty CSVs!
2. Form title always goes in the first row
3. In an HTML form, inputs are always associated with a label. By default, the converter tries to associate the input with the label on it's left. If that isn't successful, it will try and associate the input with the label on the top. 
4. Don't merge cells, it complicates things.