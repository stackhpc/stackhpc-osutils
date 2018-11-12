# Various OpenStack tools

## Gather information related to baremetal nodes using server name in a json-esque manner

    $ ./osnode.py openhpc .driver_info.[]
    $ ./osnode.py openhpc .driver_info.ipmi_address | jq
    $ ./osnode.py "openhpc-.*" .driver_info.ipmi_address

## Open tmux windows that match server name keyword

    $ ./tmuxipmi openhpc-compute
