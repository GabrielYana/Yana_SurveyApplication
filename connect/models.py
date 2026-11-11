from sqlmodel import Field , SQLModel

class ApplicantSchool(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    Username: str
    Password: str
    Fullname: str
    Idnumber: int
    Course: str
    Yearlevel:  int
    School: str
    Nationality: str
    Religion: str
    Age:  int
    Location: str


