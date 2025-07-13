====
Demo
====

If you check out the code from the repository there is a fully functioning
Django site. It only contains the admin pages, but that is sufficient for
you to browse the data.

.. code-block:: console

    git clone git@github.com:StuartMacKay/ebird-dataset-data.git
    cd ebird-dataset-data

Create the virtual environment:

.. code-block:: console

    uv venv

Activate it:

.. code-block:: console

    source venv/bin/activate

Install the requirements:

.. code-block:: console

    uv sync

Run the database migrations:

.. code-block:: console

    python manage.py migrate

Create a user:

.. code-block:: console

    python manage.py createsuperuser

Now, load the sample eBird Basic Dataset file from the data directory:

.. code-block:: console

    python manage.py load_dataset data/downloads/ebird_basic_dataset_sample.csv

Run the demo:

.. code-block:: console

    python manage.py runserver

Now log into the `Django Admin <http:localhost:8000/admin>` to browse the tables.
