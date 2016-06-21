import requests
import base64

# Note that we actually care about the order of these tests,
# which is normally bad form, but in this case we're actually interested in the
# behavior of the session scoped fixture across multiple test and that the
# function scope is not seeing the session scoped one.

# TODO: Consider using pytest-ordering to ensure order.


def test_consul_server_write(consul):
    """
    Given a session consul fixture, we can get the appropriate http port and
    write a value into the kv store.
    """
    assert 'http' in consul and consul['http'] is not None
    port = consul['http']
    resp = requests.put('http://localhost:{port}/v1/kv/spam'.format(port=port),
                        data='eggs')
    resp.raise_for_status()
    assert resp.status_code in range(200, 206)
    assert resp.content.decode('utf-8') == 'true'


def test_consul_server_read(consul):
    """
    Given the same session consul fixture used in the previous test, we
    can retrieve the key we wrote.
    """
    port = consul['http']
    resp = requests.get('http://localhost:{port}/v1/kv/spam'.format(port=port))
    resp.raise_for_status()
    assert resp.status_code in range(200, 206)
    body = resp.json()
    val = base64.b64decode(body[0]['Value']).decode('utf-8')
    assert val == 'eggs'


def test_consul_server_clean(consul_clean):
    """
    A function scoped consul_clean fixture is not going to get the value
    that the session scoped fixture wrote.
    """
    port = consul_clean['http']
    resp = requests.get('http://localhost:{port}/v1/kv/spam'.format(port=port))
    assert resp.status_code == 404
