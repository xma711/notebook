General
---------------

Reference: https://developer.chrome.com/multidevice/webview/overview

since android 4.4, the webview component is based on the chromium open source project.

In android 5.0, the webview has moved to an APK so it can be updated separately.

Some explanation: http://mogoweb.github.io/blog/2014/01/16/analysis-of-android-4-4-webview-implementation/

what are the relations among webview, chromium, v8 js engine, browser, html5 apps?


Most likely, some codes of the webkit exists in the AOSP to provide the interfaces for apps.
Then in AOSP there is bridge taking care of the interactions between webkit in AOSP and webview in an app (AwContents).  
Inside the webview, the core is chromimum;
to be used in android, there is a layer called AwContents.java meaning "android webview"-contents.


How to use webview
------------------------

One example: https://docs.google.com/presentation/d/1SDUIMYhOU79pVYrSgd0dXZ0pkqZjyhBXe7jeFmyuk80/edit#slide=id.g97a4117c_00


