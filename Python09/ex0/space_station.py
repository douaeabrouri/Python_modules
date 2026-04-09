#!/usr/bin/env python3
from pydantic import BaseModel, Field
from typing import Optional
from pydantic import ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


if __name__ == "__main__":
    RESET = "\033[0m"
    YELLOW = "\033[33m"
    RED = "\033[31m"

    station = SpaceStation(
        station_id="ISS001",
        name="Broke Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 15, 10, 30, 0),
        is_operational=True,
        notes="All systems nominal",
    )

    print("Space Station Data Validation")
    print("========================================")
    print(f"{YELLOW}ID{RESET}: {station.station_id}")
    print(f"{YELLOW}Name{RESET}: {station.name}")
    print(f"{YELLOW}Crew{RESET}: {station.crew_size} people")
    print(f"{YELLOW}Power{RESET}: {station.power_level}%")
    print(f"{YELLOW}Oxygen{RESET}: {station.oxygen_level}%")
    print(
        f"{YELLOW}status{RESET}: "
        f"{'Operational' if station.is_operational else 'Offline'}"
    )

    print("\n========================================")
    try:
        bad_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=70,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 15, 10, 30, 0),
            is_operational=True,
            notes="All systems nominal",
        )
        print(bad_station)
    except ValidationError as e:
        print(f"{RED}Expected validation error:{RESET}")
        for error in e.errors():
            print(f"{RED}{error['msg']}{RESET}")
