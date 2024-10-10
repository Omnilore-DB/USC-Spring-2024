from pathlib import Path
from typing import Tuple

from fastapi import FastAPI
from sqlalchemy import Table

from app.api.v1.router import router as v1_router
from app.database import engine, meta


def load_past_tables() -> Tuple[Table]:
    enrollment_24a = Table(
        "Enrollment-24a",
        meta,
        autoload_with=engine,
    )

    enrollment_24b = Table(
        "Enrollment-24b",
        meta,
        autoload_with=engine,
    )

    enrollment_template = Table(
        "Enrollment-TEMPLATE-2022",
        meta,
        autoload_with=engine,
    )

    prototype_membership_db = Table(
        "Prototype-MembershipDB",
        meta,
        autoload_with=engine,
    )

    prototype_membership_db_volunteerism = Table(
        "Prototype-MembershipDB-Volunteerism",
        meta,
        autoload_with=engine,
    )

    test = Table(
        "Test",
        meta,
        autoload_with=engine,
    )

    test_k = Table(
        "Test.k",
        meta,
        autoload_with=engine,
    )


def load_all_models() -> None:
    """Load all models from `app.api.v1`.
    Models must be in app/api/v1/*/models.py to be imported.
    """

    # Converts absolute path of a file ending in `models.py` to an import
    def path_to_import(p):
        return p[p.find("app") :].split(".py")[0].replace("/", ".")

    # Sort to make sure we don't have random circular imports
    model_paths = Path(__file__).parent.glob("api/v1/**/models.py")
    model_paths = list(model_paths)
    model_paths.sort()

    for path in model_paths:
        module_name = path_to_import(str(path).replace("\\", "/"))
        __import__(module_name)

    # load_past_tables()


def get_app() -> FastAPI:
    app = FastAPI(
        title="Omnilore Data Gathering API",
        description="API for gathering data for Omnilore's Membership Database",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    load_all_models()

    app.include_router(v1_router)

    return app
