# Distributed Runner
This library allows for the easy construction and management of ephemeral Dask clusters on AWS via a simple context manager. This allows you to perform distributed and parallelized computations with ease.

![license](https://img.shields.io/gitlab/license/crossref/labs/distrunner) ![activity](https://img.shields.io/gitlab/last-commit/crossref/labs/distrunner) <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

![Dask](https://img.shields.io/badge/dask-%23092E20.svg?style=for-the-badge&logo=dask&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitLab](https://img.shields.io/badge/gitlab-%23121011.svg?style=for-the-badge&logo=gitlab&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Installation

    pip install distrunner

## Usage

In your scheduler (Airfow etc.) use something like this:

    from distrunner import DistRunner
    import whatismyip

    def main():
        with DistRunner(workers=10) as cldr:
            results = cldr.client.map(print_ip, range(10))
            outcome = cldr.client.gather(results)
    
            print(outcome)

    def print_ip(x):
        return f"My IP address is {whatismyip.whatismyip()}"

The "local" flag will determine whether a remote cluster is created. For example, the following will all run locally instead of spinning up infrastructure:

    from distrunner import DistRunner
    import whatismyip

    def main():
        with DistRunner(workers=10, local=True) as cldr:
            results = cldr.client.map(print_ip, range(10))
            outcome = cldr.client.gather(results)
    
            print(outcome)

    def print_ip(x):
        return f"My IP address is {whatismyip.whatismyip()}"

You will need to set the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables to use the Fargate clusters (or run from an environment with an authorised IAM role).

## Running in Managed Workflows for Apache Airflow (MWAA)
Running inside an AWS MWAA environment requires a _little_ more setup than running locally. This is because of the way that requirements are handled in Airflow. You also need to ensure that any called functions are nested underneath the task in question. The above examples, refactored for Airflow, could read:

    REQUIREMENTS = [
        "distrunner>=1.3.0",
        "whatismyip,
        "coiled",
        "dask[complete]",
    ]

    @dag(
        default_args=DEFAULT_ARGS,
        schedule_interval="@daily",
        catchup=False,
        dagrun_timeout=timedelta(hours=16),
        start_date=datetime(2023, 4, 16),
        tags=["api"],
    )
    def main_task():
        @task.virtualenv(
            task_id="main_task",
            requirements=REQUIREMENTS,
            system_site_packages=True,
        )
        def entry_point(requirements):
            
            def print_ip(x):
                return f"My IP address is {whatismyip.whatismyip()}"

            from distrunner.distrunner import DistRunner

            with DistRunner(
                workers=1,
                requirements=requirements,
                application_name="test_application",
            ) as cldr:
                results = cldr.client.map(snapshot_routes_body, range(1))
                cldr.client.gather(results)
    
        entry_point(REQUIREMENTS)

    main_task()


## Features
* Context manager handling of Dask Fargate clusters with scale-to-zero on complete
* Easy ability to switch between local and distributed/remote development

## What it Does
This library allows you to easily run functions across a Dask cluster.

## Credits

* [AWS/Boto](https://github.com/boto/botocore)
* [Coiled](https://coiled.io)
* [Dask](https://www.dask.org/)
* [Git](https://git-scm.com/)
* [GitPython](https://github.com/gitpython-developers/GitPython)

Copyright &copy; Crossref 2023 