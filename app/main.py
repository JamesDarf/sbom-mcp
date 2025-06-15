# main.py
from fastapi import FastAPI, UploadFile
from app.sbom import generate_test_sbom, analyze_log4j

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "MCP SBOM Server Running"}

@app.post("/generate_sbom")
async def generate_sbom(file: UploadFile):
    # 지금은 파일 파싱 생략: 테스트용 샘플 SBOM 생성
    sbom_json = generate_test_sbom()
    return sbom_json

@app.post("/analyze_vuln")
async def analyze_vuln():
    sbom_json = generate_test_sbom()
    report = analyze_log4j(sbom_json)
    return report
