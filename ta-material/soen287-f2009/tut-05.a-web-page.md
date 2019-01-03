Putting it Together: A Web Page
===============================

We’re going to put what we’ve learned about HTMl and CSS together and write up a web page using both, practicing how to control the appearance of a web page **without tables.**

The web page we’re going to write will be a weekly schedule, similar to the schedule you can print from your myConcordia portal. We’re also going to imitate some of the look and feel of the [Concordia ENCS web site](http://encs.concocrdia.ca).

This tutorial will be a little hard to follow, as I’ll be jumping back and forth between HTML and CSS. It will be important to remember that that is the hardest part of the tutorial: to make sure you’re following what’s going on. The technical side – the HTML and CSS – really isn’t that hard.

I assume that you will be able to remember the basic structure of an HTML document from [this tutorial](tut-01.intro-to-html.md) and as such will dive right into the body of the HTML document.

Step 1: A Basic Page Header
---------------------------

### Background Color

We’ll start by using the same background color as the ENCS web page:

#### CSS

    body {
    	background-color:#FFFFCC;
    }

### Page Header

Take note that by the _page header_ I don’t mean the contents of the `<head>` element (which I refer to as the _document header_) but rather to the visual elements which appear at the top of the page. In the case of the ENCS web site, when I say ‘page header’ I in fact refer to the ENCS logo which appears on almost every page)

Create a div for the entire header. Give its  `id` attribute a value "`PageHeader`".

Download [this](assets/ENCS-logo.gif) image, and put it inside the `PageHeader` div in the top-right corner of the page using the following HTML and CSS:

#### HTML

    <img src='ENCS-logo.gif' id='EncsLogo' alt='Concordia ENCS Logo' />

#### CSS

    #PageHeader {
    	position:relative;
    	top:0px;
    	left:0px;
    	background-color:#eee9b1;
    }
    #PageHeader img#EncsLogo {
    	position:absolute;
    	top:0px;
    	right:0px;
    }

#### Explanation

The `position` CSS property allows you to control the position of an element in your rendered web page.

The default value for `position` is `static`.

When you set it to `relative`, you tell the browser to move the element relative to where it would render by default. So in the CSS shown, we’re moving the `<div>` with `id="PageHeader"` `0px` down (away from `top`) and `0px` to the right (away from `left`), meaning it renders in the same place!

We need to do this, however, so we can then position the `<img>` with `id="EncsLogo"` – its child – absolutely. An element with `position:absolute;` is positioned with respect to the position of its parent, but only if its parent is not positioned statically.

So in saying that the `<img>` with `id="EncsLogo"` is positioned absolutely, we can now say that its top should be `0px` away from the top of the element with `id="PageHeader"`, and its right edge is `0px` from the right side of the element with `id="PageHeader"`. The problem with absolute positioning is that it might cause the `PageHeader` element to collapse and be smaller than our image, we we’ll use a CSS `height` property to fix that:

#### CSS

    #PageHeader {
    	/* ... the CSS from before */
    	height:120px;
    }

In order to distinguish between the page header and the rest of the content, we should have some sort fo divider. To do this, let’s add a thick stripe under the `PageHeader` element:

#### CSS

    #PageHeader {
    	/* ... the CSS from before */
    	border-bottom:10px solid #922338;
    }

If you open your HTML file in a web browser, you should now see a beigish page, with a darker beige header area, and the ENCS logo on the right side. Depending on the browser you’re using, the darker area might not touch the edges of the page, but we want the header to stretch all the way across the page; to fix this, you need to specify that your `<body>` doesn’t have any padding or margin:

#### CSS

    body {
    	background-color:#FFFFCC;
    	margin:0px;
    	padding:0px;
    }

#### Explanation

Padding is the space between the edge of an element and the content inside of it. Margin is the space between an element and any elements around it. Browsers assume that a `<body>` element will have some padding or margin so you need to explicitly set the padding and margin of the `<body>` element in your CSS.

Step 2: The Main Body
---------------------

Our web page is going to have a fixed width (like mine; notice that even as the browser gets bigger and smaller the page remains the same width) so we’re now going to add another `<div>` element, after the `PageHeader`, with an  `id` attribute value of `PageMain`. We want this `<div>` to be `900px` wide, and centered in the page, so we will need some CSS for this. According to the standards, this is how you center a block level element:

#### CSS

    #PageMain {
    	margin:auto;
    	width:900px;
    }

… but Microsoft disagrees. In order to center a block level element in IE, you need to set the `text-align` property of the parent element to `center`. In this case, the parent element is the `<body>`:

#### CSS

    body {
    	/* all the other CSS from before… */
    	text-align:center;
    }
    	
    #PageMain {
    	/* the CSS from before */
    	text-align:left; /*
    				otherwise the center-
    				alignment is inherited 
    			*/
    }

Step 3: Add a Side Bar to the Main Body
---------------------------------------

