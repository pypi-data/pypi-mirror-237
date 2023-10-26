# coding: utf-8
import argparse
import logging
import os
import uuid
from ddba.app import app
import openai

logger = logging.getLogger(__name__)


def cli():
    parser = argparse.ArgumentParser(description='Digital DBA')

    parser.add_argument('--api_key', action="store", required=True, type=str)

    args = parser.parse_args()

    if not args.api_key or len(args.api_key) == 0:
        raise Exception("Please provide an API key")

    openai.api_key = args.api_key
    app.run("0.0.0.0", "8081")
    return app
