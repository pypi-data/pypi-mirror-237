# Metaflow-Ray

### Introduction
`metaflow-ray` is an extension for Metaflow that enables seamless integration with Ray, allowing users to easily leverage 
Ray's powerful distributed computing capabilities within their Metaflow flows. 
With `metaflow-ray`, you can spin up transient Ray clusters on AWS Batch directly from your Metaflow steps using 
the `@metaflow_ray` decorator. This enables you to run your Ray applications that leverage Ray Core, Ray Train, Ray Tune, 
and Ray Data effortlessly within your Metaflow flow.

### Features
- <b>Effortless Ray Integration:</b> This extension provides a simple and intuitive way to incorporate Ray 
into your Metaflow workflows using the `@metaflow_ray` decorator
- <b>Transient Ray Clusters:</b> Let Metaflow orchestrate the creation of transient Ray clusters on top of AWS Batch multi-node parallel jobs
- <b>Seamless Ray Initialization:</b> The `@metaflow_ray` decorator handles the initialization of the Ray cluster for you, so you just need to 
focus on writing your Ray code without worrying about cluster setup
- <b>Wide Range of Applications:</b> Run a wide variety of Ray applications, including hyperparameter tuning, distributed data processing, and
distributed training

### Installation
You can install `metaflow-ray` via `pip` alongside your existing Metaflow installation:
```
pip install metaflow-ray
```

### Getting Started
1. Import the `@metaflow_ray` decorator to enable integration:
```python
from metaflow import metaflow_ray
```

2. Decorate your step with `@metaflow_ray`
```python
@step
def start(self):
    self.next(self.train, num_parallel=NUM_NODES)

@metaflow_ray
@batch(**RESOURCES)
@step
def train(self):
    # Your step's training code here
```

3. Initialize Ray within Your Step
```python
@metaflow_ray
@batch(**RESOURCES)
@step
def train(self):
    import ray
    ray.init()
    # Your ray application code here
```

### Examples
Check out the [examples](/examples) directory for sample Metaflow flows that demonstrate how to use the `metaflow-ray`extension 
with various Ray applications.

### License
`metaflow-ray` is distributed under the <u>Apache License</u>.