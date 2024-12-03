# Manychrome

This is a package predominantly created for those who prefer working from the CLI. It is to add colours and to style text so to easily make warnings, notification messages, or finding text when searching for it easily pop out.

Simple functions, with an intention to allow the user to simply just type 'write', or 'listme' or similar to get things done. The function names are intended to be logical and selfexplanatory and easy to remember.


# Installation
`pip install manychrome==0.1.0`

To uninstall use: `pip uninstall manychrome==0.1.0`

# Background
This package was created because I prefer to work from the terminal and I wanted a simple way to let certain reminders and text manipulation to easily grab my attention. I also find myself to to repeat code again and again, and therefore wanted to create a package that I could just pip install and use in my different environments without having to repeat it in different directories.

I am new to coding, and this is my first package, so it might not yet follow all the right principles yet I hope it'll over time be helpful to others who also like some colour on their cli.

My intention is to keep adding to it, and make it extremely user friendly.

_For the interested one_ the name manychrome was selected as a play on the word monochrome to reflect it's opposite nature.

# What manychrome contains

## Classes
```python
Colorful()
Stylish()
FindMe()
```

### What Colorful() can be used for
*Colorful:* simple functions that provide the additional benefit of colours when viewing the data.

*Stylish:* the intention of stylish is to provide CLI text styling also without color.

*Findme:* the intention is to easily find placeholders and other items in text and make them stand out in the whole context of the text. This to quickly get an overview of the text pertaining to the words or fragments of interest in the big scheme of things. Also provides an extremely simple and straight forward way to update placeholder text for emails, documents, and invoice creation etc.

# How to Use manychrome

> Use `pip install manychrome==0.1.0`
> Use pip uninstall manychrome==0.1.0 to uninstall it

```python
from manychrome.colorful import Colorful
from manychrome.stylish import Stylish
from manychrome.findme import FindMe
```


## How to use Colorful()

It is extremely easy to get text printed in different colours and styles using manychrome.
To get coloured text simply configure the foreground colour (text color) by setting the fg value,
the background colour by setting the bg colour, and the options of styles can be set by configuring True or False.

### Use like a print() function

```python
c = Colorful(fg=127, bg=55, ul=True)
words = "This is the text that is to be printed."
c.write(words)

c.fg=220
c.bg=17
c.write("This changed the color")

c.bg=0

c.write("This text is now written without having any background colour")

```

### pretty print lists
If you want to print a list in colour (or without setting any colours)
you can use `c.listme(mylist)`.

```python

c = Colorful(fg=204, it=True)
dogs = ["Ziggy", "Bobby", "Dracula", "Leopold"]
c.listme(dogs)

```

### lists with an alternative heading
You can add a heading to your list, that can have the same or a different colour and style than your list text.

```python

c = Colorful(fg=199, it=True)
hst = Colorful(fg=220, bg=33, bo=True)
dogs = ["Ziggy", "Bobby", "Dracula", "Leopold"]
c.listme(dogs, heading=" Doggos ", heading_style=hst)

```

### How to see colour options
The colour functions are based on the xterm-256 colour codes, wrapping the text in anscii escape codes.
Depending on if your IDE or terminal emulator (or whatever you use) uses 16 color mode or can display 256 colours, they will show up differently.

The function `choose_color()` is provided to display the colours in your IDE or terminal.
This function does not belong to any class so simply call the function.


```python
choose_color()

```

save_favs() is a simple function that creates an ini file with the number and then appends to this file.
Currently it only saves one at a time, but I will update this one at a later stage.

```python

keep_me = "manychrome/examples/save_my_colors.ini"
save_favs(keep_me)
# It will ask you to input the number of the one you want to save

```


### How to configure the colours when using Colorful()
For `Colorful()` the configuration can either be set when initiating the instance, or by setting the values. This makes for a super simple view to organise the differences especially when several different instances are created. Text can contain multiple different combinations by using several instances of `Colorful()` for different fragments of the text.

The different styles can also be combined.
For example, text can be both underlined, bold, and italics at the same time.
If just wanting to print normally there is no need to do anything exept instantiate `Colorful()`.
No values are required for normal printing of the text.

See the available configuration options below.

```python
c = Colorful(fg=1, bg=2, it=True)  # All config for Colorful() can be set inside here, or as shown below
c.fg = 1  # Sets the foreground (text) colour
c.bg = 2  # Sets the background colour
c.it = True  # Set it as True for text in italics
c.ul = False  # Set ul as True for underlined text
c.bo = False  # Set bo as True for bold text
c.st = False  # Set st as True for strikethrough
c.sh = False  # Set sh as True to shift the colour between the foreground and the background
c.ft = False  # Set ft as True for faint text. NOTE: This one is having varying effects and is not yet entierly reliable. There are some colours that can be selected in combination that prints very faint text. On my IDE and cli using fg=23, fg=33 prints very faint (but coloured) text.
```


## Functions of FindMe()
See below for the current functions and config for class `FindMe()`

Use it to update values in template text for documents, emails, invoices etc.
Use it as an `in-text span function` to highlight specific sections of text.

It will highlight whatever text you add in your configuration and that you wrap in curly brackets `{}` in your text.


```python
# Set the placeholders, no limit set for the number of placeholders.
f = FindMe(
    placeholder="value"
    company="Awesome company name",
    email="colourful@email.com",
    greeting="Ohoy there",
)
# The template containing the placeholders.
template = "{greeting}. For your template, make sure to wrap the {placeholder} in curly brackets, to update the values, such as {email}, and {company}"

# Configure the style and colour of the placeholder text.
f.fg=220
f.bg=33
f.it=True

# Prints the text.
f.showme(template)
```


## Functions of Stylish()
Stylish is basically a duplication of Colorful and there is a huge amount of overlap.
This will most likely be updated to change overtime.

See below for the current functions and config for class `Stylish()`. There is a substantial overlap and ineffective intermixing between classes so might all get moved to `Colorful()`.

These provide super self explanatory and easy to remember ways to print text on the cli in whatever style. The primary function of the name of these will ignore other configuration settings, thus these can be used in combination where some text is highlighted, and depending of choice it will not be affected by that.

```python
findme(words)  # TODO check this, it's the same as showme(). Make it make sense.
bold(words)  # Prints the text bold.
italics(words)  # Prints the text in italics.
underline(words)  # Prints the text underlined.
strikethrough(words)  # Prints the text strikethrough.
highlight(words)  # Highlights the text in whatever bg colour selected.
swap(words)  # Swaps the fg / bg colours with each other.
```

### How to use Stylish()
```python
For stylish, set config
s = Stylish()
s.fg = 117
s.bg = 218
# Can do s.it = True etc but the functions below aren't affected by that so they can be used in combination with each others.
```
