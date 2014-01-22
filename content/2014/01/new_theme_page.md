Title: New Theme For the Blog
date: 2014-01-22 00:18
tag: blog
category: blog
summary:  Announcing new blog page and theme

Over the weekend, I attempted to resurrect my old website/blog. The whole exercise
reminded me why I stopped around the last time, namely, the sheer tedium of
tweaking css/html to get things just right.

Luckily, this time around I discovered [pelican](http://getpelican.com), a
static blog generator. It is based on *python* and comes with a decent number of
plugins. These plugins can be used to dramatically extend or add functionality
to your website.  I ended up picking the liquid-plugins because it allows me to
directly insert IPython notebooks, images, and more. Incidentally, the
*liquid_plugins* was built by the famous Jake Vanderplas (of mpl3d fame). He had
a nice write-up detailing how to set up liquid-plugins with pelican. Its
customizable enought that I was able to add a table of contents to my
notebook-based post in no time. I also ended up adding a caption option to the
liquid images.

Next, I took the *simply* theme from [Greg Reda](gjreda.com). I really liked the
responsive theme. But at the end, I ended up completely gutting the design and
going with my own. So much so that I now have the moonlake theme for pelican. 
Its on my github repo.  Feel free to use it as you see fit. 
