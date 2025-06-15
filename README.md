# sbom-mcp
mcp for generating to sbom.

## 사용 방법(using the command line)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


## 실행(Excute)
uvicorn app.main:app --reload
