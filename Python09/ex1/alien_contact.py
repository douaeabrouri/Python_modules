#!/usr/bin/env python3
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import ValidationError

RESET = "\033[0m"
YELLOW = "\033[33m"
RED = "\033[31m"


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_contact_rules(self: "AlienContact") -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError(f"{RED}Contact ID must start with 'AC'.{RESET}")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError(
                f"{RED}Physical contact " f"reports must be verified{RESET}"
            )
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                f"{RED}Telepathic contact requires at least 3 witnesses{RESET}"
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                f"{RED}Strong signals (> 7.0) "
                f"should include received messages{RESET}"
            )
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.fromisoformat("2024-06-21T03:15:00"),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )
    print("Valid contact report:")
    print(f"{YELLOW}ID{RESET}: {contact.contact_id}")
    print(f"{YELLOW}Type{RESET}: {contact.contact_type}")
    print(f"{YELLOW}Location{RESET}: {contact.location}")
    print(f"{YELLOW}Signal{RESET}: {contact.signal_strength}/10")
    print(f"{YELLOW}Duration{RESET}: {contact.duration_minutes} minutes")
    print(f"{YELLOW}Witnesses:{RESET}: {contact.witness_count}")
    print(f"{YELLOW}Message{RESET}: '{contact.message_received}'")
    print("\n======================================")
    try:
        AlienContact(
            contact_id="AC_BAD_001",
            timestamp=datetime(2024, 6, 21, 3, 15, 0),
            location="Dark Side of the Moon",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
        )
    except ValidationError as e:
        print(f"{RED}Expected validation error:{RESET}")
        for error in e.errors():
            msg = error["msg"].removeprefix("Value error, ")
            print(f"{RED}{msg}{RESET}")
