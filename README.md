## MyEMS Aggregation Service 数据汇总服务



### Introduction

This service is a component of MyEMS and it aggregates normalized data up to multiple dimensions.

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/myems/myems-aggregation/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/myems/myems-aggregation/?branch=master)


### Prerequisites

mysql.connector



### Installation

Download and install MySQL Connector:
```
    $ cd ~/tools
    $ wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.20.tar.gz
    $ tar xzf mysql-connector-python-8.0.20.tar.gz
    $ cd ~/tools/mysql-connector-python-8.0.20
    $ sudo python3 setup.py install
```

Install myems-aggregation service:
```
    $ cd ~
    $ git clone https://github.com/myems/myesm-aggregation.git
    $ sudo cp -R ~/myems-aggregation /myems-aggregation
    $ cd /myems-aggregation
    $ sudo git checkout master (or the release tag)

    Edit config.py for your project
    $ sudo nano config.py

    Setup systemd service:
    $ sudo cp myems-aggregation.service /lib/systemd/system/

    Enable the service:
    $ sudo systemctl enable feed-aggregation.service

    Start the service:
    $ sudo systemctl start feed-aggregation.service
```

### References

[1]. https://myems.io

[2]. https://dev.mysql.com/doc/connector-python/en/
