A Partial HTML Reference
========================

Common HTML Tags
----------------

In this tutorial, I’m going to list some of the more relevant HTML tags you will be using. I have divided them into two categories: block elements, and inline elements.

### Block Elements

Block elements automatically generate a line break at their beginning and their end. Using CSS, you can control a block element’s height and width, specify if the text in a block element is left-aligner/right-aligned/centered, or indent the first line of text in a block element.

#### Headers: `<h1>` `<h2>` `<h3>` `<h4>` `<h5>` `<h6>`

Headers are used to denote important headers in your document; if your document was a book, these would be the names of chapters etc. Extracting the headers from your document should allow someone to create a kind of table of contents.

Headers are block elements, meaning that they are on their own line.

Conventionally, you only want to have one `<h1>` tag in your document. After that, anything goes.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>The Autobiography of Richard Le Guen | leguen.ca</title>
     </head>
     <body>
      <h1>The Autobiography of Richard Le Guen</h1>
       <h2>Introduction</h2>
        <p>Richard Le Guen is a graduate
        of Software Engineering at Concordia University.
        He works as a tutor there.</p>
       <h2>Early Youth</h2>
        <h3>Family</h3>
         <p>Richard Le Guen is the youngest in a family of 6;
         his parents came from the small island of Mauritius to Canada in the 70s.</p>
         <p>They lived in Sudbury, where they had their first son,
         before moving to Montreal, where the rest of the family was born.</p>
        <h3>Friends</h3>
         <p>Richard has no friends.</p>
       <h2>Death</h2>
        <p>
         Richard died in the line of duty, protecting the President from assassination.
        </p>
     </body>
    </html>

#### Divisions `<div>`

A division has no semantic meaning. It is just a block-level division of a document. Other than the fact that – like any other block element – a `<div>` places a line break before and after itself, it is invisible until you specify how it should look using CSS. You’ll usually want to use the "id" and "class" attributes (see below) combined with CSS to distinguish div elements.

A division is used to organize your document, like the following:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Div Examples | leguen.ca</title>
     </head>
     <body>
      <div id='banner'>
       <img src='advertisement.jpg' />
      </div>
      <div id='main'>
       <p>
        Hello World!
       </p>
      </div>
      <div id='footer'>
       <p>
        &#169; Richard Le Guen
       </p>
      </div>
     </body>
    </html>

#### Paragraph `<p>`

You’ve already seen a paragraph tag in action.

#### Lists, `<ol>` and `<ul>`

Lists are block items. They can be either ordered lists `<ol>` or unordered lists `<ul>` and they contain list item elements, `<li>`. You can nest lists inside each other:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>List Examples | leguen.ca</title>
     </head>
     <body>
      <div>
       These are a few of my favorite things:
       <ol>
        <li>
         <ul>
         <li>Raindrops on roses</li>
         <li>whiskers on kittens</li>
         </ul>
        </li>
        <li>
         <ul>
         <li>Bright copper kettles</li>
         <li>warm woolen mittens</li>
         </ul>
        </li>
        <li>
         <ul>
         <li>Brown paper packages tied up with strings</li>
         </ul>
        </li>
       </ul>
      </div>
     </body>
    </html>

#### Preformatted content, `<pre>`

