# Various OpenStack tools

All utilities require OpenStack credentials present as environment variables.

## Gather baremetal nodes facts using regexable server name

    $ ./osnode.py openhpc .driver_info.[]
    $ ./osnode.py openhpc .driver_info.ipmi_address | jq
    $ ./osnode.py "openhpc-.*" .driver_info.ipmi_address

## Open tmux windows that match server name keyword

    $ ./tmuxipmi openhpc-compute
