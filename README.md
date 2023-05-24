# airflow-provider-thecodyrich
Providers an Airflow Operator to call ChatGPT via OpenAI's API.

## Requirements

* Airflow >=2.2
* OpenAI >= 0.27.4
* OpenAI API Token

## Initial Setup

Install the package.

```
pip install airflow-provider-thecodyrich
```


## Operators

The [`chatgpt_operator`](/airflow-provider-thecodyrich/operators/chatgpt_operator.py)
 runs ChatGPT queries via OpenAI's API.

## Examples

A simplified example DAG demonstrates how to use the [ChatGPT Operator](/example_dags/chatgpt_example_dag.py)

To use, you simply need to insert your own `api_key`.