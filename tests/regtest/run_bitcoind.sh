#!/usr/bin/env bash
export HOME=~
set -eux pipefail
mkdir -p ~/.telestai
cat > ~/.telestai/telestai.conf <<EOF
regtest=1
txindex=1
printtoconsole=1
rpcuser=doggman
rpcpassword=donkey
rpcallowip=127.0.0.1
zmqpubrawblock=tcp://127.0.0.1:21441
zmqpubrawtx=tcp://127.0.0.1:21441
fallbackfee=0.0002
[regtest]
rpcbind=0.0.0.0
rpcport=18554
EOF
rm -rf ~/.telestai/regtest
screen -S telestaid -X quit || true
screen -S telestaid -m -d telestaid -regtest
sleep 6
telestai-cli createwallet test_wallet
addr=$(telestai-cli getnewaddress)
telestai-cli generatetoaddress 150 $addr > /dev/null
