import uvicorn

def main():
    uvicorn.run("app:create_app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
