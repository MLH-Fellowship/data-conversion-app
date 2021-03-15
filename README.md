# Hermes

## Getting Started

### Install Dependencies

This program is currently compatible with major versions of Python, and is tested for verification on Python 2.6, 2.7, 3.7, and 3.9.

Note: Dependencies are only required for development. To use, no dependencies are required.

```bash
pip install -r requirements.txt
```

### Run in Development

```bash
python app.py
```

### Testing for Development

* Start Python interactive interpreter:

  ```bash
  python
  ```

* Examples:

  * Import Functions:
  
  ```python
  from app.exporter import to_timestamp
  ```

  * Run Function:
  
  ```python
  to_timestamp("2021-01-21T17:26:11")
  ```

* Examples, including data import:

  * Imports:
  
  ```python
  from app.exporter import simple_file_writes, sample_data
  ```

  * Run Function:
  
  ```python
  simple_file_writes(sample_data)
  ```

## About the Project

### The Problem/Project

Essentially, we need to convert CEESIM files to A2PATS files. These files are used in army flight simulators. I believe we need to convert these so that the same patterns can be used on different simulation systems to prevent redundancy of work. This will either be a desktop app but more likely a script that runs a file and creates its converted variant. This project is highly technical in nature and will require much guidance from the USAF.

* Project Support: **NA**
* Project Constraints: **NA**
* Project Skills Needed: **Python**

### Project Sponsor Info

Point of Contact: **Dion Carrieri**

### About USAF

We are working with a very technically advanced US Air Force division that deals with new technology the USAF works on such as the F-35 program.

## Resources

### Email from Dion

CEESIM files are different. I will send them to you in an XML format, and ASCII format and the CEESIM format.

You will not be able to read the CEESIM format as you do not have a CEESIM system. __*(I did not include these in the data dump - there are no CEESIM format files, these are the sc1-3 files we talked about...)*__

I think you will want to work with the XML format as you should be able to tell more from that and the XML format can be directly uploaded to CEESIM so that will probably be the one to go with.

You can open the ASCII as well but not sure if you will use that.

### Links

* [CESSIM to A2PATS Lookup Table](https://docs.google.com/spreadsheets/d/1ENsy1Ia1xtXSf6RaxW97A5YNb0TnNML9w7mTQQ_rxl8/edit#gid=0)
* [XML to Data Structure Python Packaging](http://pyxb.sourceforge.net/)
* [Glossary of Terms Used In Aviation as it relates to Electrical Engineering](https://www.radartutorial.eu/index.en.html)
* [Tool for Visualizing XSD Files](http://visualxsd.com/)
* [3D Airplane Antenna Visualizer](https://www.youtube.com/watch?v=jtxXOfzPdK4&ab_channel=TheVindicators)
* [A2PATS Family Promotional Video](https://www.youtube.com/watch?v=xBHQJwdqe58&ab_channel=textronsystems)
* **Building and testing Python**: [Testing your code](https://docs.github.com/en/actions/guides/building-and-testing-python#testing-your-code)
