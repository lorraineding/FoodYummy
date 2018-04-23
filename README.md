## Project: FoodYummy
A website for you to explore world wide recipes and dishes.
## Group Members
Duoduo (Ivy) Liu, Lu Ya Ding, Zhesheng (Helen) Gu
## Technology
| Front-end  |  Back-end |
| ------------ | -----------|
|+ HTML | + Apache	|
|+ CSS | + Flask |
|+ Javascript/DOM | + Python |
|+ JSON | + Mongodb |
|+ Ajax | + Mongoengine |
|+ JQuery | + Security |
|+ Bootstrap  |  	|
|+ 	React	| |
|+ Babel | |

## Deploy FoodYummy on Your Computer

1. Requirement
Make sure you have following:
 	MAC OSX 10.7+, Python2.7+, MongoDB 3.4, Apache 2.4
folder structure
```	
    +\FoodYummy
		-all backend1.zip files
		-\app
				-all backend2.zip files
				-all frontend.zip files
```
2. Install Dependencies
a) mod_wsgi
	Follow this: https://modwsgi.readthedocs.io/en/develop/user-guides/installation-on-macosx.html
	Then in httpd.config 
	
		DocumentRoot “PATH/TO/YOUR/FOODYUMMY”
		WSGIScriptAlias / “PATH/TO/YOUR/FOODYUMMY/FoodYummy.wsgi"
	<Directory “PATH/TO/YOUR/FOODYUMMY”>
  		  Require all granted
  		  Allow from all
		</Directory>

b) from command line, enter:
	`$ cd FoodYummy`
	`$ source setup.sh`
	`$ pip install -r requirements.txt`
c) in FoodYummy.wsgi
	replace sys.path.append() to sys.path.append(“PATH/TO/YOUR/FOODYUMMY”)

3. Run server 
	` # first run mongodb with - - dbpath PATH/TO/FOODYUMMY/database`
	`$ httpd.exe -k start`
	`$ cd FoodYummy`
	`$ python manage.py runserver`

4. To use unit test, type
	`$ python manage.py test`
## How to Use Our Website
1. from browser, type:
	localhost/
2. You can search our recipe using filter
3. You can view our recipe by clicking on the pictures
4. You can send us email by filling a contact form
5. If you want to explore more features, you can log in/register
6. You need to confirm the email address to register
7. After log in, you can view your dashboard
8. You can also upload your own recipe and dish
9. Enjoy! If any questions during installation, please contact us at **foodyummy307@gmail.com**



	

	

	
