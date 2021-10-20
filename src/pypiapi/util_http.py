import urllib3


def get_connection(num_pools: int = 10) -> urllib3.PoolManager:
    """Returns HTTP pool manager with retries and backoff"""
    return urllib3.PoolManager(
        num_pools=num_pools,
        retries=urllib3.Retry(
            total=4,
            backoff_factor=2,
            raise_on_status=True,
            raise_on_redirect=True,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
        ),
    )
