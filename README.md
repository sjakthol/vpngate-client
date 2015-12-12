A client for connecting to [vpngate.net](http://vpngate.net) OpenVPN servers.

__Features__:
* filters VPN servers by their geographical location (country or VPNs in Europe)
* probes the VPN endpoints to detect ones that aren't responding for some reason
before connecting to the VPN server
* once connected, performs a speed-test for the VPN and lets you decide if the
speed is good enough for you or if you want to try the next one on the list

## Dependencies
This client has following dependencies:
* [python](https://python.org) (at least v3.3)
* [OpenVPN](https://openvpn.net/)

## Usage

Note: `sudo` is required for OpenVPN.

### Simple Case
```shell
  sudo ./vpngate-client
```

This tries the VPN servers one-by-one ordered by their score and asks you to
choose the one you like.

### Filter by Country
```shell
  sudo ./vpngate-client --country CA
  sudo ./vpngate-client --us # --us is a shorthand for --country US
```

The above command only considers VPN servers in Canada. The country identifier
is a 2 digit code (ISO 3166-2).

### VPNs in Europe
```shell
  sudo ./vpngate-client --eu
```

As a special case, the `--eu` flag only considers VPN servers in Europe.

### Other Options
All the command line options are available by running `./vpngate-client --help`.
