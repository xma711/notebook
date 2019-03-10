overall feeling
-------------------------

reference: book "Sams teach yourself Android Application development in 24 hours, 4th edition".

write layout files in xml for each activity (just like html files..);  
then in java codes we make them dynamic and add underlying logics (like javascript to html).

it is always from one activity to another, via the 'Intent'.

each activity has to be registered in the manifest file, which tells the android OS what the app does.


app/manifests/AndroidManifest.xml
--------------------------------------

all activities have to be added here.

e.g. <activity android:name=".MainActivity"> ... </activity>


Activity
----------------------

an activity is like a standone program.  
it has a screen representation (coded by the layout file) and its own logic and own life cycle.

when we enter an app, one screen we see is one activity.
when we click a button and a new screen appears, usually it is a new activity.

in the same app, there are some ways to keep some global shared data. (SharedPreferences or sth..)
 
when one activity activates another activity (one screen to another screen), it needs to use Intent!

intent is like a request of an activity (or service, or an activity from another app..).

an app can be viewed as a collection of activities (and background activities like Service, or sub-activities like Fragments).

each activity has to be registered inside the main manifest.xml file.  
each activity has its properties, like whether it will accept certain intents from other apps.  
each also has its own layout file in /res to represent the view on the screen.

an background activity is called a service.  
the most common type of service is IntentService.  
we also need to register the intentService in the manifest file.  
the communication between the activity and the background interntservice is a publish-subscribe model.  
the intentservice publish an intent when it is done, and whichever activity that subcribes to the topic will get the intent and thus the data with it.

each activity has its life cyble.
the most important ones are onCreate(), onResume(), onPause() etc.  
we should provide details procedures for these functions.


Intent
-------------------------

Intent is a request to start an activity.  
this can be done within an app, or from an app's activity to another app's activity.

e.g. when i start a game, the default activity wil be activated (usually the "welcome" page).  
then when i click something on the menu, it will jump to another view on the screen; 
this is done by the default activity creating an intent to start the corresponding activity based on my input.

in fact, this is called explicit intent, in which an activity specifies precisely which activity to start in the intent.  
another type of intent is the implicit intent, in which an activity only has to specify the general action and let the android os to list out the possible apps that can handle that intent.  
one example is to open a url.  
the activity can create an intent to open a url (sth like Intent i = new Intent(Intent.ACTION_VIEW, url));  
and then start the activity : startActivity(i).

if the activity want to start another activity and gets returning results, then use startActivityForResult()..

To create a background intentService, similar method is used.

Intent can be used to pass data around.  
e.g. when background intentservice is done, it publishes an intent..


res/ folder
----------------------------------

all the resources should be placed in the res/ folder.  
e.g. string.xml, layout files, color file, dimension files, images files, video files, language specific files ...  

as long as we throw things there, they can be accessed by name in both manifest file and java codes.

for different layouts (portrait, landscape), we pick one (portrait) as the default, 
and add another one for landscape, then the app magically is able to switch to landscape layout when needed. 
(the reality is slightly more complicated than that, because we don't want the activity to restart)


app/java/com.example.xma.myfirstapplication/
----------------------------------------

this folder stores all the java files i think.  
the main one is MainActivity.java.

in the class MainActivity (extends AppCompatActivity), 
we just need to override some existing methods, such as onCreate() ...

in fact, just imagine onCreate() is the main function for now, although it is not true.

in all these java files, we can create local variables, just like any java programs.  
but we can also access the more complicated objects, like EditText, Button, TextView objects
that are specially designed for Android.

these more complicated objects will need to be initialized as pointers to the objects declared in
app/res/layout/activity_main.xml thru this "findView" method, which defines the layout of the activity (page).  
the objects are in activity_main.xml are declared using xml.

then, from the java file, as we have all the objects declared in activity_main.xml,
we can control any objects, such as detect button being clicked, retrieve texts from EditText object,
display texts in TextView object...

in short, these java files are the intelligence; 
while the xml files in app/res/layout/ are the views of the app!


app/res/activity_main.xml
---------------------------------

i guess for every activity there must be a corresponding xml file to state the layout.

anyway, for the MainActivity, the layout file is app/res/activity_main.xml.

question: how does MainActivity knows which is its layout file?  
answer: in the java codes, we have to explicitly add a line of code to use this layout file..

in the layout xml file, we can declare the complicated objects, such as
TextView, EditText, Button, and their properties, such as location on the page ...

these objects will be accessible from the java files in app/java/..../*.java 

