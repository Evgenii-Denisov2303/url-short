from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/short_url")
async def generate_short_url(
        long_url: str = Body(embed=True),
):
    return {"data": "1"}


@app.post("/slug")
async def redirect_to_url(slug: str):
    return ...