# Integration Clients for Salesforce MCP Server

This directory contains client libraries and example code for integrating various AI assistants with the Salesforce MCP Server.

## Available Clients

- **Claude Integration**: Tools for connecting Claude to the Salesforce MCP Server

## Creating a Client

When creating a new integration client, follow these guidelines:

1. Create a subdirectory for the AI assistant (e.g., `claude/`, `openai/`, etc.)
2. Include a README.md with clear setup and usage instructions
3. Provide example code showing basic integration patterns
4. Include authentication flow handling
5. Implement natural language processing integration

## General Integration Flow

```
User -> AI Assistant -> Integration Client -> MCP Server -> Salesforce API
                             ^                  |               |
                             |                  |               |
                             +------------------+---------------+
                                     Response
```

The integration client is responsible for:

1. Routing natural language requests to the appropriate MCP Server endpoints
2. Managing authentication and session state
3. Formatting responses for the AI assistant to present to the user
