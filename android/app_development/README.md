Overall feeling
-------------------------

Reference: book "Sams teach yourself Android Application development in 24 hours, 4th edition".

Write layout files in xml for each activity (just like html files..);  
then in java codes we make them dynamic and add underlying logics (like javascript to html).

It is always from one activity to another, via the 'Intent'.

Each activity has to be registered in the manifest file, which tells the android OS what the app does.


App/manifests/AndroidManifest.xml
--------------------------------------

All activities have to be added here.

E.g. <activity android:name=".MainActivity"> ... </activity>


Activity
----------------------

An activity is like a standalone program.  
It has a screen representation (coded by the layout file) and its own logic and own life cycle.

When we enter an app, one screen we see is one activity.
When we click a button and a new screen appears, usually it is a new activity.

In the same app, there are some ways to keep some global shared data. (SharedPreferences or something..)
 
When one activity activates another activity (one screen to another screen), it needs to use Intent!

Intent is like a request of an activity (or service, or an activity from another app..).

An app can be viewed as a collection of activities (and background activities like Service, or sub-activities like Fragments).

Each activity has to be registered inside the main manifest.xml file.  
Each activity has its properties, like whether it will accept certain intents from other apps.  
Each also has its own layout file in /res to represent the view on the screen.

An background activity is called a service.  
The most common type of service is IntentService.  
We also need to register the intentService in the manifest file.  
The communication between the activity and the background interntservice is a publish-subscribe model.  
The intentservice publish an intent when it is done, and whichever activity that subscribes to the topic will get the intent and thus the data with it.

Each activity has its life cycle.
The most important ones are onCreate(), onResume(), onPause() etc.  
We should provide details procedures for these functions.


Intent
-------------------------

Intent is a request to start an activity.  
This can be done within an app, or from an app's activity to another app's activity.

E.g. when i start a game, the default activity will be activated (usually the "welcome" page).  
Then when i click something on the menu, it will jump to another view on the screen; 
this is done by the default activity creating an intent to start the corresponding activity based on my input.

In fact, this is called explicit intent, in which an activity specifies precisely which activity to start in the intent.  
Another type of intent is the implicit intent, in which an activity only has to specify the general action and let the android OS to list out the possible apps that can handle that intent.  
One example is to open a url.  
The activity can create an intent to open a url (something like Intent i = new Intent(Intent.ACTION_VIEW, url));  
and then start the activity : startActivity(i).

If the activity want to start another activity and gets returning results, then use startActivityForResult()..

To create a background intentService, similar method is used.

Intent can be used to pass data around.  
E.g. when background intentservice is done, it publishes an intent..


Res/ folder
----------------------------------

All the resources should be placed in the res/ folder.  
E.g. string.xml, layout files, color file, dimension files, images files, video files, language specific files ...  

As long as we throw things there, they can be accessed by name in both manifest file and java codes.

For different layouts (portrait, landscape), we pick one (portrait) as the default, 
and add another one for landscape, then the app magically is able to switch to landscape layout when needed. 
(the reality is slightly more complicated than that, because we don't want the activity to restart)


app/java/com.example.xma.myfirstapplication/
----------------------------------------

This folder stores all the java files i think.  
The main one is MainActivity.java.

In the class MainActivity (extends AppCompatActivity), 
we just need to override some existing methods, such as onCreate() ...

In fact, just imagine onCreate() is the main function for now, although it is not true.

In all these java files, we can create local variables, just like any java programs.  
But we can also access the more complicated objects, like EditText, Button, TextView objects
that are specially designed for Android.

These more complicated objects will need to be initialized as pointers to the objects declared in
app/res/layout/activity_main.xml thru this "findView" method, which defines the layout of the activity (page).  
The objects are in activity_main.xml are declared using xml.

Then, from the java file, as we have all the objects declared in activity_main.xml,
we can control any objects, such as detect button being clicked, retrieve texts from EditText object,
display texts in TextView object...

In short, these java files are the intelligence; 
while the xml files in app/res/layout/ are the views of the app!


App/res/activity_main.xml
---------------------------------

I guess for every activity there must be a corresponding xml file to state the layout.

Anyway, for the MainActivity, the layout file is app/res/activity_main.xml.

Question: how does MainActivity knows which is its layout file?  
Answer: in the java codes, we have to explicitly add a line of code to use this layout file..

In the layout xml file, we can declare the complicated objects, such as
TextView, EditText, Button, and their properties, such as location on the page ...

These objects will be accessible from the java files in app/java/..../*.java 

