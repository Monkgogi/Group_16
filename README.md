# COMP0034 Skeleton Flask and Dash app for the coursework

## Code structure
- `data` save your data files or database to this directory
- `static/charts` save your generated charts (e.g. .png, .jpg, .html (for express charts)) to this directory
- `templates` pages that your web app displays, e.g. those that are accessed via the navigation bar. Includes pages for home (index), matplotlib charts, plotly express charts, and textual discussion of the Dash charts.
- `flask_app.py` configures and creates the Flask app and provides the routes
- `dash_app.py` configures and creates the Dash app, you will need to edit this with your own Dash code
- `requirements.txt` contains the libraries you will need to install for the app to run. You can use `pip install -r requirements.txt`.

## Using and modifying this Flask and Dash app code
You can use this Flask app template to present your chart portfolio for coursework 1.

You may edit the app in any way you wish (e.g. change the stylesheet, change page names, add or remove pages).

You may also delete this template and create your own Flask app from scratch. 

Please remember that you are not being asessed on your Flask skills in this coursework so any sophistication in the use of Flask will not be considered when marking the coursework. 
However, any experience in using Flask in coursework 1 will likely benefit you in coursework 2.

## Editing the `templates` html files
Use the .html files in the `templates` folder to add your chart image files and textual explanations.

Note that if you change a filename please use a refactoring method in the IDE e.g. in PyCharm use Refactor | Rename. If you do not do this and you change the name of the html file manually then you will also need to make a corresponding change to the navigation bar in `layout.html` and also to the route definitions in `flask_app.py`.

`layout.html` is the base template used by the other pages. You would only need to edit this if you wish to change the CSS style sheet that is used or if you want to edit the navigation bar (e.g. to rename or to add/remove links).

