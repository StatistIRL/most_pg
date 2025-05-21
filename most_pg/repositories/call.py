from sqlalchemy import delete, select, update
from .base import BaseRepository
from ..models.calls import Call
from .. import _types as types

class CallRepository(BaseRepository):            
    async def add_call(self, call: types.Call, flush: bool = False):
        call = Call(**call.to_dict())
        
        self._session.add(call)
        
        if flush:
            await self._session.flush()
        
        return call
    
    async def get_call_by_most_id(self, most_id: str) -> Call | None:
        stmt = select(Call).where(Call.most_id == most_id)
        result = await self._session.execute(stmt)
        call = result.scalar_one_or_none()
        return call
    
    async def update_call(self, most_id: str, data: types.CallUpdateDict, flush: bool = False) -> Call | None:
        stmt = (
            update(Call)
            .where(Call.most_id == most_id)
            .values(**data)
            .returning(Call)
        )
        result = await self._session.execute(stmt)
        call = result.scalar_one_or_none()

        if call and flush:
            await self._session.flush()

        return call

    async def delete_call(self, most_id: str, flush: bool = False) -> bool:
        stmt = delete(Call).where(Call.id == most_id)
        result = await self._session.execute(stmt)
        
        if result.rowcount and flush:
            await self._session.flush()

        return result.rowcount > 0