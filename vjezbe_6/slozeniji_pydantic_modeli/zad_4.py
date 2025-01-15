from pydantic import BaseModel

class CCTV_frame(BaseModel):
    id: int
    timestamp: str
    koordinate: tuple[float, float] = (0.0, 0.0)

frame = CCTV_frame(id=1, timestamp="1993-04-03 12:00:00")
print(frame)

frame2 = CCTV_frame(id=2, timestamp="1993-04-03 12:00:00", koordinate=(56.0, 43.0))
print(frame2)