We’re going to add a side bar to the left side of our web page. It will contain some generic information we’ll steal from the ENCS web page (such as ‘mailing address’ and ‘contact us’) as well as a navigation menu of links.

Inside the `PageMain` division, add another division (`<div>`) element, and give its  `id` attribute a value of `SideBar`. We will give it a fixed width of 250px, and tell it to _float_ to the left. This means that the content which comes after it will wrap aroud it _to the right_.

We’ll also put another thick stripe on the right side of the side bar, and give it a background, like on the ENCS web site. Download [this](assets/sidebarbg.gif) image to use as a background image.

#### CSS

    #PageMain #SideBar {
    	width:250px;
    	float:left;
    	background:url(sidebarbg.gif) bottom center no-repeat;
    	padding-bottom:407px; /* so there is nothing over the image */
    	border-right:10px solid #922338;
    }

With the side bar floating to the left, some browsers will collapse the height of the `PageMain` division. To solve this, assign `PageMain` an `overflow-y` of `hidden` (more on `overflow` some other time…)

#### CSS

    #PageMain {
    	/* the CSS from before */
    	overflow-y:hidden;
    }

### Adding the Mailing Address to the Side Bar

Inside that division, put another division `<div>`. Give its  `id` attribute a value of `MailingAddress` and put the following HTML inside it:

#### CSS

    <label>Mailing Address</label>
    <p>
     1455 de Maisonneuve Blvd. W<br />
     Montreal, Quebec<br />
     H3G 1M8 Canada
    </p>

We want this division to look just like the `Mailing Address` part of the real ENCS web site, so the label has to be on its own line, with a different background, and the text in the paragraph should be centered. To achieve this, use the following CSS:

#### CSS

    #MailingAddress label {
    	display:block;
    	font-weight:bolder;
    	background-color:#bdb76b;
    	border:#999 1px solid;
    }
    #MailingAddress p {
    	text-align:center;
    }

Looking at it in the browser, overall, our fonts are a little big, so we’re going to target some CSS rules to control the font of the document’s body.

#### CSS

    body {
    	/* the CSS from before */
    	font-family: Verdana, Arial, Helvetica, sans-serif;
    	font-size: 10px;
    }

Step 4: Add a Navigation menu to the Side Bar
---------------------------------------------

Still in the `SideBar` `<div>`, add another div after the mailing address. Give its  `id` attribute a value of `NavigationMenu` and put the following HTML inside it:

#### HTML

    <label>Navigation Menu</label>
    <ul>
     <li>
       <a href='http://users.encs.concordia.ca/~s287_2/'>
        SOEN 287 Course Web Site
       </a>
     </li>
     <li>
       <a href='http://richard.jp.leguen.ca/tutoring/soen287/'>
        SOEN 287 Tutorial Web Site
       </a>
     </li>
     <li>
       <a href='http://google.ca'>
        Google
       </a>
     </li>
    </ul>

First, we want to again format our `<label>` element:

#### CSS

    #NavigationMenu label {
    	/*	there is a better way to do this
    		without repeating the CSS properties,
    		by using the 'class' attribute… */
    	display:block;
    	font-weight:bolder;
    	background-color:#bdb76b;
    	border:#999 1px solid;
    }

Ok, this may not be the best use of a `<label>` element, but I wanted to at least make you aware of its existence.

When we look at this in the browser, however, it still doesn’t look very good. As the navigation menu is an ordered list, we get a bunch of bullet points all over the place. In order to remove them, use the `list-style` CSS property. We’re also going to use some padding (space between the edge of the element and its contents) and margins (space between the edge of the element and the elements around it):

#### CSS

    #SideBar #NavigationMenu ul {
    	list-style:none;
    	padding:0px 3px 0px 3px; /* top; right; bottom; left */
    	margin:2px; /* on all sides */
    	margin-top:10px; /*	move it down a litte…
    				note that the margin-top does
    				not stack or get added to the above margin,
    				the margin on the bottom of the element
    				is 10px.
    			*/
    }

Let’s also put the individual menu items in boxes: (or rather, give them height and borders)

#### CSS

    #SideBar #NavigationMenu ul li {
    	border:1px double #999;
    	height:25px;
    	font-weight:bolder;
    	margin:2px; /* seperate them slightly… */
    }

You might notice that if you click in a menu item, but not on the _text_, the hyperlink doesn’t work. That’s because an anchor `<a>` is an inline element, so it’s only as big as its contents require; the anchors don’t have a width nor a height, only content. Fix this by changing the `display` property of those anchors to `block`, and you can then assign them a height and width:

#### CSS

    #SideBar #NavigationMenu ul li a {
    	display:block;
    	height:25px;
    	width:100%;
    }

If you don’t like the way that the text in your anchors is underlined, you can remove that using the `text-decoration` property:

#### CSS

    #SideBar #NavigationMenu ul li a {
    	/* ... the CSS from before */
    	text-decoration:none;
    }

