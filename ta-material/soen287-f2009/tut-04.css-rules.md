Understanding CSS Rules
=======================

The format for a style rule is first an _element selector_ (which specifies which elements will be affected by the style rule) and a _declaration block_ (all the style properties and their values in braces `{}`).

The harder part to understand of a CSS rule is the ‘element selector’. We can use the element selector to make the styles in our declaration block apply to several elements. The element selector is used to target those elements, using the element’s tag-name, the element’s `class` and `id` attribute, and other (non-standard) attributes. Each of those techniques has its own special syntax.

Selecting Elements by Targeting Tag Name
----------------------------------------

So here is an example:

    p {
      text-align:right;
     }

This style rule’s element selector dictates that all `<p>` elements will have text aligned to the right.

We can use commas `,` to denote that we’re targetting multiple elements:

    h1, h2, h3, h4, h5, h6 {
      text-decoration:underline;
     }

In this example, we’re specifying that the text in all the header tags should be underlined.

What we’ve seen up until now is referred to as _targetting by element_: we’ve been targetting all occurances of a particular element. Like I said before though, you can also _target by class_, _target by id_, and _select by attribute targets_ in your style rules.

Selecting Elements by Targeting Class
-------------------------------------

Using a period, you can specify that you are targetting an element with a particular `class` attribute. The following rule affects all elements (irrelevant of what element it is) whose `class` attribute includes them in the "Important" class name:

    .Important {
      color:black;
     }

We can combine targeting by element and targeting by `class` to dictate for example that only list items `<li>` with belonging to the "`Important`" class name should be affected:

    li.Important {
      font-weight:bolder;
      color:red;
     }

Selecting Elements by Targeting Id
----------------------------------

Using an octothorpe (#) you can also specify that you are targetting an element with a particular `id` attribute. What follows is a rule which affects only the element with an `id` attribute value of "PageTitle":

    #PageTitle {
      font-variant:small-caps;
     }

Again, you can combine this with targeting by element to specify that the element is affected only if it is a particular element, such as an `<h1>`:

    h1#PageTitle {
      font-variant:small-caps;
      text-decoration:underline;
     }

Selecting Elements by Attribute Targets
---------------------------------------

You can also target elements based on attribute other than `id` and `class` by putting the attribute name in square brackets:

    a[href] {
      font-weight:bolder;
     }

In this example, we are targeting anchor elements `<a>` which have the "href" attribute. We can specify multiple attributes. In the next example we are selecting anchors `<a>` with both href and title attributes:

    a[href][title] {
      font-weight:bolder;
     }

You can also specify a value for the attribute, or a partial value. (partial values are not supported in Internet Explorer)

    img[src="My Image File.jpeg"] {
    			/* an image whose src attribute
    			has a value of "My Image File.jpeg" */
      border:5px solid yellow;
     }
     img[src|="My"] {	/* an image whose src attribute
    			has a value starting with "My" */
      background:blue;
     }
     img[src~="Image"] {	/* an image whose src attribute
    			has a value containing the word "Image" */
      font-weight:bolder;
     }

Selecting Elements by Relationship
----------------------------------

You can also select elements by their relationships to other elements.

### Descendants

The simplest relationship you can specify is to target all _descendants_ (elements nested within it, or nested within elements nested within it…) of an element. In the following example, I’ve specified that all anchors `<a>` within the division `<div>` with an `id` attribute of "`Navigation`" will have purple text:

    div#Navigation a {
      color:#8911CC;
     }

So this example will affect all anchors `<a>` which are inside the "`Navigation`" division `<div>` no matter how ‘deeply’ nested they are. So if we apply this style rule to the following HTML:

    <div id="Navigation">
     <p>
      <a>The first anchor</a>
     </p>
     <a>The second anchor</a>
    </div>

… both anchors `<a>` would have purple text, as they are both descendants of the "Navigation" division `<div>`.

### Immediate Child Elements

If we want only the second anchor `<a>` to be affected (ie the _children_ of the "Navigation" division `<div>`) we would have to use a greater-than character > like so:

    div#Navigation > a {
      color:#8911CC;
     }

Now – if we apply the style rule to the HTML above – only the second anchor will be affected.

### Adjacent Elements

The last relationship we can use to target is adjacent elements. Lets say that whenever an image `<img>` is followed by a paragraph we want the text to be in italics. We would use a plus character + to denote this relationship:

    img + p {
      font-style:italic;
     }

Personally I think this is a litle too general, so it would be a better idea to specify that the paragraph must have the "ImageDescription" class name:

    img + p.ImageDescription {
      font-style:italic;
     }

Instead of the `<style>` Element: Style Sheets
============================================

We have now arrived at style sheets. We’ve been successful at removing messy "style" attributes from all our elements, and put all that information in a style element nested in the document’s head `<head>` element.

This leaves lots of style-pertinent information in our HTML document though, and in our idealistic academic environment, an HTML document can _only_ define structure and contain content.

Linking To a Style Sheet
------------------------

The solution to this problem lies in the "H" part of HTML. If you looked up "HyperText", you’d know a "Hypertext" document is a text document which contains references to other documents and resources which are easy to follow. So far we’ve seen references in the form of anchors `<a>` (do not call them links!) and of images `<img>` and now we’re going to add another kind of reference: the link element.

    <link rel="stylesheet" title="My Default"
    		type="text/css" href="blarg.css" />

Take note: the line break is only there so it will fit on the page!

You can replace then entire style element in your document’s head with a link element. Just copy all your style rules into a .css file. In this case, I’m calling the file "blarg.css" but you can call it whtever you want.

For now keep the CSS file in the same folder as your HTML file.

So – returning to our example document earlier in this tutorial – here are our files:

The CSS File ‘blarg.css’
------------------------

    /* we target the body and specify it has a background */
     body {
      background:black;
     }
     /* we say that any elements * inside the body element are bolder */
     body * {
      font-weight:bolder;
     }
     /* we now target the div with the identifier 'g' */
     div#g {
      overflow:hidden;
      border:10px solid green;
     }
     /* and now all elements * inside the div with the identifier 'g' */
     div#g * {
      color:green;
     }
     /* we now target the div with the identifier 'b' */
     div#b {
      overflow:hidden;
      border:10px solid #000055;
     }
     /* and now all elements * inside the div with the identifier 'b' */
     div#b * {
      color:blue;
     }
     /* we now target any element of the class "Important" */
     .Important {
      color:white;
      text-decoration:underline;
     }

The HTML File
-------------

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
     <head>
      <title>Using the Style Attribute | Richard Le Guen</title>
      <link rel="stylesheet" title="My Default"
    	type="text/css" href="blarg.css" />
     </head>
     <body>
      <h1 class="Important">The Style Attribute</h1>
      <div id='g'>
       <h2>Arrows</h2>
       <p>Ollie, Connor</p>
       <h2>Lanterns</h2>
       <p>Hal, Jon, Kyle</p>
      </div>
      <div id='b'>
       <h2>Beetles</h2>
       <p>Ted… and those other ones</p>
      </div>
      <p class="Important">This is important, so its white and underlined…</p>
     </body>
    </html>

Alternate Page Styles
---------------------

If you want to give your visitors the option to render the page differently, you can include alternate link elements: (there has to be one default/non-alternate stylesheet though)

    <link rel="alternate stylesheet" title="Secondary!"
    			type="text/css" href="alt.css" />

If you add extra alternative link elements like this after the first (and the corresponding CSS files) a visitor can select to view the page using the alternate stylesheet. Try it! In FireFox, click View->Page Style and you should see a list of your stylesheet link elements’ titles.
