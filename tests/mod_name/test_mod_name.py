import mod_name
from mod_name import runner

def test_print_str():
    assert mod_name.__version__ == '0.0.1a0', 'version is incorrect'
    runner.print_str("Version is %s" % mod_name.__version__)