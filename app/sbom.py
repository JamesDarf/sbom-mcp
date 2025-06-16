import json
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.output import OutputFormat, get_writer

# 테스트용 샘플 SBOM 생성
def generate_test_sbom():
    bom = Bom()

    component = Component(
        name='log4j-core',
        version='2.14.0',
        type=ComponentType.LIBRARY,
        purl='pkg:maven/org.apache.logging.log4j/log4j-core@2.14.0'
    )

    bom.components.add(component)

    writer = get_writer(OutputFormat.JSON, bom)
    return writer.output_as_string()

# 취약점 탐지 (단순 버전 비교)
def analyze_log4j(sbom_json_str):
    sbom = json.loads(sbom_json_str)
    vulns = []

    for component in sbom.get('components', []):
        name = component.get('name', '')
        version = component.get('version', '')
        if name == 'log4j-core':
            if version.startswith('2.') and version < '2.15.0':
                vulns.append({
                    "component": name,
                    "version": version,
                    "vulnerability": "CVE-2021-44228 (Log4Shell)"
                })

    return {"vulnerabilities": vulns}
