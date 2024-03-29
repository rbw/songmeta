from app.services import TrackService
from app.controller import Controller

from .schemas import TrackPayload, Track, Tracks


class TrackController(Controller):
    def __init__(self):
        self.trk = TrackService(self.app)

    def routes_make(self):
        return "/tracks", [
            ("/", "GET", self.get_many),
            ("/", "POST", self.create),
            ("/{track_id}", "GET", self.get_one),
        ]

    async def get_one(self, req):
        track_id = req.path_params.get("track_id")
        item = await self.trk.get_one(track_id)
        return self.json_response(item, 200, Track)

    async def get_many(self, _):
        items = await self.trk.get_many()
        return self.json_response(items, 200, Tracks)

    async def create(self, req):
        body = await req.body()
        track = self.deserialize(body, TrackPayload)
        await self.trk.create(track)
        return self.json_response(None, 201)

