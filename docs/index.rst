.. eBird Dataset Data documentation master file, created by
   sphinx-quickstart on Tue Dec 24 07:15:15 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

eBird Dataet Data
================
.. include:: ../README.rst
    :start-after: overview-start
    :end-before: overview-end

The Cornell Laboratory of Ornithology in Ithaca, New York runs the eBird database
which collects observations of birds from all over the world. All the observations
are published on `eBird.org`_, and they also make them available via the `eBird Basic Dataset`_,
which is available on the 15th of each month. This project contains a loader and 
models to take load the data (CSV) files into a database. From there you can analyse 
the data with python, jupyter notebooks, or build a web site.

To get started, you will need to `sign up`_ for an eBird account, then `request access`_,
which usually takes 7 days to be reviewed and approved.

.. _eBird.org: https://ebird.org
.. _sign up: https://secure.birds.cornell.edu/identity/account/create
.. _request access: https://ebird.org/data/download
.. _eBird Basic Dataset: https://science.ebird.org/en/use-ebird-data/download-ebird-data-products

Table of Contents
-----------------
.. toctree::
   :maxdepth: 1

   install
   loaders
   database
   demo
   changelog
   license
