import os

from django.conf import settings
from django.core.management import call_command

import pytest

pytestmark = pytest.mark.django_db


def test_loader():
    call_command(
        "load_dataset",
        os.path.join(settings.DOWNLOAD_DIR, "ebird_basic_dataset_sample.csv"))
