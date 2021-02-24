# Getting Started:
### Installing packages
```pip3 install -r requirements.txt```

### Running the app
```python3 app.py```

### Testing functions
- start python shell: ```python3```  
- example command: 
```from app.exporter import to_timestamp```
```to_timestamp("2021-01-21T17:26:11")```
- example command importing function & data: 
```from app.exporter import simple_file_writes, sample_data
```simple_file_writes(sample_data)```


# About the Project

The Problem/Project
Essentially, we need to convert CEESIM files to A2PATS files. These files are used in army flight simulators. I believe we need to convert these so that the same patterns can be used on different simulation systems to prevent redundancy of work. This will either be a desktop app but more likely a script that runs a file and creates its converted variant. This project is highly technical in nature and will require much guidance from the USAF.

- Project Support: NA
- Project Constraints: NA
- Project Skills Needed: Python

Project Sponsor Info
Point of Contact: Dion Carrieri

About USAF
We are working with a very technically advanced US Air Force division that deals with new technology the USAF works on such as the F-35 program.

# Email details from Dion outlining project files:

CEESIM files are different. I will send them to you in an XML format, and ASCII format and the CEESIM format.

You will not be able to read the CEESIM format as you do not have a CEESIM system. __*(I did not include these in the data dump - there are no CEESIM format files, these are the sc1-3 files we talked about...)*__

I think you will want to work with the XML format as you should be able to tell more from that and the XML format can be directly uploaded to CEESIM so that will probably be the one to go with.

You can open the ASCII as well but not sure if you will use that.

# Resources:

[XML to Data Structure Python Packaging](http://pyxb.sourceforge.net/)

[Glossary of Terms Used In Aviation as it relates to Electrical Engineering](https://www.radartutorial.eu/index.en.html)

[Tool for Visualizing XSD Files](http://visualxsd.com/)

[3D Airplane Antenna Visualizer](https://www.youtube.com/watch?v=jtxXOfzPdK4&ab_channel=TheVindicators)

[A2PATS Family Promotional Video](https://www.youtube.com/watch?v=xBHQJwdqe58&ab_channel=textronsystems)


# Building and testing Python
[Testing your code](https://docs.github.com/en/actions/guides/building-and-testing-python#testing-your-code)

GitHub provides a Python workflow template that should work for most Python projects. 

You don't have to install anything! 

Prerequisites:
You should be familiar with YAML and the syntax for GitHub Actions. We recommend that you have a basic understanding of Python, PyPy, and pip.

