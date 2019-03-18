Basics
------------

Reference: http://tutorial.djangogirls.org/en/html/README.html

a template is a file that we can re-use to present different information in a consistent format.  

A django template's format is described in a language called HTML. 

Html is a code that is interpreted by a web browser to display a webpage for the user.

Html stands for HyperText Markup Language.  
HyperText means it is a type of text that supports hyperlinks between pages.  
Markup means we have taken a document and marked it up with code to tell a browser how to interpret the page.  

Html code is built with tags, each one starting with \< and ending with \>. these tags represent markup elements.


All HTML documents must start with a type declaration: <!DOCTYPE html>.

The HTML document itself begins with <html> and ends with </html>.

The visible part of the HTML document is between <body> and </body>.

Usually, one thing in html starts with <tagname> and ends with </tagname>.  
The first <tagname> can have some extra attributes, e.g. <a href="google.com">this is a link to google</a>.

There seems to some exceptions though, like image:  
<img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">  
, which has only <img attributes> and no </img>

<br> the line break is another example. however, it seems that adding a </br> is no problem too.

Example 1
--------------
Reference: http://tutorial.djangogirls.org/en/html/README.html

```
<html>
    <p>Hi there!</p>
    <p>It works!</p>
</html>
```

The most basic tag, <html>, is always the beginning of any webpage and </html> is always the end. 

As you can see, the whole content of the website goes between the beginning tag <html> and closing tag </html>
    
<p> is a tag for paragraph elements; </p> closes each paragraph


```
<html>
    <head>
        <title>Ola's blog</title>
    </head>
    <body>
        <p>Hi there!</p>
        <p>It works!</p>
    </body>
</html>
```
head is an element that contains information about the document that is not displayed on the screen.

Body is an element that contains everything else that is displayed as part of the web page.

Notice how the browser has understood that "Ola's blog" is the title of your page? It has interpreted <title>Ola's blog</title> and placed the text in the title bar of your browser (it will also be used for bookmarks and so on).

Each opening tag is matched by a closing tag, with a /,   
and that elements are nested (i.e. you can't close a particular tag until all the ones that were inside it have been closed too).

It's like putting things into boxes.   
You have one big box, <html></html>;   
inside it there is <body></body>, and that contains still smaller boxes: <p></p>.

You need to follow these rules of closing tags, and of nesting elements - if you don't, the browser may not be able to interpret them properly and your page will display incorrectly.


More tags
-------------------------


    <h1>A heading</h1> - for your most important heading

    <h2>A sub-heading</h2> for a heading at the next level

    <h3>A sub-sub-heading</h3> ... and so on, up to <h6>

    <em>text</em> emphasizes your text

    <strong>text</strong> strongly emphasizes your text

    <br /> goes to another line (you can't put anything inside br)

    <a href="http://djangogirls.org">link</a> creates a link

    <ul><li>first item</li><li>second item</li></ul> makes a list, just like this one!

    <div></div> defines a section of the page


example 2
-----------------------
```
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
        <div>
            <h1><a href="">Django Girls Blog</a></h1>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My first post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My second post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut f.</p>
        </div>
    </body>
</html>
```
