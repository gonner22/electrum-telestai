from electrum_tls.i18n import _

fullname = _('SwapServer')
description = """
Submarine swap server for an Electrum-TLS daemon.

Example setup:

  electrum-tls -o setconfig enable_plugin_swapserver True
  electrum-tls -o setconfig swapserver_port 5455
  electrum-tls daemon -v

"""

available_for = ['cmdline']
