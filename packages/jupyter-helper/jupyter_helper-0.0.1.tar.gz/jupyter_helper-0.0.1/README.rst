Installation
------------

Install via pip:
  pip install jupyter-helper

Or you can use an editable install with:
  git clone https://github.com/lll9p/jupyter-helper.git
  cd  jupyter-helper
  pip install -e . --no-build-isolation


Usage
-----

to run:
  from helper import Helper
  helper = Helper(scope=globals())
  helper.set_global_values().import_libs().run_magics().done()

or
  helper.done()
