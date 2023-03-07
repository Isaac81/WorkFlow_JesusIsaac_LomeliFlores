from time import sleep
import random
from prefect import flow, task


@task
def create_process():
    process  =  {
        "num1": random.randint(0, 100),
        "num2": random.randint(0, 100),
        "tme": random.randint(1, 5)
    }

    return process


@task
def execute(process):
    result = process['num1'] / process['num2']
    sleep(process['tme'])

    return result


@flow
def main_flow():
    p = create_process()
    result = execute(p)
    print(f"Process completed in {p['tme']} seconds. Result: {result}")


if __name__ == "__main__":
    main_flow()