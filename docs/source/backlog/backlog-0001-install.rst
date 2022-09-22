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
