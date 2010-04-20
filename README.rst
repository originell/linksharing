=================
django-linksharing
=================

--
is
--

there to give you the possibility to share links with users.

Requirements
============

+ python_ >= 2.4
+ django_ >= 1.1

Installation
============

Use the included setup.py

::

    python setup.py install

Then open up your project's urls.py and include this app's urls.
For example:

::

    (r'^links/', include('django_linksharing')),

TODO
====

* Use reverse/resolve
* Maybe some kind of friendship system (news feed?)
* AJAX to fill description automagically

.. _python: http://www.python.org/
.. _django: http://www.djangoproject.com/
