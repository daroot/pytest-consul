pytest-consul 
=============

pytest-consul is a pytest plugin meant for being able to do integration and
unit testing against [Hashicorp's Consul](https://www.consul.io/).

This plugin is heavily influenced by the design of 
[DisposableConsul](https://github.com/EverythingMe/disposable-consul).

Install
-------

   $ pip install pytest-consul

Usage
-----

When pytest-consul is installed, the fixtures available will ensure that an
actual local consul agent in bootstrap mode is running.   The fixture object
contains a dictionary containing each of the exposed consul ports by name.

The `consul` fixture is session scoped.  All tests using it will share catalog
and kv state.

    def test_consul_thing(consul):
        http_port = consul['http']
        my_app.register_consul(('localhost', http_port))
        my_app.do_something_that_writes_to_consul_kv()
        resp = requests.get('http://localhost:{port}/v1/key/my-test-key'.format(
            port=http_port))
        actual_value = base64.b64decode(resp.json()[0]['Value'])
        assert actual_value == 'my-expected-value'


The `consul_clean` fixture is function scoped.  If you want a clean consul state 
for a given test, this fixture will provide it.


Note
----

The consul agent takes a second or two to start up, even in bootstrap mode.
This makes these fixtures better for integration style tests, rather than unit
tests.  Using the function scope `consul_clean` in particular is going to add
that additional latency to every single test which uses it.  The flip side of
this is that using the session scope `consul` will not give you test isolation;
if your tests leave values in the kv store or catalog, it may affect any tests
that run after them.


Options
-------

pytest-consul adds the option `--consul-binary` to py.test, allowing you to
utilize a specific consul binary.  By default, it will pick the first `consul`
available in the PATH.
