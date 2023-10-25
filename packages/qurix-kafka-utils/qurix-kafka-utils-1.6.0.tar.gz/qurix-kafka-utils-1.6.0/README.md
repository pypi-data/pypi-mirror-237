# KafkaUtils

# What is it?

Qurix kafka utils is a Python package that provides a class for reading the unknown messages from topic.It also provides various functions to get important topic metrics like offset. Finally, it provides a tool to anonymize dataframes.

# Main Features

Key features of the package include:

- consuming the messages using confluent kafka platform
- can set specific offset options like Earliest, Latest, Last and Exlipicit to consume messages
- Logging: The package sets up logging using the Python `logging` module to facilitate monitoring and error handling during execution.
- Observer: the kafka observer allows to get important topic metrics such as offset
- Anonymization: Dataframes can be anonymized before, after reading

# Requirements

`confluent-kafka`

You can install these dependencies manually or use the provided requirements.txt file in repository.


# Installation

## Create a new virtual environment
`python -m virtualenv .venv --python="python3.11"`

## Activate
source .venv/bin/activate

## Install
To install the `qurix-kafka-utils` package, you can use `pip`:

`pip install qurix-kafka-utils`

# Usage

## Generic Consumer

Import the `GenericConsumer` class from the package:
as mentioned in the example 

## Example to use Consumer

```
from qurix.kafka.utils.generic_consumer import GenericConsumer
from qurix.kafka.utils.offset_enum import Offset
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka-Bootstrap-Server
    'group.id': 'my_consumer_group',  # Verbrauchergruppe
    'auto.offset.reset': 'earliest'  # Offset-Einstellung für neue Verbraucher
}


consumer = GenericConsumer(topic="my_topic", consumer_config=conf)

#To consume messages from topic
consumer.read_messages()

#To consume messages from specific offset (E.g "Earliest")
consumer.set_offset(partition=0 , offset_option=Offset.EARLIEST)

#To consume messages with explicit number by giving to  variable offset_value
consumer.set_offset(partition=0 , offset_option=Offset.EXPLICIT , offset_value = 20)
consumer.read_messages()
#To consume messages with timestamp by giving to  variable offset_value
consumer.set_offset(partition=0 , offset_option=Offset.TIMESTAMP , timestamp_dt=datetime_timestamp)
#To extend the df with header 
consumer.extend_df_with_header(df= your_df_from_read_messages)
#To extract value 
consumer.extract_json(df , 'column_name')
```

## Kafka Observer

Import the `KafkaObserver` class from the package

## Example to use Kafka Observer

```
from qurix.kafka.utils.kafka_observer import KafkaObserver

conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka-Bootstrap-Server
}

observer = KafkaObserver(conf)

#To get consumer groups
observer.get_consumer_groups()
#To get the offset of the consumer group
observer.get_consumer_group_offset(group_id="my_group_id")
#To get consumer groups with offsets
observer.get_consumer_groups_with_offsets()
#To get offset status
observer.get_offset_status(consumer = my_consumer, topic = "my_topic"), auto_offset = "earliest")
#To plot offset
observer.plot_offset_status(consumer = my_consumer)
```

## Anonymization

Import the `Anonymizer` class from the package.

`Anonymizer` takes a value argument which allows to specify the content of object columns. It is None by default. It taks a dictionary conisisting out of the index of the column and the value to replace the content with. Valid arguments are gender, name, address

## Example to use Anonymizer

```
import pandas as pd
from qurix.kafka.utils.anonymizer import Anonymizer

df = pd.read_csv("my_csv_file.csv")

#Without value argument
anonymizer = Anonymizer(df)
df_anonymized = anonymizer.anonymize_dataframe()
df_anonymized.head()
#With value argument
anonymizer = Anonymizer(df, {3: 'gender', 5: 'name'})
df_anonymized = anonymizer.anonymize_dataframe()
df_anonymized.head()
```

# Contact
For any inquiries or questions, feel free to reach out
