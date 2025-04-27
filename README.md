# Whitehat School `vulhub` 내 취약한(CVE) Docker 환경 구성 실습
차세대 보안리더 양성 프로그램 '화이트햇 스쿨' 3기 과제 제출용 Repository입니다.

# Flask SSTI Vulnerability PoC

This project is a personal practice based on the CVE environment provided by Vulhub.  
It focuses on demonstrating a Server-Side Template Injection (SSTI) vulnerability using a Flask server.

## About This Repository

- Originally forked from [Vulhub](https://github.com/vulhub/vulhub).
- Cleaned up to include only the relevant `flask/ssti` environment for PoC practice.
- Includes a detailed report (`README.md`) and screenshots documenting the PoC process.

## Vulnerability Information

- **Vulnerability**: Server-Side Template Injection (SSTI)
- **Framework**: Flask
- **Environment**: Docker-based

## Proof of Concept (PoC)

- The environment was built using only `docker-compose.yml` and `Dockerfile`.
- Successfully verified the SSTI vulnerability by injecting and executing server-side Python code.

## Educational Purpose

This repository is created for personal educational purposes and demonstrates the basic exploitation process of SSTI vulnerabilities.

## Related Pull Request

- [Pull Request Link](https://github.com/vulhub/vulhub/pull/689)

## License

This project retains the original Vulhub license terms.
