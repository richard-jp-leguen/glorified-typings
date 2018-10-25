HTML: HyperText Markup Language
===============================

Basic HTML Concepts
-------------------

HTML is a markup language, not a programming language. It is used to annotate (or structure) the content and information found in a document. It is **not** supposed to be used to alter a document’s appearance. So here is a very basic example:

    Hello <em>world</em>!

In this example, I have some text ( "Hello world!" ) and I have specified that there is an emphasis on the word ‘world’ by putting an _open tag_ `<em>` before it and a _closing tag_ `</em>` after it. We could also say that "world" is inside an emphasis _element_.

Another example:

    <p>I <strong>hate</strong> Richard Le Guen.</p> <p>He is a terrible tutor.</p>

Here, I have written the words "I hate Richard Le Guen. He is a terrible tutor." We have two paragraph elements, `<p>`, and a `<strong>` element. The `<strong>` element is _nested_ inside of the first paragraph element.

### Viewing the HTML Document in a Browser

Copy-paste the example into a text file, and save it as a `.html` file. Then open that file using a web browser of your choosing. The word "hate" should look stronger, and the two sentences should be seperated by a line break. This brings us to basic HTML concept #1:

### White Space Doesn’t Matter

In HTML, any amount of continuous white space – once it is rendered in a web browser – is reduced to a single space. So the previous example, and the following…

    <p>
     <strong>
      hate
     </strong>
     Richard Le Guen.
    </p>
    <p>
     He is a terrible tutor.
    </p>

… effectively describe the same document. Only the tags determine where line breaks will go. This does **not** mean that you should just use `<p>` tags wherever you need a new line; `<p>` elements represent paragraphs. If you need a line break in a paragraph, use the `<br />` tag.

    <p>
     Once upon a midnight dreary, <br />
     While I pondered weak and weary, <br />
     Over many a quaint and curious volumes of forgotten lore. <br />
     While I nodded – nearly napping <br />
     Suddenly there came a tapping <br />
     As of someone gently rapping, <br />
     Rapping at my chamber door <br />
     "'Tis some visitor" I muttered, <br />
     "Rapping at my chamber door" <br />
     "Only this and nothing more…" <br />
    </p>

Here – since "The Raven" is a poem – I need lots of line breaks, but I don’t want every line to be a paragraph; that doesn’t make sense. Instead, I’ve put the first stanza in a paragraph element `<p>` and put a `<br />` tag at the end of each line.

### Tags Should Always Be Closed

Tags should always be closed. The following is not valid…

**The Following is a Fail:**

    Hello <span>World!

… as the `<span>` element is not closed. Aditionally, you have to close tags in the order they are opened, so this is not valid either:

**The Following is a Fail:**

    <span>Hello<em></span>World</em>!

You might have noticed that the `<br />` tag doesn’t come in a pair (open-close) like the other tags we’ve seen. That wouldn’t make sense ("`<br>This is a new line?</br>`") so the `<br />` tag is an example of an _empty tag_ or a _self-closing tag_: the tag closes itself, hence why there is a slash (‘`/`’) in the tag before the ‘`>`’.

You _can_ get away with not closing your `<br />` tags, and using `<br>` instead, but this is a dated practice and a bad habit, and it will cause you grief when you start writing XML.

### Images and Attributes

You can include references to images in HTML content. An image tag is another empty (self-closing) tag.

    <p>Look at this pretty picture: <img src="lena.jpg" /></p>

Here we have a paragraph, and in it is a reference to an image. Here we also see our first _attribute_: attributes are values contained in the open tag of an element. So the above example includes an empty `<img>` tag, representing an image element, which in turn has an attribute name `src` whose value is `lena.jpg`. Attributes can mean many things; in this particular situation `src` is the file in which our image is found.

Take note that the attribute’s value is in quotation marks. You can get away with not quoting the attribute value, but this is again a dated practice and a bad habit which will cause you grief when writing XML. You can use either single quotes or double quotes.

### HTML Entities

You might be wondering what to do if you have an attribute whose value contains a quotation mark:

**The Following is a Fail:**

    <p>
     Look at this pretty picture:
     <img src='lena.jpg' title='it s the beautiful Lena' />
    </p>
    <p>
     Look at this pretty picture:
     <img src="lena.jpg" title="it's the beautiful Lena" />
    </p>

… you might also be wondering if you can use the less than `<` and greater than `>` characters normally. (you shouldn’t)

**The Following is a Fail:**

    <p>Greater Than:> </p> <p>Less Than:< </p>

The solution to the above problems are _HTML entities_. You can replace any ‘special’ or reserved character with an ampersand `&` followed by a code and a semicolon `;` like so:

    <p>
     Look at this pretty picture:
     <img src='lena.jpg' title='it&quot;s the beautiful Lena' />
    </p>
    <p>
     Greater Than:&gt; </p> <p>Less Than:&lt;
    </p>

You can also represent HTML entities with an ampersand `&`, an octothorpe `#`, a numeric value, and a semicolon `;`:

    L&#8217;universit&eacute; Concordia<br />Montr&eacute;al, Qu&eacute;bec

For a full list of HTML entities, visit the [w3schools reference page](http://www.w3schools.com/tags).

Again, you can afford not to use HTML entities sometimes, but it is bad practice, and can lead to major security vulnerabilities in your web site.

### Comments

You can include comments in an HTML document. Comments are their own special type of element, and their opening and closing tags look different they begin with `<!–` and end with `–>`.

    <p>
      Hello
      <!-- This is a comment; it will not appear when the page is rendered -->
     World!
    </p>

HTML Documents
--------------

So far we’ve seen the basics of HTML, but we have yet to see a complete, valid, HTML document. Here is the simplest complete, valid HTML document I can come up with:

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
                "http://www.w3.org/TR/html4/strict.dtd">
    <html>
     <head>
      <title>My First HTML Document | Richard Le Guen</title>
     </head>
     <body>
      <h1>My First HTML Document</h1>
      <p>Hello World!</p>
     </body>
    </html>

Some important points:

*   The first two lines look like madness; it is a _DOCTYPE declaration_. It specifies what version of HTML your document is written in, and consequently affects how browsers may try to render your HTML document into a web page. The doctype should be on only one line, but due to the width of my web site I’ve had to put it on two. This is stil valid, but one line is better.
*   After the Doctype declaration, the rest of the document is contained inside a single `<html>` element.
*   The `<html>` element has only two immediate children nested inside of it; a `<head>` and a `<body>`. The contents of the `<head>` don’t seem to be visible when you render the page in a browser…
    *   In the `<head>` element we have a `<title>` element, which is the name of the page as it will appear in either the title bar of the browser window, or in the title part of the browser tab.
*   Any text inside our `<body>` element is again nested inside another element (either an `<h1>` or a `<p>`).

Remember: Structure, Not Appearance
-----------------------------------

Remember that HTML is used to denote the structure of a document; not the appearance. There are obsolete tags like `<font>` or `<b>` (for bold) or `<u>` (for underline) but you should not use them as they are dated, obsolete, and bad practice. Instead, you should use Cascading Style Sheets (CSS) to affect the appearance of a document, which we will cover soon enough.
