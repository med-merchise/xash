After installation tasks
========================

Rationale:

  After adding `xash` as a dependency in a project, check this list of tasks.


Full list
---------

- Check this same section for all dependencies:

  + `xit`
  + `xit.books`

- To install `scipy`, the `python` version constraint had to be changed from
  using caret (``"^3.10"``) to use tilde (``"~3.10"``).  This was to avoid a
  `poetry` dependency error.  See also `poetry issue #4316 <pi4316_>`__, and
  `poetry dependency specification <ppds_>`__.

.. _pi4316: https://github.com/python-poetry/poetry/issues/4316
.. _ppds: https://python-poetry.org/docs/dependency-specification/

- To generate static images for web-based visualization libraries, for example
  when integrating Jupyter Notebooks in Sphinx (see MyST-NB_, and `xit.books`_
  documentation), a library like Kaleido_ must be used.

  .. note:: Check this!

     When I added this package using ``poetry``, it selected the version
     ``"^0.2.1.post1"``.  Then the ``install`` command could not locate a
     version compatible with it, to solve the problem ``"0.2.1"`` was used.

.. _myst-nb: https://github.com/executablebooks/MyST-NB
.. _Kaleido: https://github.com/plotly/Kaleido
.. _xit.books: https://github.com/med-merchise/xit.books
