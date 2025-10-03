from pathlib import Path

from dagster_dbt import DbtProject

Airbnb_Project_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "Airbnb_Project").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
Airbnb_Project_project.prepare_if_dev()