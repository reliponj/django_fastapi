import uvicorn as uvicorn

if __name__ == '__main__':
	uvicorn.run("django_fastapi.app:fastapp", port=8000, host='0.0.0.0', reload=True)
