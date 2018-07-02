# Vi IMproved (January 14th, 2009)

Vi is a full-screen text editor which is included with almost every distribution of Linux. Some Linux distributions (hopefully those we’re using today in the lab) also come with Vi IMproved, which is an improved, easier-to-use version of Vi. We will be using Vi IMproved (hereafter referred to as vim) to create and edit our Perl scripts this semester, so I have provided this little tutorial on using it, focusing on the things which confused the crap out of me when I first used vim in Soen 229.

## Launching Vim for the First Time

On the command line type the following: (use a file name which does not exist)

    vim myFile.pl

The entire console should go black, with little tilde (‘~’) characters all along its left side. Welcome to Vim. The Vim Editor Has 3 Modes of Operation

*   Visual command mode
*   Colon command mode
*   Text mode

Having just starting vim, you’re in Visual Command Mode. Here are some other things you should notice:

*   Something like `"myFile.pl" 25L, 1175C` should appear in the bottom left corner of the console. That text will disappear later, but for now, it tells you the name of the file you’re editing, or the name it will have once you save. The `25L` would mean that the file is 25 lines long, and `1175` would mean the file containing 1175 characters.
*   Still along the bottom, further to the right, you have two integers separated by a comma. The first is the line number – how many lines you are from the beginning of the file – and the second is how many characters you are into that file.
*   Once along the bottom, and still further right _again_ you’ll see the word ‘Top’. If you’ve moved the cursor, you may see a percentage, or even the word ‘Bottom’. This tells you approximately how deep into the file the position of the entire screen is.

## Performing a Forward Search

So let’s start playing around in vim’s Visual Command Mode! Let’s start by performing a forward search:

*   type in ‘/’ followed by a String of your choosing. What you type should appear at the bottom of the console.
*   Hit enter; the cursor should have moved to the next occurrence of that String.
*   To continue searching, you can hit ‘n’.

The cursor should no longer be at the beginning of the file. Since we’re still in Visual Command Mode, we can type in ‘^’ to move the cursor to the beginning of the current line, where we’ll start typing.

## Inserting Text

*   Type in ‘i’ to begin inserting text just before the cursor, and you will now be in Text Mode.
    *   **For now, do not touch the arrow keys;** your cursor is where we want it to be.
*   Type in some new text, and end it with a new line so it’s on its own line.

## Saving

To return to Visual Command Mode you need only hit ‘esc’. If you are happy with the changes you’ve made to the file and are done with vim, you can enter Colon Command Mode by typing in a ‘:’ character. Then type in the ‘wq’ command to write (to file) and quit.

If you don’t want to quit but still want to save, type ‘:’ (to switch to Colon Command Mode) followed by ‘w’ to save without exiting.

## Deleting an Entire Line

Let’s say we’re not happy with those changes, though. We want to delete that line of text we’ve added. So – still in Visual Command Mode – we move the cursor up, back onto the line of text we added. We can type in ‘D’ (note the case) and the entire line will be deleted.

## Undo

However, if you regret this, you can hit ‘u’ (in Visual Command Mode) to undo. Depending on if you’re in vi or vim, you may be able to undo only the most recent action.

## Quit Without Saving

To quit without saving, switch to Colon Command Mode with ‘:’ (if you’re in Text Mode you first have to switch to Visual Command Mode using ‘esc’) and type in ‘q’ meaning quit. If you’ve made any changes to the file, you will have to specify that you want to discard those changes with the ‘q!’ colon command.

## A Not-So-Short Summary

### Visual Command Mode

So once again, when you first launch vim you are in Visual command mode. Here are a few of the things you can do while in visual command mode.

*   Use ‘/’ to perform a forward search. Type in ‘/’ followed by a String you’d wish to search for, then hit enter. The cursor will move to the next occurrence of that String, or your will get a `Pattern not found` message. To continue the search, and find the next occurrence, hit the ‘n’ key, for ‘next’.
*   You could do the exact same thing, but using ‘?’ in the place of ‘/’ to perform a backwards search.
*   Hit ‘D’ if you need to delete the entire line of text where the cursor is currently located.
*   If you made a mistake using ‘D’ to delete an entire line of text, you can try the undo command with the ‘u’ key.
*   If you type in ‘:’ you will switch to Colon Command mode. (see below)
*   if you hit the ‘i’ key you will switch to Text mode and be able to enter text just before the position of the cursor. (see below for more on Text mode)

### More Visual Command Mode (skippable)

*   To move the cursor, you should be able to use the arrow keys. If not…
    *   Use ‘j’ to move down
    *   Use ‘k’ to move up
    *   Use ‘h’ to move left
    *   Use ‘l’ to move right
*   You can move to the beginning of a line with ‘^’ and the end of a line with ‘$’.
*   You can scroll up a page using ‘ctrl+f’ and down using ‘ctrl+j’
*   if you type in ‘I’ the cursor will move to the beginning of the line, you will switch to Text mode and be able to enter text just before the position of the cursor. (see below for more on Text mode)
*   if you hit the ‘a’ key you will switch to Text mode and be able to enter text just after the position of the cursor. (see below for more on Text mode)
*   if you type in ‘A’ the cursor will move to the end of the line, you will switch to Text mode and be able to enter text just after the position of the cursor. (see below for more on Text mode)

### Colon Command Mode

In Colon Command Mode, you can do any of the following:

*   If you want to go to a particular line, type in the line number and hit enter; the cursor will move to that line.
*   Type ‘q’ to exit vim. If you have made unsaved changes to a file, you wil have to use the ‘q!’ command to confirm you wish to discard those changes.
*   Type ‘w’ to save, and continue using vim. To “save as” type in ‘w’ followed by the new file name.
    *   Or you could type ‘wq’ to save and then immediately quit.
*   ‘r _filename_‘ will paste in the contents of another file after the line where the cursor is.

### Text Mode

In Text Mode, you can edit text normally, and return to Visual Command Mode by hitting the ‘esc’ key. Take note that when using vi (as opposed to vim) in Text Mode you won’t be able to use the arrow keys to move the cursor; vi will interpret them as characters.
