Difference between xml and html
-------------------------------

Xml and html were designed with different goals:  
	- xml was designed to carry data - with focus on what data is  
	- html was designed to display data - with focus on how data looks  
	- xml tags are not predefined like html tags are

reference: http://www.w3schools.com/xml/xml_whatis.asp

in many html applications, xml is used to store or transport data,
while html is used to format and display the same data.


Xml example
--------------------
```
<note>
  <date>2015-09-01</date>
  <hour>08:30</hour>
  <to>Tove</to>
  <from>Jani</from>
  <body>Don't forget me this weekend!</body>
</note>
```

some advantages
------------------
Xml stores data in plain text format.
This provides a software and hardware-independent way of storing, transporting and sharing data.

With xml, data can be available to all kinds of "reading machines" like people, computers, news feeds, etc.

Xml separates data from presentation.  
Xml does not carry info about how to be displayed.


Xml tree structure
-------------------------------

<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>


xml vs json
-----------------------

Reference: http://stackoverflow.com/questions/4862310/json-and-xml-comparison

json pros:  
	- simple syntax, which results in less markup overheads compared to xml.  
	- easy to use with javascript as the markup has the same basic data types as javascript.  
	- json schema for description and datatype and structure validation.
Json cons:  
	- simple syntax, only a handful of different data types are supported

xml pros:  
	- generalized markup; possible to create dialects for any kind of purposes  
	- xml schema for datatype, structure validation. makes it possible to create new datatypes.  
	- xpath/xquery for extracting information  
	- built in support for namespaces  
xml cons:  
	- relatively wordy compared to json

"If you are mostly going to use JavaScript then you should go with JSON."


Other notes
----------------------

In python, the library dicttoxml can be used to convert dictionary to xml.  
Check: https://pypi.python.org/pypi/dicttoxml
