import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

@pytest.mark.parametrize("user,group", [
    ("dedcon", "dedcon"),])
def test_users(host, user, group):
    usr = host.user(user)
    assert usr.exists
    assert usr.group == group

def test_symlink(host):
    f = host.file("/root/dedcon").is_symlink

    assert f == True

def test_hosts_file(host):
    f = host.file('/root/dedcon/dir')

    assert f.exists
