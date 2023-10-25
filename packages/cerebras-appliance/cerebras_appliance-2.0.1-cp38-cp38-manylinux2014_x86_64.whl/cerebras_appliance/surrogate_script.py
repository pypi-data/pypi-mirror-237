#!/usr/bin/env python3
"""
A script to run in the external scheduler to serve as a surrogate job for
the appliance job. It waits for a signal from the appliance or the external
scheduler to terminate the process. If an exception is raise, it queries
the appliance to find the status for the appliance job, and exit based on
that status:
    SUCCEEDED: exit with 0.
    FAILED or CANCELLED: exit with 1.
    others: send a cancel job to the appliance to cancel the job and exit with 1.
"""

# Copyright 2023 Cerebras Systems, Inc.

import argparse
import json
import logging
import shlex
import signal
import subprocess
import sys
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

_shutdown = False
def _handle_shutdown(signal_no, frame):
    global _shutdown # pylint: disable=global-statement
    _shutdown = True
    raise RuntimeError("Set _shutdown to True")


def _get_appliance_job(job_name):
    try:
        cmd = f'csctl get job {job_name} -ojson'
        output = subprocess.check_output(shlex.split(cmd)).decode('utf-8')
        output_json = json.loads(output)
        return output_json
    except subprocess.CalledProcessError as exp:
        logger.error(f"cmd {cmd} failed; {exp}. Exit 1")
        sys.exit(1)


def _main(args):

    signal.signal(signal.SIGINT, _handle_shutdown)
    signal.signal(signal.SIGTERM, _handle_shutdown)

    job_name = args.job_name
    logger.info(f"Surrogate job for appliance job {job_name} started")
    try:
        while not _shutdown:
            logger.debug("Waiting for shutdown")
            time.sleep(10)
    except RuntimeError:
        output_json = _get_appliance_job(job_name)
        if output_json['status']['phase'] == 'RUNNING':
            # Give the appliance 10 second to terminate the job if any.
            time.sleep(10)

        output_json = _get_appliance_job(job_name)
        if output_json['status']['phase'] == 'SUCCEEDED':
            logger.info(
                f"Appliance job {job_name} {output_json['status']['phase']}. Exit normally")
            sys.exit(0)
        elif output_json['status']['phase'] == 'FAILED' or \
            output_json['status']['phase'] == 'CANCELLED':
            logger.error(
                f"Appliance job {job_name} {output_json['status']['phase']}. Exit with error")
            sys.exit(1)
        else:
            # Cancel the appliance job.
            cancel_cmd = f'csctl cancel job {job_name}'
            logger.info(f"Cancelling {job_name}")
            subprocess.check_output(shlex.split(cancel_cmd))
            sys.exit(1)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--job-name",
        default=None,
        help="Name of the appliance job.",
    )
    _main(parser.parse_args())
