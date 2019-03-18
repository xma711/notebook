Css
----------------------

Html file (without javascript) is a dull file. 
All the headers, paragraphs, lists, tables will look quite ugly in the browser.

To make them look better, css can be used.

To change the looking of element(s), simply use the tag name from the html file, and use {} to add something inside.  
E.g. an html file has <p> .. </p> stuff, 
the css file can set looking to all the stuff in this tag by:  
p {  
  settings...  
}  
this is called "id selector".

Another way is class selector.  
E.g. the html file has <p class="classname">whatever whatever.</p>.  
The css file can access any elements with such a class by:  
.classname {  
  settings...  
}  

to group a few different tags and apply the same setting to them, simply:  
tag1, tag2, tag3 {  
  settings...   
}  
