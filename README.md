# Salesforce MCP Server

A comprehensive middleware server for Salesforce development, integration, and automation using Metadata API and Conversational Programming techniques.

## ? Features

### Core Connectivity
- **Multi-Org Authentication** - Connect to multiple Salesforce orgs (Production, Sandbox, Scratch Orgs)
- **OAuth 2.0 Flow Support** - Web server, JWT, and device authentication flows
- **Session Management** - Secure storage and refresh of access tokens
- **Connection Profiles** - Save and switch between different org connections

### Data Operations
- **Universal Object Querying** - Query any standard or custom object with SOQL
- **Bulk Data Operations** - Support for Bulk API 2.0 for large dataset operations
- **SOSL Search Integration** - Full-text search across multiple objects
- **Composite Requests** - Execute multiple operations in a single transaction
- **CDC Event Capture** - Listen to Change Data Capture events

### Metadata Management
- **Metadata Deployment** - Deploy metadata components to orgs
- **Metadata Retrieval** - Extract and download org metadata
- **Diff & Compare** - Compare metadata between orgs or revisions
- **Conversational Metadata Creation** - Generate metadata from natural language prompts
- **Custom Metadata Type Management** - CRUD operations for custom metadata

### Development Tools
- **Apex Code Execution** - Run anonymous Apex code blocks
- **Apex Test Execution** - Run and retrieve results of Apex tests
- **Debug Log Management** - Retrieve, filter and analyze debug logs
- **Org Limit Monitoring** - Check API limits and governance limits
- **Metadata Validation** - Pre-validate deployments before executing them

### Integration Capabilities
- **Webhook Support** - Create inbound and outbound webhooks
- **API Gateway** - Expose Salesforce data through custom REST endpoints
- **External Services Integration** - Connect to third-party APIs and services
- **Event-Driven Architecture** - Support for Platform Events and external event processing
- **Data Sync Patterns** - Implement bidirectional sync between Salesforce and external systems

### AI-Assisted Development
- **Code Generation** - Generate Apex, LWC, or Flow code from descriptions
- **Schema Recommendations** - Get AI-powered suggestions for object/field configurations
- **Metadata Documentation** - Auto-generate documentation for metadata components
- **Prompt-Based Queries** - Convert natural language to SOQL/SOSL queries
- **Intelligent Data Mapping** - AI assistance for mapping between different data structures

### Security Features
- **Field-Level Security Analysis** - Identify and report on FLS configurations
- **Permission Set Management** - Create and modify permission sets programmatically
- **Profile Management** - Analyze and optimize profile configurations
- **Security Health Check** - Run automated security scanning
- **Encryption Support** - Handle Shield Platform Encryption requirements

### DevOps & Automation
- **CI/CD Pipeline Integration** - Hooks for GitHub Actions, Jenkins, etc.
- **Source Control Integration** - Git-friendly metadata format and operations
- **Automated Testing** - Run test suites and generate coverage reports
- **Deployment Scheduling** - Schedule metadata deployments for specific times
- **Release Management** - Track and manage component versions across environments

### Performance & Monitoring
- **Request Throttling** - Respect and manage API limits
- **Performance Analytics** - Track query and operation performance
- **Health Monitoring** - Monitor connection status and server health
- **Audit Logging** - Comprehensive logging of all operations
- **Error Handling & Retry Logic** - Robust error handling with configurable retry strategies

### UI & Visualization
- **Interactive Query Builder** - Visual interface for building SOQL queries
- **Schema Explorer** - Visual browsing of object relationships and fields
- **Data Viewer** - Tabular and relational data viewing
- **Metadata Component Explorer** - Browse and search metadata components
- **Environment Dashboard** - Overview of connected orgs and their status

## ?? Installation

```bash
git clone https://github.com/santoshprolocity/salesforce-mcp-server.git
cd salesforce-mcp-server
npm install
npm start
```

## ? Documentation

Detailed documentation for each feature is available in the [/docs](/docs) directory.

## ? API Reference

The server exposes a RESTful API with the following main endpoints:

- `/api/auth/*` - Authentication operations
- `/api/data/*` - Data operations (query, search, CRUD)
- `/api/metadata/*` - Metadata operations
- `/api/apex/*` - Apex code execution endpoints
- `/api/ai/*` - AI-assisted development features

## ? Quick Start

1. Configure your environment variables in `.env`
2. Connect to your Salesforce org
3. Start querying objects or creating metadata

## ? Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ? License

This project is licensed under the MIT License - see the LICENSE file for details.
