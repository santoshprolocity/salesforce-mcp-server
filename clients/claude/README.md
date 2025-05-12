# Claude Integration Client for Salesforce MCP Server

This directory contains example code for integrating Claude with the Salesforce MCP Server. The integration client handles the communication between Claude and the Salesforce MCP Server, enabling natural language interactions with Salesforce.

## Overview

The integration client performs the following functions:

1. Processes natural language requests from Claude
2. Routes requests to the appropriate MCP Server endpoints
3. Handles OAuth authentication flow
4. Maintains session state between interactions
5. Formats responses for Claude to present to the user

## Integration Flow

```
User -> Claude -> Integration Client -> MCP Server -> Salesforce API
                        ^                  |               |
                        |                  |               |
                        +------------------+---------------+
                                Response
```

## Getting Started

1. Install dependencies
```bash
pip install requests uuid
```

2. Configure the client
```python
# Set your MCP Server URL
MCP_SERVER_URL = "http://localhost:5000"
```

3. Use the integration client in your Claude application

## Example Usage

```python
from claude_integration import SalesforceMcpClient

# Create a client instance
client = SalesforceMcpClient("http://localhost:5000")

# Generate a session ID for the conversation
session_id = client.create_session()

# Process a natural language request
response = client.process_request("Connect to my production Salesforce org", session_id)

# Handle authentication if needed
if response.get('action') == 'connect_org':
    auth_url = response.get('auth_url')
    # Redirect user to auth_url for OAuth flow
    # ...

# Process a data query
response = client.process_request("Query top 10 accounts by created date", session_id)

# Display the results to the user
print(response['result'])
```

## Authentication Flow

The client handles the OAuth authentication flow as follows:

1. User requests to connect to Salesforce
2. Client sends request to `/api/nlp/connect-org`
3. Server returns an auth URL
4. User is redirected to auth URL to authenticate with Salesforce
5. Salesforce redirects back to the MCP Server with an auth code
6. MCP Server exchanges the code for access tokens
7. Client checks auth status with `/api/auth/status`

## Maintaining Context

The client uses a session ID to maintain context across multiple interactions. This allows for stateful conversations where the user can refer to previous queries or records.