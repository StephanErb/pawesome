Welcome! Pawesome!
==================

Example project for the EuroPython talk `Release Management with Devpi`_

Install
-------
   
    pip install -r requirements.txt


Upload to Devpi
---------------
   
The following command sequence will upload code and documetation to the given 
Devpi server. Packages are uploaded as wheel and source distributions. Upload
settings are defined in `setup.cfg`.
  
.. code:: bash

    devpi use http://mydevpi/myuser/myindex
    devpi login myuser

    devpi upload # performs build and upload



.. _Release Management with Devpi: https://ep2015.europython.eu/conference/talks/release-management-with-devpi)

