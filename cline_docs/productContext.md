# Project Context

## Overview
The Netgear Switch Management Application is designed to manage up to 50 network switches. It leverages Flask for the backend, React for the frontend, and PostgreSQL with Redis for data handling. The application is deployed via Docker containers, ensuring modularity and portability.

## Problem Statement
The application addresses the need for centralized switch management, offering features like role-based authentication, a CMS, and SNMP integration. It operates effectively in airgapped environments, requiring self-contained dependencies.

## Key Features
- Role-based access control
- Wiki-style CMS
- Switch management via OpenAPI and SNMP
- Responsive UI with Bootstrap and dark mode
- Worker processes for polling switches
- SSL handling with temporary workarounds

## Technologies
- Backend: Flask
- Frontend: React
- Database: PostgreSQL
- Caching: Redis
- Deployment: Docker
