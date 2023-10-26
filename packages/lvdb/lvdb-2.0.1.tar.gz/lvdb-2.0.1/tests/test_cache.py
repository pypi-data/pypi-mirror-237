import pytest

import numpy as np


@pytest.mark.cache
def test_set(cache_instance):
    cache_instance.set((1, 2), np.ones(5))
    assert cache_instance.__cache[(1, 2)] == np.ones(5)

@pytest.mark.cache
def test_set_ttl(cache_instance):
    cache_instance.set((3, 5), np.zeros(5), 1)
    assert cache_instance.__cache[(3, 5)] == np.zeros(5)

@pytest.mark.cache
def test_expiration(cache_instance):
    assert not cache_instance.get((3, 5))

@pytest.mark.cache
def test_get(cache_instance):
    assert cache_instance.get((1, 2)) == np.ones(5)