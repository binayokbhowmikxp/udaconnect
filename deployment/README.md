***********
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/kafka
***********

ec2-user@ip-10-1-2-75:~> export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
ec2-user@ip-10-1-2-75:~> export HELM_KUBEAPISERVER=https://127.0.0.1:6443
ec2-user@ip-10-1-2-75:~> helm repo add bitnami https://charts.bitnami.com/bitnami
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /etc/rancher/k3s/k3s.yaml
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /etc/rancher/k3s/k3s.yaml
"bitnami" already exists with the same configuration, skipping
ec2-user@ip-10-1-2-75:~> helm install my-release bitnami/kafka
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: /etc/rancher/k3s/k3s.yaml
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: /etc/rancher/k3s/k3s.yaml
NAME: my-release
LAST DEPLOYED: Thu Mar 17 11:50:57 2022
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: kafka
CHART VERSION: 15.4.1
APP VERSION: 3.1.0

** Please be patient while the chart is being deployed **

Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:

    my-release-kafka.default.svc.cluster.local

Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your cluster:

    my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092

To create a pod that you can use as a Kafka client run the following commands:

    kubectl run my-release-kafka-client --restart='Never' --image docker.io/bitnami/kafka:3.1.0-debian-10-r46 --namespace default --command -- sleep infinity
    kubectl exec --tty -i my-release-kafka-client --namespace default -- bash

    PRODUCER:
        kafka-console-producer.sh \
            
            --broker-list my-release-kafka-0.my-release-kafka-headless.default.svc.cluster.local:9092 \
            --topic test

    CONSUMER:
        kafka-console-consumer.sh \
            
            --bootstrap-server my-release-kafka.default.svc.cluster.local:9092 \
            --topic test \
            --from-beginning
