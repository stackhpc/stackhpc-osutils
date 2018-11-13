# Various OpenStack tools

All utilities require OpenStack credentials present as environment variables.

## Installation

    $ pip install .

## Gather baremetal nodes facts using regexable server name

    $ osnode openhpc .driver_info.[]
    $ osnode openhpc .driver_info.ipmi_address | jq
    $ osnode "openhpc-.*" .driver_info.ipmi_address

## Open tmux windows that match server name keyword

    $ tmuxipmi openhpc-compute
