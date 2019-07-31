# Various OpenStack tools

All utilities require OpenStack credentials present as environment variables.

## Installation

    $ pip install git+https://github.com/stackhpc/stackhpc-osutils

## Gather baremetal nodes facts using server name

Query what keys are available for retrieval:

    $ osutils.node -p openhpc -q '.driver_info.[]'
    ["deploy_kernel", "ipmi_address", "ipmi_username", "ipmi_password", "deploy_ramdisk"]

Get list of `ipmi_address` and format the output using `jq`:

    $ osutils.node -p openhpc -q '.driver_info.ipmi_address' | jq
    [
      {
        "value": "10.45.253.35",
        "key": "openhpc-login-0"
      },
      {
        "value": "10.45.253.11",
        "key": "openhpc-compute-0"
      },
      {
        "value": "10.45.253.12",
        "key": "openhpc-compute-1"
      }
    ]    

Use regex to filter server names:

    $ osutils.node -p 'openhpc-.*0' -q '.driver_info.ipmi_address'
    [{"value": "10.45.253.1", "key": "openhpc-login-0"}, {"value": "10.45.253.22", "key": "openhpc-compute-0"}]

## Open tmux windows that match server name keyword

    $ osutils.ipmi openhpc-compute
    Opening tmux window: openhpc-compute-0
    ipmitool -I lanplus -H 10.45.253.22 -U root -P calvin sol activate
    Opening tmux window: openhpc-compute-1
    ipmitool -I lanplus -H 10.45.253.35 -U root -P calvin sol activate
