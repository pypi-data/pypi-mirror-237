"""
    Soil Moisture Downloader: Configured to download datasets from the Climate Data Store
    Downloads hourly soil moisture datasets for full year
"""
import argparse
import json
import logging
import os
import sys

import numpy as np
import pandas as pd

import cdsapi


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


c = cdsapi.Client()


def era5_sm_downloader(year: str, download_path: str, depth: list, area: list) -> None:
    """downloader from ERA5 API"""

    variables = []
    for dep in depth:
        variables.append(f"volumetric_soil_water_layer_{dep}")

    c.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "variable": variables,
            "year": int(year),
            "month": [
                "01",
                "02",
                "03",
                "04",
                "05",
                "06",
                "07",
                "08",
                "09",
                "10",
                "11",
                "12",
            ],
            "day": [
                "01",
                "02",
                "03",
                "04",
                "05",
                "06",
                "07",
                "08",
                "09",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
                "31",
            ],
            "time": [
                "00:00",
                "06:00",
                "12:00",
                "18:00",
            ],
            "area": area,
            "format": "netcdf",
        },
        download_path + f"ERA5_SM_{year}.nc",
    )


def downloader(
    start_date: str, end_date: str, download_path: str, api: str, depth: list, area: list
) -> None:
    """download"""

    date_ranges = pd.date_range(start=start_date, end=end_date)
    date_ranges = [date.year for date in date_ranges]
    years = np.unique(date_ranges)

    for yr in years:
        if api == "era5":
            logger.info(f"Initiating downloading of ERA5 Soil Moisture for {yr}")
            if not os.path.exists(download_path):
                os.makedirs(download_path)
            era5_sm_downloader(yr, download_path, depth, area)
            logger.info(f"Downloaded ERA5 Soil Moisture for {yr}")


if __name__ == "__main__":
    # command line option
    parser = argparse.ArgumentParser(
        description="Downloads soil moisture \
                                     datasets from start date to end date"
    )
    parser.add_argument(
        "start_date",
        type=str,
        help="initial date to start \
                                     downloading from e.g. 1990-01-01",
    )
    parser.add_argument(
        "end_date",
        type=str,
        help="end date to stop \
                                     downloading datasets from e.g. 2030-12-31",
    )
    parser.add_argument("api", type=str, help="download portal API e.g. era5, lpdaac, etc.")
    parser.add_argument(
        "-a",
        "--area",
        type=json.loads,
        help="bounding box area for downloading \
                         datasets e.g. [50.775, 2.775, 42.275, 18.025]",
    )
    parser.add_argument(
        "-d",
        "--depth",
        type=json.loads,
        help="volumetric \
                        soil moisture depths e.g. [1, 2, 3, 4]",
    )
    parser.add_argument(
        "path",
        type=str,
        help="directory to save the \
                        downloaded datasets e.g. /sm_downloaded/",
    )

    args = parser.parse_args()

    downloader(args.start_date, args.end_date, args.path, args.api, args.depth, args.area)
