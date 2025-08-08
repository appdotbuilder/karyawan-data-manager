from sqlmodel import SQLModel, Field
from datetime import date, datetime
from typing import Optional
from decimal import Decimal


# Persistent models (stored in database)
class Employee(SQLModel, table=True):
    """Employee model with complete information for employee management system."""

    __tablename__ = "employees"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: str = Field(unique=True, max_length=50, description="Unique employee identifier")
    full_name: str = Field(max_length=255, description="Employee's full name")
    department: str = Field(max_length=100, description="Employee's department")
    position: str = Field(max_length=100, description="Employee's job position")
    email: str = Field(
        max_length=255,
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        description="Employee's email address",
    )
    phone_number: str = Field(max_length=20, description="Employee's phone number")
    join_date: date = Field(description="Date when employee joined the company")
    salary: Decimal = Field(decimal_places=2, max_digits=12, description="Employee's salary")
    is_active: bool = Field(default=True, description="Whether employee is currently active")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Record creation timestamp")
    updated_at: Optional[datetime] = Field(default=None, description="Record last update timestamp")


# Non-persistent schemas (for validation, forms, API requests/responses)
class EmployeeCreate(SQLModel, table=False):
    """Schema for creating a new employee."""

    employee_id: str = Field(max_length=50, description="Unique employee identifier")
    full_name: str = Field(max_length=255, description="Employee's full name")
    department: str = Field(max_length=100, description="Employee's department")
    position: str = Field(max_length=100, description="Employee's job position")
    email: str = Field(
        max_length=255,
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        description="Employee's email address",
    )
    phone_number: str = Field(max_length=20, description="Employee's phone number")
    join_date: date = Field(description="Date when employee joined the company")
    salary: Decimal = Field(decimal_places=2, max_digits=12, description="Employee's salary")


class EmployeeUpdate(SQLModel, table=False):
    """Schema for updating existing employee information."""

    full_name: Optional[str] = Field(default=None, max_length=255, description="Employee's full name")
    department: Optional[str] = Field(default=None, max_length=100, description="Employee's department")
    position: Optional[str] = Field(default=None, max_length=100, description="Employee's job position")
    email: Optional[str] = Field(
        default=None,
        max_length=255,
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        description="Employee's email address",
    )
    phone_number: Optional[str] = Field(default=None, max_length=20, description="Employee's phone number")
    join_date: Optional[date] = Field(default=None, description="Date when employee joined the company")
    salary: Optional[Decimal] = Field(default=None, decimal_places=2, max_digits=12, description="Employee's salary")
    is_active: Optional[bool] = Field(default=None, description="Whether employee is currently active")


class EmployeeResponse(SQLModel, table=False):
    """Schema for employee API responses."""

    id: int
    employee_id: str
    full_name: str
    department: str
    position: str
    email: str
    phone_number: str
    join_date: date
    salary: Decimal
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]


class EmployeeSearch(SQLModel, table=False):
    """Schema for employee search parameters."""

    name: Optional[str] = Field(default=None, description="Search by name (partial match)")
    department: Optional[str] = Field(default=None, description="Filter by department")
    position: Optional[str] = Field(default=None, description="Filter by position")
    is_active: Optional[bool] = Field(default=None, description="Filter by active status")
    min_salary: Optional[Decimal] = Field(default=None, description="Minimum salary filter")
    max_salary: Optional[Decimal] = Field(default=None, description="Maximum salary filter")
