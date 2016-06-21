from pytest_consul.plugin import _acquire_ports, consul_ports


def test_ports():
    """
    When we ask for ports, we get a dictionary containing a mapping of all the
    ports consul needs to operate.  Each port is in the ephemeral port range.
    """
    ports = _acquire_ports()
    assert set(ports.keys()) == set(consul_ports)
    for port_name, port in ports.items():
        assert port >= 32768
