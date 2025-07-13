============
Loading Data
============
eBird Dataset Data has a loader the `eBird Basic Dataset`_, which is
published on the 15th of each month. The dataset is published as a
zipped, tab-delimited CSV file. The files are very large so loading
them is going to take a while:

.. code-block:: console

    python manage.py load_dataset ebird_basic_dataset.csv

.. _eBird Basic Dataset: https://support.ebird.org/en/support/solutions/articles/48000838205-download-ebird-data#anchorEBD
