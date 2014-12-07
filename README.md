Github Notifier Indicator
================
Simple notifier for Github.

Dependencies
---------
* AppIndicator3
* Gtk

Use
---------
* Choose **settings** on the right
![](http://i60.tinypic.com/ip1278.png)

* Choose Applications on the left, then **Generate new token** in the **Personal access tokens**
![](http://i58.tinypic.com/rcv9cw.png)

* Select a name for your token, and the **notifications** access is enough
![](http://i60.tinypic.com/19sbab.png)

* Click **Generate token**, remember your token, it's only show for once. Then save it to **token** file
![](http://i60.tinypic.com/xfz3oo.png)

**Note:**Don't leave blank spaces ahead of line in **token** file.

If the token is wrong, the number of notifications always shows 2. You can check whether the token is right by open this link in browser:

`https://api.github.com/notifications?access_token=YOURTOKEN`
