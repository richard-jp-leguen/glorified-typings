Putting it Together 2: A Three Column Page
==========================================

We’re going to again make a page with a calendar in it, but it will not have two fixed-width columns; instead it will have three columns, one of which will have a flexible width. (which is a little more challenging)

I again assume that you will be able to remember the basic structure of an HTML document from [this tutorial](tut-01.intro-to-html.md) and as such will dive right into the body of the HTML document.

Step 1: A Basic Page Header
---------------------------

Just follow Step 1 as you saw it in [this](tut-05.a-web-page.md) tutorial.

Step 2: The Main Body
---------------------

This time, our web page is going to have a flexible width so that if the browser window is wider or thinner, the page’s width will adjust.

Nonetheless, we’re again going to add another `<div>` element, after the `PageHeader`, with an  `id` attribute value of `PageMain`. We don’t want to give this `<div>` a ‘width’ CSS property, but we will give it a `min-width` of `600px`, and we will again center it in the page.

#### CSS

    body {
    	/* all the other CSS from before… */
    	text-align:center; /* for Microsoft… */
    }
    #PageMain {
    	margin:auto; /* standardized way to center a block level element */
    	min-width:600px;
    	text-align:left; /*
    				otherwise the center-
    				alignment is inherited 
    			*/
    }

Step 3: Add the Left Side Bar to the Main Body
----------------------------------------------

This page will have three columns: since this is a calendar, the leftmost column will be a list of links to months.

Inside the `PageMain` division, add another division (`<div>`) element, and give its  `id` attribute a value of `MonthsNavBar`. We will give it a fixed width of `195px`, and tell it to _float_ to the left. This means that the content which comes after it will wrap around it _to the right_.

Give all the hyperlinks in the leftmost nav bar hrefs of `#` appended to the month name:

#### HTML

    <ul>
     <li><a href="#January">January</a></li>
     <!-- more… -->
    </ul>

#### CSS

    #PageMain #MonthsNavBar {
    	width:195px;
    	float:left;
    }

With the side bar floating to the left, some browsers will collapse the height of the `PageMain` division. To solve this, assign `PageMain` an `overflow-y` of `hidden` (more on `overflow` some other time…)

#### CSS

    #PageMain {
    	/* the CSS from before */
    	overflow-y:hidden;
    }

Step 4: Add the Right Side Bar to the Main Body
-----------------------------------------------

Next we add a `<div>` after the `MonthsNavBar` division, and give it an `id` of `CoursesNavBar`; the right side bar will be a list of courses. Like, with the side bar of months, amek all the hyperlinks link to `#` appended to the course name:

#### HTML

    <ul>
     <li><a href="#SOEN287">SOEN287</a></li>
     <!-- more… -->
    </ul>

We will also give this side bar a fixed width of `195px`, and tell it to _float_ to the right, so that the content which comes after it will wrap aroud it _to the left_.

#### CSS

    #PageMain #CoursesNavBar {
    	width:195px;
    	float:right;
    }

Step 4: The Main Center Column
------------------------------

Now we are ready to create our center column. Create another `<div>` element after the `CoursesNavBar` div; give it an `id` of `MainContent`.

We don’t want the Main column to wrap around the other columns, and we also want a line between it and the side columns and for it to have a different background color. To achieve all this, assign the left and right margins a value of `200px` (a little more than the width of the left and right columns):

    #MainContent{
    	border:5px solid black;
    	background:yellow;
    	margin-left:200px;
    	margin-right:200px;
    }

When you open the page in a browser the You should now be able to widen the window and see that the center column will widen and shrink, to a minimum width of `600px`.
