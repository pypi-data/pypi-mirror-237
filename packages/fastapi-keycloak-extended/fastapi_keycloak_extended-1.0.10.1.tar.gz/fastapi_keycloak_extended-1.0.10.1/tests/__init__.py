import pytest

from fastapi_keycloak_extended import FastAPIKeycloak


class BaseTestClass:
    @pytest.fixture
    def idp(self):
        return FastAPIKeycloak(
            server_url="https://keycloak.yuluspaces.com:8985",
            client_id="backend",
            client_secret="nAJrimV7bBHqeoCoO4Yve0IS29ckZXAs",
            admin_client_id="admin-cli",
            admin_client_secret="2K58am0ieojvvBremcsR1smWd6qceUJH",
            realm="test-dev",
            callback_uri="http://localhost:8081/callback",
        )
