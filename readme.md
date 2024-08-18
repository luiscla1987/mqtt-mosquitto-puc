```bash
    systemctl status mosquitto
    systemctl stop mosquitto
    systemctl start mosquitto

    mosquitto_pub -h 192.168.0.10 -p 1884  -u luis -P 123456 -t /sensor1 -m test

````

Sistema Operacional: Ubuntu 24.04 LTS


* Instalacao:
    ```bash
        sudo apt install mosquitto
    ```
