Which tools to use to plot charts
=================================

:Priority: MEDIUM


Rationale
---------

**As a** `developer`, **I** need to define what tools to use to plot good and
interactive charts to be used in reports, **so that** we can identify all
possible patterns and start developing all implied tools.


Description
-----------

The most basic level is defined by `Matplotlib`_.  The most common base for
data analysis tools is `pandas`_, it extends `Matplotlib`_ to produce charts
based on its data manipulation results.

There are a more elaborated list to evaluate with support for interactive
charts:

- `Plotly Python <plotly_>`__: Graphing Library.  See also `Plotly JavaScript
  <plotly.js_>`__ (A standalone JavaScript data visualization library, that
  powers the Python and R modules).
- dash_: Framework based on `plotly` for rapidly building data apps in Python,
  R, Julia, and F#.  See also the `code repository <dash-git_>`__.
- `Google Chart <gchart_>`__: Display live data on your site.
- vega_: Declarative language for creating, saving, and sharing interactive
  visualization designs.  See also the `code repository <vega-git_>`__.
  See flasked-altair_, a demo Flask application of using Altair_ to generate
  D3 charts using Vega grammar.
- seaborn_: Statistical data visualization.
- `kaleido`_ is a static image export for web-based visualization libraries
  with zero dependencies.
- streamlit_: Faster way to build and share data apps.

Check also the site `five Python Libraries for creating interactive plots
<py5ip_>`__.

.. _matplotlib: https://matplotlib.org/
.. _pandas: https://pandas.pydata.org/
.. _gchart: https://developers.google.com/chart
.. _kaleido: https://medium.com/plotly/introducing-kaleido-b03c4b7b1d81
.. _plotly: https://plotly.com/python/
.. _plotly.js: https://plotly.com/javascript/
.. _dash: https://dash.plotly.com/
.. _dash-git: https://github.com/plotly/dash
.. _vega: https://vega.github.io/
.. _vega-git: https://github.com/vega
.. _flasked-altair: https://github.com/lemoncyb/flasked-altair
.. _altair: https://github.com/altair-viz/altair
.. _seaborn: https://seaborn.pydata.org/
.. _streamlit: https://streamlit.io/
.. _py5ip: https://mode.com/blog/python-interactive-plot-libraries/
