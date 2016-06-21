def test_default_config(testdir):
    """
    If no --consul-binary is given on command line, use 'consul', which
    will find the binary in the path.
    """
    testdir.makepyfile(
        """
        def test_default(request):
            assert request.config.option.consul_binary == 'consul'
        """
    )
    result = testdir.runpytest()
    assert result.ret == 0


def test_binary_config(testdir):
    """
    If a --consul-binary is specified, honor the option.
    """
    testdir.makepyfile(
        """
        def test_config_option(request):
            assert request.config.option.consul_binary == '/spam/eggs'

        def test_module_state():
            from pytest_consul.plugin import plugin_state
            assert plugin_state['consul_binary'] == '/spam/eggs'
        """
    )
    result = testdir.runpytest('--consul-binary', '/spam/eggs')
    assert result.ret == 0
