# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""
This file defines the util functions related to model export
"""
import os
import shutil

from .logging_utils import get_logger_app

logger = get_logger_app(__name__)


def extract_best_pytorch_model(job_output_dir: str, best_pytorch_model_folder: str) -> None:
    """Save the best model checkpoint to pytorch model folder
    :param job_output_dir: job's output directory
    :type job_output_dir: str
    :param best_pytorch_model_folder: pytorch model folder
    :type best_pytorch_model_folder: str
    :return: None
    :rtype: None
    """
    os.makedirs(best_pytorch_model_folder, exist_ok=True)

    for filename in os.listdir(job_output_dir):
        file_path = os.path.join(job_output_dir, filename)
        if os.path.isfile(file_path) and (not filename.endswith(".log")) and (not filename.endswith(".csv")):
            shutil.copy2(file_path, best_pytorch_model_folder)
    logger.info("Pytorch model saved successfully.")