A preformatted element will be render in the web page as plain text, exactly as it appears in the HTML. Most notably, this means white space _is_ relevant in a preformatted element.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Div Examples | leguen.ca</title>
     </head>
     <body>
      <div id='content'>
       It's an X-Wing!
       <pre>
                   __
        .-.__      \ .-.  ___  __|_|  
    '--.-.-(   \/\;;\_\.-._______.-.
        (-)___     \ \ .-\ \;;\(   \       \ \
         Y    '---._\_((Q)) \;;\\ .-\     __(_)
         I           __'-' / .--.((Q))---'    \,
         I     ___.-:    \|  |   \'-'_          \
         A  .-'      \ .-.\   \   \ \ '--.__     '\
         |  |____.----((Q))\   \__|--\_      \     '
            ( )        '-'  \_  :  \-' '--.___\
             Y                \  \  \       \(_)
             I                 \  \  \         \,
             I                  \  \  \          \
             A                   \  \  \          '\
             |              snd   \  \__|           '
                                   \_:.  \
                                     \ \  \
                                      \ \  \
                                       \_\_| 
       </pre>
      </div>
     </body>
    </html>

#### Tables, `<table>`

With the `<table>` element come various other elements as well: `<tbody>`, `<tr>` (table row), `<td>` (table cell) and `<th>` (table header cell) which are to be used in a `<table>` element.

It is important to note that while it is easy to use a table to control the structure of elements in a web site, **this is wrong** and a table should only be used when you have a table of information in your document.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>My First HTML Table | Richard Le Guen</title>
     </head>
     <body>
      <h1>Multiplication Tables</h1>
      <table>
      <tbody>
       <tr>
        <td> &nbsp; </td><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th>
        <th>6</th><th>7</th><th>8</th><th>9</th><th>10</th>
       </tr>
       <tr>
        <th>1</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td>
        <td>6</td><td>7</td><td>8</td><td>9</td><td>10</td>
       </tr>
       <tr>
        <th>2</th><td>2</td><td>4</td><td>6</td><td>8</td><td>10</td>
        <td>12</td><td>14</td><td>16</td><td>18</td><td>20</td>
       </tr>
       <tr>
        <th>3</th><td>3</td><td>6</td><td>9</td><td>12</td><td>15</td>
        <td>18</td><td>21</td><td>24</td><td>27</td><td>30</td>
       </tr>
       <tr>
        <th>4</th><td>4</td><td>8</td><td>12</td><td>16</td><td>20</td>
        <td>24</td><td>28</td><td>32</td><td>36</td><td>40</td>
       </tr>
       <tr>
        <th>5</th><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td>
        <td>30</td><td>35</td><td>40</td><td>45</td><td>50</td>
       </tr>
       <tr>
        <th>6</th><td>6</td><td>12</td><td>18</td><td>24</td><td>30</td>
        <td>36</td><td>42</td><td>48</td><td>54</td><td>60</td>
       </tr>
       <tr>
        <th>7</th><td>7</td><td>14</td><td>21</td><td>28</td><td>35</td>
        <td>42</td><td>49</td><td>56</td><td>63</td><td>70</td>
       </tr>
       <tr>
        <th>8</th><td>8</td><td>16</td><td>24</td><td>32</td><td>40</td>
        <td>48</td><td>56</td><td>64</td><td>72</td><td>80</td>
       </tr>
       <tr>
        <th>9</th><td>9</td><td>18</td><td>27</td><td>36</td><td>45</td>
        <td>54</td><td>63</td><td>72</td><td>81&tt;/td><td>90</td>
       </tr>
       <tr>
        <th>10</th><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td>
        <td>60</td><td>70</td><td>80</td><td>90</td><td>100</td>
       </tr>
      </tbody>
      </table>
     </body>
    </html>

#### Input Forms, `<form>`

Forms are a block-level elements which are used for allowing users to interact with a web site. We will get into them later.

#### Script `<script>`

The `<script>` element contains code to be executed in the browser environment. Typically, the code is written in some form of ECMAscript such as JavaScript, or JScript.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Script | leguen.ca</title>
     </head>
     <body>
      <script type="text/javascript">
       alert("Annoying Popup!");
      </script>
     </body>
    </html>

### Inline Elements

Inline elements can be placed inside a block-level element, and do not begin or end with a line break. It is invalid to put a block-level element nested inside an inline element.

#### Images, `<img />`

Images, like we saw earlier, are elements which are represented using empty (or self-closing) tags. To specify the image file to reference, use the ‘src’ attribute. The ‘src’ attribute can be a relative path, an absolute path, or a full URL.

It is also recommended that you include the ‘alt’ attribute when referencing an image; in the event that the image can’t be included in the rendered document, the text provided by the alt attribute will appear.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Images in HTML | Richard Le Guen</title>
     </head>
     <body>
      <h1>Images</h1>
      <div>
       <h2>An Image With a Url in the src Attribute</h2>
       <img src="http://www.google.ca/logos/logo.gif" alt="Google Logo" />
      </div>
      <div>
       <h2>The 'alt' Attribute</h2>
       <img src="#" alt="Error including image file." />
      </div>
     </body>
    </html>

#### Anchors, `<a>`

Anchors are also erroneously referred to as links. If you specify value for the "href" attribute, a user can click on an anchor element to be directed to another document on the World Wide Web.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Anchors in HTML | Richard Le Guen</title>
     </head>
     <body>
      <h1>Anchors</h1>
      <p>
       Click <a href="http://www.google.ca">here</a> to search the Internet
        using the Google Search Engine.
      </p>
     </body>
    </html>

#### Span `<span>`

Like a `<div>`, a `<span>` has no semantic meaning. It is just an inline element used to organize the content of a document. Again, you’ll probably want to use the "class" and "id" attributes to distinguish between `<span>` elements.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Span elements in HTML | Richard Le Guen</title>
     </head>
     <body>
      <h1>The &lt;span&gt;</h1>
      <p>
       Hello World! <br />
       <span class="sentence">
        This is an example of using span elements.
       </span>
       <span class="sentence">
        Example by
        <span class="name">Richard Jean-Paul Le Guen</span>
        for
        <span class="course">SOEN 287</span>
       </span>.
      </p>
     </body>
    </html>

#### Input `<input />`

Input elements are empty (self-closing) elements, nested inside inside form elements. They allow users to interact with a web site. We will see them in the future.

Common HTML Attributes
----------------------

### The "id" Attribute

The "id" attribute can give a unique name to an element in your document. Doing this can allow both style sheets and scripts to target that element specifically.

Since the "id" attribute should be unique throughout the docment, you can also target that element in a document with an anchor element. To do this, append an octothorpe "#" and the id to the end of the url in the "href" attribute.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Using the ID Attribute | Richard Le Guen</title>
     </head>
     <body>
      <div id="Header">
       <h1 id="PageTitle">The &lt;span&gt;</h1>
       <div id="TableOfContents">
        <p>Click <a href="#MainBody">here</a> to go to the main body.</p>
        <p>Click <a href="#Footer">here</a> to go to the footer.</p>
       </div>
      </div>
      <div id="MainBody">
       This is the main body of my page.
      </div>
      <div id="Footer">
       Page by Richard Jean-Paul Le Guen
      </div>
     </body>
    </html>

### The "class" Attribute

The "class" attribute can add further semantic meaning to an element in a document. Using style sheets you can also specify changes in appearance to all elements belonging to a particular class.

An element can belong to multiple classes; the attribute value should be all the names the classes, seperated by spaces.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Class Attributes in HTML | Richard Le Guen</title>
     </head>
     <body>
      <h1>Class Attributes</h1>
      <div id="NavigationBar">
       <a href="home.html" class="Navigation">Home</a>
       <a href="news.html" class="Navigation">News</a>
       <a href="about.html" class="Navigation">About</a>
       <a href="contact.html" class="Navigation">Contact</a>
       <a href="http://google.ca" class="Navigation External">Google</a>
      </div>
     </body>
    </html>

In the example, I can very easily use CSS to ensure that all the links in the Navigation Bar look the same, since they are all of the same class. Note that the last link belongs to both the "Navigation" and the "External" classes.

### The "title" Attribute

The title attribute allows you to give a descriptive title to any element in your document. Most browsers will display the title in a kind of floating label when the mouse hovers over the element. A popular example of the use of titles are the comments which appear when you let your mouse rest over a comic on [xkcd.com](http://www.xkcd.com).

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Title Attributes in HTML | Richard Le Guen</title>
     </head>
     <body>
      <p>Let the mouse rest over the image to see the title:</p>
       <img src="http://www.google.ca/logos/logo.gif" title="The Google logo!" alt="The Google logo" />
     </body>
    </html>
