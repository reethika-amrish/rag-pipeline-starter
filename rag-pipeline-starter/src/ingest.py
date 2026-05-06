"""Portfolio documents — Reethika Jayaprakash's resume projects."""

PORTFOLIO_DOCUMENTS = [
    {
        "id": "project-1",
        "title": "Agentic AI–Powered Data Classification System",
        "content": """Senior AI/ML Engineer at Enterprise Data Integrity Platform. 
        Designed a multi-agent AI system using LangGraph state-machine orchestration for 
        automated CDE/PII classification with intent resolution, scope validation, 
        checkpoint-based HITL review, and structured error classification. Built HITL workflow 
        with approve/reject and retry-with-context-reset protocols, multi-checkpoint input 
        validation, and no-hallucination policy enforcement. Implemented LangChain tool-calling 
        chains with Pydantic schemas for asset classification, catalog querying, and business 
        term generation with LangGraph conditional routing. Integrated enterprise catalog 
        systems via MCP-based tool architecture and engineered LangSmith observability for 
        token usage tracking and tool invocation metrics.""",
        "metadata": {"role": "Senior AI/ML Engineer", "tech": "LangGraph, LangChain, LangSmith, PydanticAI, MCP, HITL"}
    },
    {
        "id": "project-2",
        "title": "Agentic Document Intelligence with RAG & LangGraph",
        "content": """Senior AI/ML Engineer at Insurance Enterprise Client. Deployed RAG-driven 
        document intelligence platform using LangChain/LangGraph orchestration with AWS Textract 
        OCR, automated chunking, vector embedding, and semantic retrieval. Built LangChain 
        retrieval chains for knowledge base Q&A and CRM integration via tool-calling agents 
        with RESTful API tools, chain-of-thought prompting, and Pydantic output validation. 
        Orchestrated document workflows using LangGraph stateful graphs with conditional 
        transitions and custom tools for document retrieval, CRM lookup, and knowledge 
        article publishing. Implemented parallel node execution for concurrent document 
        chunk retrieval and CRM data enrichment, achieving 98% Q&A accuracy.""",
        "metadata": {"role": "Senior AI/ML Engineer", "tech": "LangChain, LangGraph, AWS Textract, RAG, Vector DB"}
    },
    {
        "id": "project-3",
        "title": "Agentic Sentiment-Aware Conversational Platform",
        "content": """Senior AI/ML Engineer at Retail Trade Enterprise Client. Built 
        conversational AI platform using LangChain/LangGraph orchestration with sentiment 
        analysis, S3-stored transcript ingestion, and knowledge base integration. Implemented 
        LangGraph conditional edge routing for sentiment-driven response selection — dynamically 
        routing through escalation, empathetic response, or standard reply paths. Built 
        LangChain tool-calling agents with Pydantic schemas for semantic search, transcript 
        retrieval, sentiment scoring, and article publishing. Leveraged LangGraph state 
        persistence and checkpointing to maintain conversation history, sentiment trajectory, 
        and escalation state across multi-session interactions.""",
        "metadata": {"role": "Senior AI/ML Engineer", "tech": "LangChain, LangGraph, NLP, S3, Pydantic"}
    },
    {
        "id": "project-4",
        "title": "AI-Powered Web Intelligence & Content Extraction Pipeline",
        "content": """AI/ML Engineer at Market Intelligence Enterprise Client. Designed 
        high-throughput web crawling pipeline using Crawl4AI for concurrent website crawling 
        extracting content, images, and PDFs with configurable depth. Built LLM-powered 
        extraction layer for entity extraction, topic classification, insight generation, 
        and summarization from unstructured web data. Engineered parallel content processing 
        pipeline converting PDFs and images to searchable text via OCR, chunking for vector 
        embedding, and indexing. Implemented end-to-end pipeline orchestration with automated 
        scheduling, error handling, retry mechanisms, and result aggregation.""",
        "metadata": {"role": "AI/ML Engineer", "tech": "Crawl4AI, LLM, OCR, Vector Search, AWS EKS"}
    },
    {
        "id": "project-5",
        "title": "Automated Image Entity Detection & Classification System",
        "content": """AI/ML Engineer at Wildlife Imaging Enterprise Client. Designed 
        event-driven image detection pipeline using EventBridge, Lambda preprocessing, and 
        SageMaker-hosted YOLOv8 inference endpoints with auto-scaling. Built post-detection 
        LLM integration layer for contextual entity name resolution, species/family 
        classification, and attribute extraction outputting structured JSON. Built automated 
        model evaluation workflows with precision tracking, drift detection alerting. Deployed 
        containerized inference on ECS with health-check probes and automated restart policies.""",
        "metadata": {"role": "AI/ML Engineer", "tech": "YOLOv8, EventBridge, Lambda, SageMaker, ECS, LLM"}
    },
    {
        "id": "project-6",
        "title": "Cross-Tenant Microsoft Teams & SharePoint Migration System",
        "content": """Software Developer at Migration Product Development Team. Architected 
        cross-tenant Microsoft Teams/SharePoint migration platform with React frontend and 
        .NET backend, handling 10,000+ users, 2TB+ data payload. Engineered incremental 
        migration with checkpoint-based rollback, adaptive entitlement mapping, permission/group 
        conflict resolution, and delta-sync. Integrated Microsoft Graph API and SharePoint 
        REST API with OAuth 2.0 authentication, token refresh, paginated batch requests with 
        exponential backoff. Built React-based real-time monitoring dashboard with progress 
        tracking, error classification, and automated alerting.""",
        "metadata": {"role": "Software Developer", "tech": "React, .NET, SQL Server, MS Graph API, OAuth 2.0"}
    },
    {
        "id": "project-7",
        "title": "Clinical Research & Content Management Platform",
        "content": """Software Developer at Healthcare & Enterprise Solutions Client. Developed 
        Angular Nx monorepo frontend with NgRx/RxJS state management for real-time data 
        synchronization, concurrent multi-user editing, and optimistic UI updates. Built 
        reusable Angular component library with lazy-loaded modules, virtual scrolling for 
        50K+ records, UI charting, and multi-criteria search with fuzzy matching. Engineered 
        RESTful Node.js APIs with JSON/CSV serialization, request validation middleware, rate 
        limiting, and token-based authentication. Designed normalized SQL schema with composite 
        indexes and stored procedures with 85%+ code coverage.""",
        "metadata": {"role": "Software Developer", "tech": "Angular/Nx, NgRx, RxJS, Node.js, SQL, CI/CD"}
    },
    {
        "id": "about",
        "title": "About Reethika Jayaprakash",
        "content": """Senior AI/ML Engineer with 6+ years of experience designing enterprise-grade 
        AI solutions and scalable web applications. Based in Seattle, WA. Bachelor of Engineering 
        in Electronics & Communication from Panimalar Institute of Technology, Chennai (GPA: 8.9/10, 
        graduated 2020). Currently working at zeb as Senior AI/ML Engineer since September 2024. 
        Previously worked at Avasoft Inc as Software Development Engineer from June 2020 to 
        September 2024, and as Graduate Intern from December 2019 to May 2020. Key skills include 
        LangChain, LangGraph, LangSmith, PydanticAI, MCP, RAG, YOLOv8, React, Angular, .NET, 
        Node.js, Python, JavaScript, TypeScript, C#, AWS, Docker, PostgreSQL, SQL Server.""",
        "metadata": {"role": "Senior AI/ML Engineer", "tech": "Full Stack + AI/ML"}
    },
]
