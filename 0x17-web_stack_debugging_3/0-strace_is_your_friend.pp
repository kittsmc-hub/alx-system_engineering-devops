# This Puppet manifest installs a missing module to fix Apache returning a 500 error.

node 'webserver' {
  package { 'missing-module':
    ensure => installed,
  }
}

