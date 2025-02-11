# Project Brief

## Overview
Netowrk Control Management System

## Goals
- Primary Goal: Provide a unified front end for Netgedar M4300 devices
- Secondary Goal: Manage firware and configuration of Netgedar M4300 devices

## Target Audience
- Broadcast engineers working on the Fuse Corporate Rigs

## Technical Details
- Technology Stack:
    - Python
    - Django
    - Django REST Framework
    - Docker
    - Docker Compose
    - Nginx
    - Gunicorn
    - PostgreSQL
    - Redis
    - Celery
    - Netgear OpenAPI Client
- Infrastructure: Single Debian server deployment using Docker and Docker Compose
- Future Enhancements: 
  - Full implementation of the Netgear OpenAPI Client for full control over the Netgear devices
  - SSL cert management for the Nginx server and Netgear devices

## Milestones
1. Ship working containerized django app with a simple switch list with links to each switch plus simple CMS for network docs.
2. Add Grafana/Redis dashboard for entire network with links to each switch
3. Add config management for each switch
4. Add firmware management for each switch
5. Add Netgear OpenAPI Client for full control over the Netgear devices
