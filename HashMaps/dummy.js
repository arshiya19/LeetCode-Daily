async def disconnect(self, close_code):
await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
    )
    logger.info(f"User {self.user} disconnected from game {self.game_id}")
