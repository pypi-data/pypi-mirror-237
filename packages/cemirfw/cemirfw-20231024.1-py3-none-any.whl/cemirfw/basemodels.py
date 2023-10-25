from commands.create_sqltable import cfwIPAddress, cfwNow, cfwDateTime, cfwDecimal, create_sqltable
from func_builtin_class import BaseModel

class PostInvoicesData(BaseModel):
    invoices_id: int
    afloat: float
    astr: str
    project_date: cfwNow
    content: dict
    ip_address: cfwIPAddress = "192.168.1.1"


class Users(BaseModel):
    user_id: int
    name: str = "muslu"
    email: str
    phone: str
    age: int
    balance: float
    is_active: bool
    registration_date: cfwDateTime
    address: dict
    tags: list
    profile_image: bytes
    point: cfwDecimal
    ip_address: cfwIPAddress = "192.168.1.2"


async def main():
    dsn = "dbname=maindb user=postgres password=dD5Yz6xE5m host=admin.makdos.com port=5435"
    result1 = await create_sqltable(PostInvoicesData, dsn=dsn, create=True)
    print(result1)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
