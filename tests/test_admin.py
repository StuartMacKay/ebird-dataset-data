from django.urls import reverse

from ebird.dataset.data import models

import pytest

pytestmark = pytest.mark.django_db

models = [
    models.Checklist,
    models.Location,
    models.Observation,
    models.Observer,
    models.Species,
]

# Don't include tests for the delete view as we're testing against
# a live database and deleting a Location which will trigger generating
# a list of all Checklists and all Observations, which is going to
# take a while.

@pytest.mark.parametrize("model", models)
def test_changelist_view(admin_client, model):
    url = reverse("admin:data_%s_changelist" % model.__name__.lower())
    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize("model", models)
def test_add_view(admin_client, model):
    url = reverse("admin:data_%s_add" % model.__name__.lower())
    response = admin_client.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize("model", models)
def test_change_view(admin_client, model):
    obj = model._default_manager.last()
    url = reverse("admin:data_%s_change" % model.__name__.lower(), args=(obj.pk,))
    response = admin_client.get(url)
    assert response.status_code == 200
