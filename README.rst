Welcome! Pawesome!
==================

Example project for the EuroPython talk `Release Management with Devpi`_

The following command sequence will upload code and documetation to the given 
Devpi server. Packages are uploaded as wheels and source distributions. Upload
settings are defined in `setup.cfg`.
  
.. code:: bash

    pip install -r requirements.txt

    devpi use http://mydevpi/myuser/myindex
    devpi login myuser

    devpi upload --with-docs # builds before uploading


.. _Release Management with Devpi: https://ep2015.europython.eu/conference/talks/release-management-with-devpi

