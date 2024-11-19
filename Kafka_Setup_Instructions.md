
# Kafka Setup Instructions with Configuration Changes

## 1. Download Kafka
Download Kafka from [https://kafka.apache.org/downloads](https://kafka.apache.org/downloads) and choose **Binary downloads: Scala 2.13**.

## 2. Extract and Move Kafka
Extract the file `kafka_2.13-3.8.1.tgz`, move the extracted folder to the **C:** directory, and rename the folder to **kafka**.

## 3. Update Configuration Files
Navigate to the **C:\kafka\config** directory, and make the following changes:

- In **`zookeeper.properties`**, change the `dataDir` setting to:
  ```
  dataDir=C:/kafka/zookeeper-data
  ```

- In **`server.properties`**, change the `log.dirs` setting to:
  ```
  log.dirs=C:/kafka/kafka-logs
  ```

## 4. Start Zookeeper
Open a command prompt, navigate to the Kafka directory, and start the Zookeeper server:
```bash
C:\kafka> .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```

## 5. Start Kafka Server
In a new command prompt window, navigate to the Kafka directory, and start the Kafka server:
```bash
C:\kafka> .\bin\windows\kafka-server-start.bat .\config\server.properties
```

## 6. Create a Kafka Topic
In a new command prompt window, create a topic named `test`:
```bash
C:\kafka\bin\windows> kafka-topics.bat --create --bootstrap-server localhost:9092 --topic test
```

## 7. Start Kafka Producer
In another command prompt, start a Kafka producer to send messages to the `test` topic:
```bash
C:\kafka\bin\windows> kafka-console-producer.bat --broker-list localhost:9092 --topic test
```

## 8. Start Kafka Consumer
In another command prompt, start a Kafka consumer to read messages from the `test` topic:
```bash
C:\kafka\bin\windows> kafka-console-consumer.bat --topic test --bootstrap-server localhost:9092 --from-beginning
```

These steps should start Zookeeper and Kafka, create a topic, and allow you to produce and consume messages on the `test` topic.
