from datetime import date
from pydantic import BaseModel, Field, field_validator, model_validator, ValidationInfo


class Course(BaseModel):
    id: int | None = None
    name: str
    start_date: date
    end_date: date
    cut1_percentage: float = Field(..., ge=0, le=100)
    cut2_percentage: float = Field(..., ge=0, le=100)
    cut3_percentage: float = Field(..., ge=0, le=100)

    @field_validator('end_date')
    def end_date_after_start_date(cls, end_date: date, info: ValidationInfo):
        start_date = info.data.get('start_date')

        if start_date and end_date <= start_date:
            raise ValueError('End date must be after start date')
        return end_date

    @model_validator(mode='after')
    def check_total_percentage(cls, course: 'Course'):
        total = course.cut1_percentage + course.cut2_percentage + course.cut3_percentage
        if total != 100:
            raise ValueError('The sum of cut1 percentage, cut2 percentage, and cut3 percentage must be 100. V2')
        return course