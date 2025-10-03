from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import Airbnb_Project_dbt_assets
from .project import Airbnb_Project_project
from .schedules import schedules

defs = Definitions(
    assets=[Airbnb_Project_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=Airbnb_Project_project),
    },
)