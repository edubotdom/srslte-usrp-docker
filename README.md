## A USRP-friendly image for LTE experimentation

Pulls the srsLTE project [srsLTE] last version avaiable, the USRP drivers from the [Ettus Research PPA] and installs them, with the USRP as targeted SDR front-end.

Build with:

    docker-compose up

## Build args

* `UBUNTU_VERSION` codename of the base Ubuntu (default `focal`)

## Deploy

Execute `srsepc_if_masq.sh` script, included inside the repository, to perform IP masquerading, where `<out-interface>` is the interface that connects PC to internet.

    sudo srsepc_if_masq <out_interface>

Run with:

    ./start.sh

It is recommended to run two separate containers, and run separately the two components. In the `srsLTE_conf.py` file you can find a script that simplifies the configuration process of MCC, MNC and Band, including the possibility to register a new user. It should be run inside the two containers, as the repository is cloned in path `./`. To run every component, commands are the following.

Run srsENB:

    srsenb

Run srsEPC
    
    srsepc

Use `uhd_find_device` to check if the container sees the USRP. 
  
If you want to run GUI applications within the container (also works via SSH):

    ./xstart.sh


[srsLTE]: https://github.com/srslte/srslte
[Ettus Research PPA]: https://launchpad.net/~ettusresearch/+archive/ubuntu/uhd
