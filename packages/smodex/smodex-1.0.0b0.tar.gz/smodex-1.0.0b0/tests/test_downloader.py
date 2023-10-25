import os
from unittest.mock import Mock
from unittest.mock import patch

import cdsapi
import pytest
from smodex.sm_downloader import downloader
from smodex.sm_downloader import era5_sm_downloader


@pytest.fixture
def mock_cdsapi_client():
    # Create a mock object for the cdsapi.Client class
    mock_client = Mock(spec=cdsapi.Client())
    return mock_client


@pytest.mark.skip(reason="cdsapi api retrieve method not called correctly")
@patch("cdsapi.Client")
def test_era5_sm_downloader(mock_cdsapi_client, tmp_path):
    year = "2023"
    download_path = str(tmp_path)
    depth = [1, 2]
    area = [50.775, 2.775, 42.275, 18.025]

    # Set up the mock CDS API client
    mock_cdsapi_client.retrieve.return_value = None

    # Call the function to be tested
    era5_sm_downloader(year, download_path, depth, area)

    # Check if the CDS API client's retrieve method was called with the expected arguments
    mock_cdsapi_client.retrieve.assert_called_once_with(
        "reanalysis-era5-single-levels",
        {
            "product_type": "reanalysis",
            "variable": ["volumetric_soil_water_layer_1", "volumetric_soil_water_layer_2"],
            "year": year,
            "month": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
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
            "time": ["00:00", "06:00", "12:00", "18:00"],
            "area": area,
            "format": "netcdf",
        },
        download_path + f"ERA5_SM_{year}.nc",
    )


def test_downloader(tmp_path, monkeypatch, caplog):
    # test data
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    download_path = str(tmp_path)
    api = "era5"
    depth = [1, 2]
    area = [50.775, 2.775, 42.275, 18.025]

    # Monkeypatch the os.makedirs function to avoid creating directories during testing
    monkeypatch.setattr(os, "makedirs", lambda path: None)

    downloader(start_date, end_date, download_path, api, depth, area)

    assert "Initiating downloading of ERA5 Soil Moisture for 2023" in caplog.text
    assert "Downloaded ERA5 Soil Moisture for 2023" in caplog.text


if __name__ == "__main__":
    pytest.main()
