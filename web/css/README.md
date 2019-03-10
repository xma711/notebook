css
----------------------

html file (without javascript) is a dull file. 
all the headers, paragraphs, lists, tables will look quite ugly in the browser.

to make them look better, css can be used.

to change the looking of element(s), simply use the tag name from the html file, and use {} to add something inside.  
e.g. an html file has <p> .. </p> stuff, 
the css file can set looking to all the stuff in this tag by:  
p {  
  settings...  
}  
this is called "id selector".

another way is class selector.  
e.g. the html file has <p class="classname">whatever whatever.</p>.  
the css file can access any elements with such a class by:  
.classname {  
  settings...  
}  

to group a few different tags and apply the same setting to them, simply:  
tag1, tag2, tag3 {  
  settings...   
}  
