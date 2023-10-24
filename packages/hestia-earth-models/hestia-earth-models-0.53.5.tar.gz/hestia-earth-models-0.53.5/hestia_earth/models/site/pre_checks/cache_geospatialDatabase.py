"""
Site Pre Checks Cache Geospatial Database

This model caches results from Geospatial Database.
"""
from functools import reduce
from hestia_earth.utils.tools import flatten

from hestia_earth.models.geospatialDatabase.utils import (
    MAX_AREA_SIZE, CACHE_VALUE, CACHE_AREA_SIZE,
    has_geospatial_data, has_coordinates, get_area_size, geospatial_data, _run_query, _collection_name
)
from hestia_earth.models.geospatialDatabase import list_ee_params
from hestia_earth.models.utils.site import CACHE_KEY, related_years
from hestia_earth.models.log import debugValues

REQUIREMENTS = {
    "Site": {
        "or": [
            {"latitude": "", "longitude": ""},
            {"boundary": {}},
            {"region": {"@type": "Term", "termType": "region"}}
        ]
    }
}
RETURNS = {
    "Site": {}
}


def cache_site_results(results: list, collections: list, area_size: int = None):
    def _combine_result(group: dict, index: int):
        collection = collections[index]
        name = collection.get('name')
        value = results[index]
        data = (group.get(name, {}) | {collection.get('year'): value}) if 'year' in collection else value
        return group | {name: data}

    return reduce(_combine_result, range(0, len(results)), {}) | (
        {CACHE_AREA_SIZE: area_size} if area_size is not None else {}
    )


def _extend_collection(name: str, collection: dict, years: list = []):
    data = collection | {'name': name, 'collection': _collection_name(collection.get('collection'))}
    return [
        data | {
            'year': str(year)
        } for year in years
    ] if 'reducer_annual' in collection and 'reducer_period' not in collection else [data]


def list_collections(years: list, include_region: bool = False):
    ee_params = list_ee_params()
    # only cache `raster` results as can be combined in a single query
    rasters = [value for value in ee_params if value.get('params').get('ee_type') == 'raster']
    rasters = flatten([
        _extend_collection(value.get('name'), value.get('params'), years) for value in rasters
    ])

    vectors = [
        value for value in ee_params if all([
            value.get('params').get('ee_type') == 'vector',
            value.get('params').get('collection')
        ])
    ]
    vectors = flatten([
        _extend_collection(value.get('name'), value.get('params')) for value in vectors
    ]) + ([{
        'ee_type': 'vector',
        'collection': _collection_name(f"gadm36_{level}"),
        'fields': f"GID_{level}",
        'name': f"region-{level}"
    } for level in range(0, 6)] if include_region else [])

    return (rasters, vectors)


def _cache_results(site: dict, area_size: float):
    # to fetch data related to the year
    years = related_years(site)
    include_region = all([has_coordinates(site), not site.get('region')])
    rasters, vectors = list_collections(years, include_region=include_region)

    raster_results = _run_query({
        'ee_type': 'raster',
        'collections': rasters,
        **geospatial_data(site)
    })

    vector_results = _run_query({
        'ee_type': 'vector',
        'collections': vectors,
        **geospatial_data(site)
    })

    return cache_site_results(raster_results + vector_results, rasters + vectors, area_size)


def _should_cache_results(site: dict):
    area_size = get_area_size(site)
    contains_geospatial_data = has_geospatial_data(site)
    contains_coordinates = has_coordinates(site)
    has_cache = site.get(CACHE_KEY, {}).get(CACHE_VALUE) is not None

    debugValues(site,
                area_size=area_size,
                MAX_AREA_SIZE=MAX_AREA_SIZE,
                contains_geospatial_data=contains_geospatial_data,
                has_cache=has_cache)

    should_cache = all([
        not has_cache,
        contains_coordinates or area_size <= MAX_AREA_SIZE,
        contains_geospatial_data
    ])
    return should_cache, area_size


def run(site: dict):
    should_cache, area_size = _should_cache_results(site)
    return {
        **site,
        CACHE_KEY: {**site.get(CACHE_KEY, {}), CACHE_VALUE: _cache_results(site, area_size)}
    } if should_cache else site
