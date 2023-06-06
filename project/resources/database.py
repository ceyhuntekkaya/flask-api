#!/usr/bin/python
# -*- coding: utf-8 -*-


async def async_fetch(app, sql, *args, fetch_one=False, return_type="dict"):
    """

    :param app: Request app.
    :param sql: SQL string to fetch.
    :param args: SQL parameters for prepared statements.
    :param fetch_one: If True fetch one, limit 1.
    :param return_type: Return result type as dict, tuple or asyncpg record.
    :return: Database fetch result.

    """

    # Take a connection from the pool.
    async with app["pool"].acquire() as connection:
        # Open a transaction.
        async with connection.transaction():
            # Run the query passing the request argument.
            stmt = await connection.prepare(sql)

            # Prepared statement execute.
            result = (
                await stmt.fetchrow(*args) if fetch_one else await stmt.fetch(*args)
            )

            # If database result is none return.
            if not result:
                return None

            # Convert items to dict.
            if return_type == "dict":
                # {"column1": "value1", "column2": "value2", ... }
                if fetch_one:
                    return dict(result)

                # [{"column1": "value1", "column2": "value2", ... }]
                return [dict(row) for row in result]

            # Convert items to tuple.
            elif return_type == "tuple":
                if fetch_one:
                    # (column1, 'column2', ...)
                    return tuple(result)

                # [(column1, 'column2', ...)]
                return [tuple(row) for row in result]

            # Asyncpg record objects.
            else:
                return result


async def async_execute(app, sql, *args):
    """

    :param app: Request app.
    :param sql: SQL string to fetch.
    :param args: SQL parameters for prepared statements.

    """

    # Take a connection from the pool.
    async with app["pool"].acquire() as connection:
        # Open a transaction.
        async with connection.transaction():
            # Run the query passing the request argument.
            await connection.execute(sql, *args)


async def orm_session_add(app, obj):
    """

    :param app: Request app.
    :param obj: Object to insert.

    """

    # Add to session and insert.
    async with app["session"]() as session:
        async with session.begin():
            if isinstance(obj, list):
                session.add_all(obj)
            else:
                session.add_all([obj])


async def orm_execute(app, query):
    """

    :param app: Request app.
    :param query: Query to execute.

    """

    async with app["session"]() as session:
        async with session.begin():
            await session.execute(query)


async def orm_fetch(app, query, fetch_one=False, return_type="dict"):
    """

    :param app: Request app.
    :param query: Object to select.
    :param fetch_one: Result to fetch one.
    :param return_type: Return type for result.
    :return: Database fetch result.

    """

    # Get object/objects.
    async with app["session"]() as session:
        async with session.begin():

            # Execute query.
            result = await session.execute(query)

            # Filter fetch one.
            if not fetch_one:
                values = result.fetchall()
            else:
                values = result.fetchone()

            # Return none if database result is none.
            if not values:
                return None

            # Convert result items to dict.
            if return_type == "dict":
                # {"column1": "value1", "column2": "value2", ... }
                if fetch_one:
                    val = values[0]
                    return await val.as_dict()

                # [(< app.database.models.Anomaly object at 0x109198bb0 >,)]
                return [await row[0].as_dict() for row in values]

            # JSON.
            elif return_type == "json":
                return values[0]

            # Asyncpg record objects.
            else:
                if fetch_one:
                    return values[0]
                else:
                    return [row[0] for row in values]
