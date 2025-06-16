from fastapi import FastAPI, UploadFile
from app.sbom import generate_test_sbom, analyze_log4j

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MCP SBOM Server Running (CycloneDX 최신버전)"}

@app.post("/generate_sbom")
async def generate_sbom(file: UploadFile = None):
    sbom_json = generate_test_sbom()
    return sbom_json

@app.post("/analyze_vuln")
async def analyze_vuln():
    sbom_json = generate_test_sbom()
    report = analyze_log4j(sbom_json)
    return report
