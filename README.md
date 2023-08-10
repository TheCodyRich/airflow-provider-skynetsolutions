# airflow-provider-skynetsolutions
Provides an Airflow Operator to call ChatGPT via OpenAI's API.

## Requirements

* Airflow >=2.2
* OpenAI >= 0.27.4
* OpenAI API Token

## Initial Setup

copy the source code and dump it in your includes as a custom operator.


## Examples

A simplified example DAG demonstrates how to use the [ChatGPT Operator](/example_dags/chatgpt_example_dag.py)

To use, you simply need to insert your own `api_key`.
