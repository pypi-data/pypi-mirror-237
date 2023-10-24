# RabbitMQ Toolkit

RabbitMQ Toolkit is a comprehensive package designed to simplify RabbitMQ operations. It encapsulates the core functionalities into three intuitive classes: `QueueManager`, `Producer`, and `Consumer`, streamlining the process of message queueing, producing, and consuming.

## Installation

Install the package via pip:

```bash
pip install rabbitmq_toolkit
```


## Features

- **QueueManager**: Effortlessly manage your RabbitMQ queues.
- **Producer**: Produce messages with ease, ensuring they're properly queued.
- **Consumer**: Robustly consume messages, with built-in mechanisms to handle common scenarios.

## Usage Example

### Producer

In `producer.py`:

```python
from rabbitmq_toolkit import QueueManager, Producer

# Initialize the Queue Manager and declare a queue
queue_mgr = QueueManager()
queue_name = "sample_queue"
queue_mgr.declare_queue(queue_name)

# Produce a message
producer = Producer(queue_mgr)
producer.send_message(queue_name, "Hello from RabbitMQ Toolkit!")
```

Run `producer.py` in terminal:
```bash
python producer.py
```

### Consumer

In `consumer.py`:

```python
from rabbitmq_toolkit import QueueManager, Consumer

# Initialize the Queue Manager
queue_mgr = QueueManager()
queue_name = "sample_queue"
# We use declare_queue for both can operate independently and can be started in any order.
queue_mgr.declare_queue(queue_name)

# Consume the message
def callback(message):
    print(f"Received: {message}")

consumer = Consumer(queue_mgr)
consumer.start_consuming(queue_name, callback)
```

Run `consumer.py` in other tab terminal:
```bash
python consumer.py
```

**Note:** This provides a clear distinction between the Producer and Consumer, showcasing how they can be used in separate files.