What are HTML, CSS, JavaScript, PHP and Perl?
----------------------------

reference: http://www.thesitewizard.com/html-tutorial/what-is-html.shtml

the order of study web techniques: https://www.zhihu.com/question/22646257 (in zhihu)
which recommends w3school.


Overview
----------------------------
A good overview can be found here: https://www.zhihu.com/question/22689579

html is the format of a document which allows a browser to display the content in certain ways.  
an analogy is that word document has both content and formatting info.
html is the same. it stores both content and format info.

html can also have extra format info like background colour, font, size of text, which are considered as "appearance" of the page.  
or better, these info can be stored in an external file and can be reused; 
also the same html can points to different appearance file for different appearances.  
this special file is called css (cascading style sheets).

html and css are somewhat dumb files. 
they are only good for displaying information.  
if you want html web pages to have some special effects, we need javascript, which can be used inside the html document.
programs written in js run in the web browser itself.

however, even with html, css, js, the webpages cannot go very far.

to make the website truely dynamic, which can respond to users' requests, we need database and 
other programming languages that dynamically generate html pages at the server.
the popular programming languages are php, perl and nowadays even python.

at this stage, we need something that can bridge the user-server interactions (http server) and 
the framework that parses each request and generates html pages as a response.  
this something is the http server, such as apache, nginx, etc. 


how to create a website
-----------------------------
ref: http://www.thesitewizard.com/gettingstarted/startwebsite.shtml


What is the difference between an Apache/nginx server and Node.js one
-------------------------------

reference: https://www.quora.com/What-is-the-difference-between-an-Apache-nginx-server-and-Node-js-one

excerpts:

"Apache and Nginx are both HTTP servers. 
They can serve static files like (.jpg and .html files) 
or dynamic pages (like a Wordpress blog or forum written in a language like PHP or Python). 
Apache/nginx need to be configured to recognize the URLs that users will be requesting and route them to the right place.

So, for example, with a typical PHP site (like a Wordpress blog) 
you tell Apache that any file that ends with .php should be interpreted as PHP code, 
so when the user visits "http://myblog.com/tag.php?q=mytag", 
for example, Apache will launch the PHP interpreter to read the file and process it into an HTML page. 
As part of this process, PHP may talk to a MySQL database and use that to generate the page. 
Lastly, PHP gives the final HTML code to Apache to send to the user's browser.

So, far so good?

Now, Node is a bit different. 
It's a programming environment like PHP that lets you talk to database, make dynamic pages, etc. 
However, it differs in that it includes an HTTP server. 
That means that it can actually act completely on its own without nginx or Apache. 
You can just run Node and it will be the HTTP server 
and also the "app server" (which actually creates your dynamic pages and talks to the DB).

It's a two for one deal.

Last thing to know is that when people actually deploy Node on the internet, 
they sometimes put another HTTP server like nginx in front of Node. 
That means that when a user loads a page, it first hits Nginx which can make a decision about where to route the request. 
This is handy if you have a big site and need to run many Node instances to handle all your traffic. 
This way, the single nginx server can split the work to be done among many Node.js "app servers". "


website vs web appliction
---------------------------

reference: http://stackoverflow.com/questions/8694922/whats-the-difference-between-a-web-site-and-a-web-application

websites are primarily informatinal such as cnn and bbc,
while web apps primarily allow the user to perform actions, such as gmail.

howevery, ususally this is totally personal and subjective..