Equally, if you want the navigation text to be a color other than blue, use the `color` property, which corresponds to the font’s color:

#### CSS

    #SideBar #NavigationMenu ul li a {
    	/* ... the CSS from before */
    	color:#922338;
    }

Step 5: The Page’s Main Content
-------------------------------

After the `<div>` `SideBar`, add another `<div>` and give its `id` attribute a value of `MainContent`. It is inside this division that we will be putting the calendar. For now, temporarily, just put some lorem ipsum text in it.

To control where the main content goes – and prevent it from wrapping around the side bar when the side bar ‘runs out’ – use CSS to make it float to the right, and give it a fixed width:

#### CSS

    #MainContent{
    	width:640px;
    	float:right;
    }

Personally, I don’t like how the thick stripe at the top of the page goes all the way accross the page. We’re going to change the CSS so it only goes accross part of the page, but not the side bar.

Find the CSS rule which targets the `PageHeader` element. Change its `border-bottom` value to the following:

    border-bottom:1px solid #999;

Now add a style rule targeting the `MainContent` division and give it a thick stripe on top:

#### CSS

    #MainContent {
    	/* the CSS from earlier */
    	border-top:10px solid #922338;
    }

Now the content of the left panel is probably a little higher than the main content. To fix this, we’re going to also put a thick stripe on top of the side bar, but it will be the same color as the header’s background color:

#### CSS

    #PageMain #SideBar {
    	/* the CSS from before */
    	border-top:10px #eee9b1 solid;
    }

Now that we have a page layout, we are ready to put a weekly calendar in the main content of the page.

Step 6: The Calendar
--------------------

In the `MainContent` division, put a header `<h1>` like this:

#### HTML

    <h1>Weekly Schedule</h1>

Let’s stylize that header for kicks. In the CSS try the following:

#### CSS

    h1 {
    	font-size:2em;
    	border-bottom:5px double black;
    	width:70%;
    	margin:auto;
    	margin-bottom:10px;
    }

The goal here, again, is for the web page to be a weekly schedule, like you have on your myConcordia portal. It will consist of 7 ordered lists, each representing a day of the week, as well as one more to serve as a kind of ‘index’. In those lists, each list item will represent a 15 minute period of time.

For organization, we’ll want to group all these `<ol>` elements into a division which we’ll give an  `id` attribute of `WeeklySchedule`:

#### HTML

    <div id='WeeklySchedule'>
     <ol id='Monday'><!-- more to come --></ol>
     <ol id='Tuesday'><!-- more to come --></ol>
     <ol id='Wednesday'><!-- more to come --></ol>
    <div>

We want the `WeeklySchedule` division to be centered in the maincontent of the page, and to have a fixed width which means two things:

*   According to standards, the division containing them – WeeklySchedule – should have a `margin:auto` style property
*   … and according to Microsoft, its parent element (MainContent) should have a `text-align:center` property.

Now, in the HTML document, inside the WeeklySchedule division, write out some `<ol>` elements and give their `<li>` children  `id` attributes. Every `<li>` – which represents a 15 minute time slot – should have a unique `id` attribute, for use in later tutorials and assignments.

#### HTML

Please note that there were errors in this HTML snippet, which were corrected on the 20th of September.

    <ol>
     <li id='Time08h00'>8:00</li>
     <li id='Time08h15'>8:15</li>
     <li id='Time08h30'>8:30;</li>
      <!-- more… -->
    </ol>
    <ol id='Monday' class='DayOfWeek'>
     <li id='Monday08h00'>&nbsp;</li>
     <li id='Monday08h15'>&nbsp;</li>
     <li id='Monday08h30'>&nbsp;</li>
      <!-- more… -->
    </ol>

Note that an element’s `id` or `class` attribute can’t start with a number.

We want these unordered lists to have fixed widths, and to be side by side, so we’re going to apply the `float:left;` CSS property to them all, as well as a `width:75px;` CSS property. We don’t need the list items to be numbered either so we’re going to use the `list-style:none;`, `padding:0px;` and `margin:0px;` propertie too.

#### CSS

    #MainContent #WeeklySchedule ol {
    	width:75px;
    	list-style:none;
    	float:left;
    	padding:0px;
    	margin:0px;
    }

As for our list items, they should all have a fixed height, a border, and a white background.

#### CSS

    #MainContent #WeeklySchedule ol li {
    	border:1px solid black;
    	background:white;
    	height:45px;
    }

Once you’ve done that, find the list item which corresponds to the beginning of your tutorial section, and inside put a div element with an `id` attribute of `Soen287Tutorial`:

#### HTML

    <div id='Soen287Tutorial'>
    	SOEN287<br />Tut
    </div>

We want this division to stretch out a few time slots, and we want it to appear over the time slots which it occupies:

#### CSS

    #Soen287Tutorial {
    	position:relative;
    	z-index:2;
    	height:125px;
    	background-color:blue;
    }

Step 7: Profit
--------------

If only.
