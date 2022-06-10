import asyncio
import websockets
from json import loads, dumps
from typing import Awaitable
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
from logging import info, debug

from ..utils import Repr
from ..config.config import apiUrl, heartbeatInterval
from ..exceptions.exceptions import NoConnectionException

class HideoutClient(Repr):
    def __init__(self, token: str, refresh_token: str):
        self.__token = token
        self.__refresh_token = refresh_token
        self.__socket = None
        self.__active = False
        self.__eventHandlers = []

    async def __main(self):
        """This instance handles the websocket connections."""
        try:
            debug("Connecting with hideout API")
            async with websockets.connect(apiUrl) as ws:
                debug("hideout API connection established successfully")
                self.__active = True 
                self.__socket = ws
                # print(loads(await ws.recv()))

                # while self.__active:
                #     for handler in self.__eventHandlers:
                #         await handler(loads(await ws.recv()))
        except ConnectionClosedOK:
            debug("Hideout API connection closed peacefully.")
            self.__active = False
        # except ConnectionClosedError:


    def run(self):
        """Establishes a connection to the websocket servers."""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__main())
        loop.close()

    async def close(self):
        """
        Closes the established connection.
        Raises:
            NoConnectionException: No connection has been established yet. Aka got nothing to close.
        """
        if not isinstance(self.__socket, websockets.WebSocketClientProtocol):
            raise NoConnectionException()

        self.__active = False