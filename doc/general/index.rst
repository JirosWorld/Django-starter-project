.. _general_index:

===================
General information
===================

This section briefly describes the project structure and framework that was
used to built this project.


JavaScript
==========

JavaScript code is written in ECMAScript 2015 (ES6) and transpiled using webpack
and babel. Therefore, all non-compiled code is placed outside the static directory
into ``src/{{ project_name|lower }}/js/``.

All third party libraries should be installed using npm::

    $ npm install --save <package>

or::

    $ npn install --save-dev <package>

After installing libraries can be included using ES6 imports::

    import <package> from '<package>';

**Exceptions**

When you need to override third-party JavaScript you still need to manually place
files into ``src/{{ project_name|lower }}/static/``.
