#Creating a Kafka Cluster with Confluent
#Introduction
#https://ssh.instantterminal.acloud.guru/?_ga=2.39112672.212074364.1727950880-1154966438.1727950875
#In this lab, we will have the opportunity to install and configure a three-broker cluster using Confluent Community. We will start with three regular Ubuntu servers and build a working Kafka cluster.
#Solution

#Log in to each of the nodes/servers using the credentials provided on the hands-on lab page:

ssh cloud_user@<PUBLIC_IP_ADDRESS>
#Node 1:54.174.254.62
#Node 2:44.201.206.240
#Node 3:3.92.175.232
#Password: 5-OiS!Z!
#Install the Confluent Community Package on Broker Nodes

    #On all three servers, add the GPG key:
    wget -qO - https://packages.confluent.io/deb/5.2/archive.key | sudo apt-key add -
    #On each server, add the package repository:
    sudo add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/5.2 stable main"
    #On each server, install Confluent Community and Java:
    sudo apt-get update && sudo apt-get install -y openjdk-8-jre-headless confluent-community-2.12

#Configure Zookeeper

    #On each server, edit the hosts file:
    sudo vi /etc/hosts
    #On each server, add the following to the hosts file:
    10.0.1.101 zoo1
    10.0.1.102 zoo2
    10.0.1.103 zoo3
    #Save and exit each file by pressing Escape followed by :wq.
    #On each server, edit the zookeeper config file:
    sudo vi /etc/kafka/zookeeper.properties
    #Delete the contents of the config file, and add the following to the file on each server:
    tickTime=2000
    dataDir=/var/lib/zookeeper/
    clientPort=2181
    initLimit=5
    syncLimit=2
    server.1=zoo1:2888:3888
    server.2=zoo2:2888:3888
    server.3=zoo3:2888:3888
    autopurge.snapRetainCount=3
    autopurge.purgeInterval=24
    #Save and exit each file by pressing Escape followed by :wq.
    #On each server, set up the zookeeper ID:
    sudo vi /var/lib/zookeeper/myid
    #On each server, set the contents of /var/lib/zookeeper/myid to the server's ID:
        On Node 1, enter 1.
        On Node 2, enter 2.
        On Node 3, enter 3.
    #Save and exit each file by pressing Escape followed by :wq.

#Configure Kafka

    #On each server, edit the kafka config file:
    sudo vi /etc/kafka/server.properties
    #Set broker.id to the appropriate ID for each server (1 on Node 1, 2 on Node 2, and 3 on Node 3).
    #On each server, set zookeeper.connect to zoo1:2181.
    #Save and exit each file by pressing Escape followed by :wq.

#Start Zookeeper and Kafka

    #On each server, start and enable the Zookeeper and Kafka services:
    sudo systemctl start confluent-zookeeper
    sudo systemctl enable confluent-zookeeper
    sudo systemctl start confluent-kafka
    sudo systemctl enable confluent-kafka
    #On each server, check the services to make sure they are running:
    sudo systemctl status confluent*
    #Both services should be active (running) on all three servers.
    #On the Node 1 server, test the cluster by listing the current topics:
    kafka-topics --list --bootstrap-server localhost:9092
    #The output should look like this:
    #_confluent.support.metrics

Conclusion
Congratulations on successfully completing this hands-on lab!
