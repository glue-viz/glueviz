The glueviz meta-package
========================

This package does not contain any code, but instead is a meta-package that 
depends on the core glue code as well as stable plugins that we want to 
provide to users by default. 

It can be installed with::

    pip install glueviz

This currently installs:

* `glue-core <https://github.com/glue-viz/glue>`_, the main glue package
* `glue-vispy-viewers <https://github.com/glue-viz/glue-vispy-viewers>`_,
  which adds 3D viewers

In future, as more plugin packages become stable, we will include them
in this meta-package.

Issues should be opened `in the repository for the main glue package
<https://github.com/glue-viz/glue>`_.
