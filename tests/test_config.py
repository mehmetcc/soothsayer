from soothsayer.config import ConfigurationService

def test_valid_input_given_should_read_host_field():
    config = ConfigurationService().load()
    assert config["Server"]["host"] == "localhost"


def test_valid_input_given_should_read_port_field():
    config = ConfigurationService().load()
    assert config["Server"]["port"] == "6666"