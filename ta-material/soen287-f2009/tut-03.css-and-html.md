CSS: Cascading Style Sheets
===========================

CSS Properties
--------------

Now that you’re using HTML to define the content and structure of your documents, you’re probably itching to control how your documents look in a browser. This can be done with CSS,or Cascading Style Sheets. Using CSS you can specify CSS properties for the elements in your document. Typical CSS properties include:

|CSS Property|Effects|
|--- |--- |
|color|Using the `color` property, you can make changes the font color of the text appearing in the element.|
|font|Change the font and appearance of the text in an element using the `font` property.|
|background|The `background` property can be used to change the background of an element. The `background` property can be specify a uniform single-color background, or a background image.|
|border|The `border` property can affect the color, width and style of border of an element.|
|position|The `position` property allows you to control where an element is rendered on the page.|
|margin|The distance between the edge of an element and the elements around it is modified by the `margin` property.|
|padding|The distance between the edge of an element and the elements inside it is modified by the `padding` property.|
|height|Using CSS you can specify the height of a block level element, or some inline elements like `<img>`.|
|width|Using CSS you can specify the width of a block level element, or some inline elements like `<img>`.|
|overflow|If the content of an element is greater than its height/width, the `overflow` property can be used to determine if it should be visible of hidden, or if a scroll bar should appear etc.|


You can find a more complete list of CSS properties at the [w3schools page](https://www.w3schools.com/cssref/). The purpose of this tutorial is not to list and explain every CSS property, but to convey how to use CSS properly in conjunction with HTML.

The first way we’ll see of doing this is the wrong way to do it: using the `style` attribute.

    <div style='background:black;padding:50px;'>
     <h1 style='color:yellow;text-decoration:underline;'>
      The Style Attribute
     </h1>
     <span style='color:red;font:large "Arial" sans-serif;'>
      Red text.
     </span>
     <span style='color:blue;font:medium "Comic Sans MS" sans-serif;'>
      Blue text.
     </span>
     <span style='color:green;font:large cursive;'>
      Green text.
     </span>
     <span style='color:white;font:large "Arial" sans-serif;font-variant:small-caps;'>
      White text.
     </span>
    </div>

You see that the format for CSS properties and their values is always the name of the property, followed by a colon `:`, the property’s value, and finally a semicolon used to delimit the properties.

Instead of the `style` Attribute: the `<style>` Element
-----------------------------------------------------

So why not use the `style` attribute? The `style` attribute results in the HTML document containing more than just content and structure. As a consequence, when you want to change the appearance, you have to comb through the entire document, changing `style` attributes. Let’s look at a better example:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
     <title>Using the Style Attribute | Richard Le Guen</title>
    </head>
    <body style="background:black;">
     <h1 style='font-weight:bolder;color:white;text-decoration:underline;'>
      The Style Attribute
     </h1>
     <div style='font-weight:bolder;overflow:hidden;border:10px solid green;' id='g'>
      <h2 style='font-weight:bolder;color:green;'>Arrows</h2>
      <p style='font-weight:bolder;color:green;'>Ollie</p>
      <h2 style='font-weight:bolder;color:green;'>Lanterns</h2>
      <p style='font-weight:bolder;color:green;'>Hal, Jon, Kyle</p>
     </div>
     <div style='font-weight:bolder;overflow:hidden;border:10px solid #000055;' id='b'>
      <h2 style='font-weight:bolder;color:blue;'>Beetles</h2>
      <p style='font-weight:bolder;color:blue;'>Ted</p>
     </div>
     <p style='font-weight:bolder;color:white;text-decoration:underline;'>
      This is important, so its white and underlined…
     </p>
    </body>
    </html>

This document would be a lot easier to understand if it didn’t have all the style attributes. Additionally, alot of those style attributes contain redundant properties. Here are some oservations:

*   Everything in the body `<body>` has a `font-weight:bolder;`
*   Everything in the division `<div>` with `id="g"` has a `color:green;`
*   Everything in the division `<div>` with `id="b"` has a `color:blue;`
*   There are two elements which have both `color:white;text-decoration:underline;`

So here is the same document, but now I have added a `<style>` tag in the document’s `<head>` which will contain _style rules_.

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
     <head>
      <title>Using the Style Attribute | Richard Le Guen</title>
      <style>
    <!--
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
    -->
      </style>
     </head>
     <body>
      <h1 class="Important">The Style Attribute</h1>
      <div id='g'>
       <h2>Arrows</h2>
       <p>Ollie, Connor</p>
       <h2>Lanterns</h2>
       <p>Hal, Jon, Kyle&tt;/p>
      </div>
      <div id='b'>
       <h2>Beetles</h2>
       <p>Ted… and those other ones</p>
      </div>
      <p class="Important">This is important, so its white and underlined…</p>
     </body>
    </html>

Some important things to take note of before we proceed and try to understand these style rules a little more in [the next tutorial](tut-04.css-rules.md):

*   I’ve added a `class` attribute to those elements which used to have the `color:white;text-decoration:underline;` style in common. They both have a `class` attribute with a value of "`Important`" now.
*   All the rules in the `<style>` element are in a big HTML comment. This is because they’re not really content that belongs in our HTML document.
*   In our `<style>` element we can include CSS comments, which look just like block comments in Java: anything between `/\*` and `\*/` is not part of a CSS style rule.
