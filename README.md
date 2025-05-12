# Salesforce MCP Server

A middleware bridge allowing conversational AI assistants like Claude to interact with Salesforce. This server acts as an intermediary that translates natural language requests into Salesforce API operations, enabling a seamless conversational interface to your Salesforce data and metadata.

## ? Bridge between AI and Salesforce

The Salesforce MCP (Metadata API/Conversational Programming) Server enables you to:

- Ask your AI assistant to connect to Salesforce and perform actions
- Use natural language to query, create, update and analyze Salesforce data
- Navigate between records with conversational commands
- Generate metadata components through natural language descriptions
- Execute Apex code and automation through simple prompts

## ? Example Use Cases

```
You: "Connect to my production Salesforce org"
[System performs OAuth authentication]

You: "Query the top 10 accounts by created date"
[System returns account list]

You: "Open the first account in that list and show me its related contacts"
[System retrieves and displays the related contacts]

You: "Generate a trigger that updates opportunities when accounts change"
[System generates and displays Apex code]

You: "Create a new field on Contact called Training Status"
[System creates new metadata]
```

## ? Core Features

### Authentication & Connectivity
- **Multi-Org Authentication** - Connect to production, sandbox, and scratch orgs
- **OAuth 2.0 Flow Support** - Web server, JWT, and device authentication flows
- **Session Management** - Secure storage and refresh of access tokens
- **Connection Profiles** - Save and switch between different org connections

### Data Operations
- **Conversational Querying** - Translate natural language to SOQL
- **Object Navigation** - Browse related records with simple commands
- **Record Retrieval** - Get records by ID, name or other unique identifiers
- **Record Creation/Updates** - Create and update records via conversation
- **Record Search** - Find records across multiple objects with SOSL

### Metadata Operations
- **Natural Language Metadata Creation** - Generate fields, objects, and components
- **Metadata Retrieval** - View and analyze org metadata with simple requests
- **Apex Code Generation** - Create Apex classes, triggers, and more via conversation
- **Metadata Deployment** - Deploy components to orgs with natural commands

### AI Integration
- **Context Awareness** - Maintain context between requests
- **Command Recognition** - Parse and understand Salesforce-specific commands
- **Intent Detection** - Map natural language to appropriate Salesforce API calls
- **Entity Extraction** - Identify objects, fields, and values in requests
- **Response Formatting** - Present Salesforce data in a conversational manner

## ?? Installation

```bash
git clone https://github.com/santoshprolocity/salesforce-mcp-server.git
cd salesforce-mcp-server
pip install -r requirements.txt
python app.py
```

## ? Connecting to AI Assistants

The server exposes RESTful endpoints that can be called by AI assistants:

1. **Authentication**: `/api/auth/*` - Endpoints for connecting to Salesforce orgs
2. **Data Operations**: `/api/data/*` - Endpoints for data querying and manipulation
3. **Metadata Operations**: `/api/metadata/*` - Endpoints for metadata management
4. **Natural Language Processing**: `/api/nlp/*` - Endpoints for parsing requests
5. **AI Context Management**: `/api/context/*` - Endpoints for managing conversation context

## ? Getting Started

1. Configure your environment variables in `.env`
2. Start the server with `python app.py`
3. Connect your AI assistant to the server APIs
4. Start asking your AI to interact with Salesforce!

## ? Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ? License

This project is licensed under the MIT License - see the LICENSE file for details.
