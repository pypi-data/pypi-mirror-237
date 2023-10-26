<!--
Copyright 2022 Tecton, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->
# Tecton Airflow provider for Apache Airflow

This package contains operators, a sensor and a hook that integrate Tecton into Apache Airflow.

Two basic capabilities are supported:
1) Submitting materialization jobs
2) Waiting for Feature View/Feature Service data to materialize.

`TectonSensor` waits for Feature View/Feature Service data to materialize.
`TectonTriggerOperator` launches a Tecton job.
`TectonJobOperator` launches a Tecton job and waits for its completion.
`TectonFeatureTableTriggerOperator` launches a Tecton Feature Table ingestion job.
`TectonFeatureTableJobOperator` launches a Tecton Feature Table ingestion job and waits for its completion.

# Installation

You can install this package via `pip install airflow-provider-tecton`. Note that this requires `apache-airflow>=2.0`.

# Configuration

This provider uses operators that interface with Tecton's API and requires you set up Airflow Connection for Tecton. Most of the Connection config fields will be left blank. Configure the following fields:

 - `Conn Id`:`tecton_default`
 - `Conn Type`:`Tecton`
 - `Host`:`https://your-tecton-url.tecton.ai`
 - `password`:`your-tecton-api-key`

# Usage

## Configuring a Feature View for manual triggering

A `BatchFeatureView` and a `StreamFeatureView` can be configured for manual triggering only. To do so, set `batch_trigger=BatchTriggerType.MANUAL`. When set to manual, Tecton will not automatically create any batch materialization jobs for the Feature View. As of Tecton 0.6, any FeatureView can be manually triggered, but this is recommended mostly for manual usage.

For a `StreamFeatureView`, only batch materialization job scheduling will be impacted by the `batch_trigger` setting. Streaming materialization job scheduling will still be managed by Tecton.

Here’s an example of a `BatchFeatureView` configured for manual triggering.

```python
from tecton import batch_feature_view, FilteredSource, Aggregation, BatchTriggerType
from fraud.entities import user
from fraud.data_sources.transactions import transactions_batch
from datetime import datetime, timedelta

@batch_feature_view(
    sources=[FilteredSource(transactions_batch)],
    entities=[user],
    mode='spark_sql',
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(column='transaction', function='count', time_window=timedelta(days=1)),
        Aggregation(column='transaction', function='count', time_window=timedelta(days=30)),
        Aggregation(column='transaction', function='count', time_window=timedelta(days=90))
    ],
    online=False,
    offline=True,
    feature_start_time=datetime(2022, 5, 1),
    tags={'release': 'production'},
    owner='matt@tecton.ai',
    description='User transaction totals over a series of time windows, updated daily.',
    batch_trigger=BatchTriggerType.MANUAL # Use manual triggers
)
def user_transaction_counts(transactions):
    return f'''
        SELECT
            user_id,
            1 as transaction,
            timestamp
        FROM
            {transactions}
        '''
```

If a Data Source input to the Feature View has `data_delay` set, then that delay will still be factored in to constructing training data sets but does not impact when the job can be triggered with the materialization API.

## Materialization Job Submission

There are two methods available to submit materialization jobs:
1) [TectonTriggerOperator](./tecton_provider/operators/tecton_trigger_operator.py): This triggers a materialization job for a Feature View. Tecton will retry any failing jobs automatically. Note that completion of this operator only means submission succeeded. To wait for completion, you must combine this with `TectonSensor`.
2) [TectonJobOperator](./tecton_provider/operators/tecton_job_operator.py): This triggers a materialization job for a Feature View with no retries. Additionally, when this operator is terminated, it will make a best effort to clean up the execution of the materialization job. Using this operator allows you to use standard Airflow keyword arguments to configure retry behavior. Additionally, this operator is synchronous, meaning that when the operator has succeeded, the underlying job has succeeded.

Both of these require the following arguments:
1) workspace - the workspace name of the Feature View you intend to materialize
2) feature_view - the name of the Feature View you intend to materialize
3) online - whether the job should materialize to the online store. This requires that your FeatureView also has online materialization enabled.
4) offline - whether the job should materialize to the offline store. This requires that your FeatureView also has offline materialization enabled.

The time interval of the materialization job is configured automatically using Airflow templates. By default, it is from the `data_interval_start` to the `data_interval_end` of your DAG run. These can overridden if necessary.

#### Example Usage

```python
from tecton_provider import TectonJobOperator, TectonTriggerOperator

TectonJobOperator(
    task_id="tecton_job",
    workspace="my_workspace",
    feature_view="my_fv",
    online=False,
    offline=True,
    retries=3,
)


TectonTriggerOperator(
    task_id="trigger_tecton",
    workspace="my_workspace",
    feature_view="my_fv",
    online=True,
    offline=True,
)
``` 

## Waiting For Materialization

### [TectonSensor](./tecton_provider/sensors/tecton_sensor.py)

This enables you to wait for Materialization to complete for both Feature Views and Feature Services. Common uses are for monitoring as well as kicking off a training job after daily materialization completes.


#### Example Usage
```python
from tecton_provider import TectonSensor

TectonSensor(
    task_id="wait_for_fs_online",
    workspace="my_workspace",
    feature_service="my_fs",
    online=True,
    offline=False,
)

TectonSensor(
    task_id="wait_for_fv",
    workspace="my_workspace",
    feature_view="my_fv",
    online=True,
    offline=True,
)
```

# Examples

See [example dags here](./tecton_provider/example_dags).

# Development
## Pre-commit

This repo uses pre-commit. Run `pre-commit install` in the repo root to configure pre-commit hooks. Pre-commit hooks take care of running unit tests as well as linting files.

## Run unit tests manually

Run `python -m pytest tests/` in the repo root.

# License
This is licensed with the Apache 2.0 License.

# Issues
Please submit issues and pull requests in our official repo: https://github.com/tecton-ai/airflow-provider-tecton

Tecton would be happy to hear from you. Please email any feedback nacosta@tecton.ai.
