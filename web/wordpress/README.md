Overview
------------

Wordpress is an open-source content server to host "web files".  
I can just "install" wordpress in my local computer and then access it from browser.  
Internally it uses php and relies on apache (or other web server..)

Test
--------------

Following http://www.tecmint.com/install-wordpress-on-ubuntu-16-04-with-lamp/ 
to install wordpress..
Or better ref: https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-on-ubuntu-14-04 

mysql> CREATE DATABASE wp_myblog;  
mysql> GRANT ALL PRIVILEGES ON wp_myblog.* TO xma@localhost IDENTIFIED BY "wordpress_pw";  

pw of my test site at localhost "path" : LW@tTmHYv*OmIq@(hQ
username: xma

anyway, at the end, it can be access at http://localhost

to edit the site, i just have to login and do my editting.


Nano wordpress (WP) vs Ruby on Rails (RoR)
----------------------------------------------

One answer: http://stackoverflow.com/questions/13862257/can-wordpress-replace-a-framework-like-django-or-ruby-on-rails

speed, scale and maintainability seems an issue for wordpress.

If you need a car, you can buy some tools and build it (web frameworks like Ruby on Rails),
or you can buy a truck and try to modify it (wordpress).

Wordpress is an application in itself.
Internally it is a blogging platform. every piece of content technically is a post.
