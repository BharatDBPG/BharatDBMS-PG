# BharatDBMS-PG
# 🇮🇳 BharatDB Project Repositories – CDAC Chennai

Welcome to the official repository index for **BharatDB**, a research and development initiative led by **CDAC Chennai**. 

---

## 🔒 Private Repositories 

> These repositories are private and accessible only to authorized collaborators and viewers. Please contact the BharatDB team for further details or collaboration opportunities.

### 🛡 `SHAKTI_PG_ADMIN`
Shakti pgAdmin is a database management tool that offers local language support for its graphical user interface (GUI), enabling users to interact with PostgreSQL in their native languages. It enhances accessibility and user experience for non-English speaking users.
Local language support has been successfully integrated into the application to enhance accessibility and improve user experience for a broader audience. Eight Indian regional languages—Hindi, Kannada, Tamil, Telugu, Marathi, Gujarati, Bengali, and Punjabi—have been added, allowing users to interact with the interface in their native languages. This involved configuring translation settings, managing .po and .mo files, and updating language catalogs to ensure accurate and context-appropriate translations.

Repository Link : [`(https://github.com/BharatDBPG/SHAKTI_PG_ADMIN.git)`](https://github.com/BharatDBPG/SHAKTI_PG_ADMIN.git)

### 🔍 `ai_image_search`
A PostgreSQL extension for image similarity search using AI-based embeddings. Integrates deep learning model with pgvector to support image-based queries directly within SQL.

Repository Link : [`(https://github.com/BharatDBPG/pg_image_similarity.git)`](https://github.com/BharatDBPG/pg_image_similarity.git)

### 🖼 `ai_image_detector`
A full-stack application designed to identify and classify AI-generated images. It combines a modern React frontend with a deep learning backend to detect synthetic visual content using specialized neural network models.

Repository Link : [`https://github.com/BharatDBPG/ai_image_detector.git`](https://github.com/BharatDBPG/ai_image_detector.git)

### 🌐`multilingual_fuzzy_match`
A PostgreSQL extension enabling multilingual fuzzy matching and transliteration for Indian languages. Ideal for use cases such as identity resolution, deduplication, and semantic search across diverse scripts.

Repository Link : [`(https://github.com/BharatDBPG/multilingual_fuzzy_match.git)`](https://github.com/BharatDBPG/multilingual_fuzzy_match.git)

### 🛠️ `pg_findallclusters`
An advanced PostgreSQL cluster discovery script for Debian-based systems. It lists both system-managed and manually configured clusters with detailed info like version, port, role, status, and size. Supports JSON output, detects down clusters, and requires sudo access for full inspection

Repository Link : [`(https://github.com/BharatDBPG/Enhancement_Debian_Postgres_pg_lsclusters.git)`](https://github.com/BharatDBPG/Enhancement_Debian_Postgres_pg_lsclusters.git)

### 🔐 `key_rotation_dashboard`
A full-stack app built with Node.js, Express, PostgreSQL, and React to manage secure and automated key rotation. It features scheduled key generation using node-cron. The frontend offers a clean dashboard to monitor and trigger rotations.

Repository Link : [`(https://github.com/BharatDBPG/PG_Sodium_Key_Rotation_Dashboard.git)`](https://github.com/BharatDBPG/PG_Sodium_Key_Rotation_Dashboard.git)

### 💬 ChatDB
An AI enabled chatbot that lets users communicate with their databases in natural languages. It connects with the database and users can seamlessly converse with their database to receive insights and visualization using natural language.

Repository Link : [`(https://github.com/BharatDBPG/ChatDB.git))`](https://github.com/BharatDBPG/ChatDB.git)

### 🧩 ChatDB_integrated_pgAdmin
We have integrated ChatDB into the pgAdmin to let users communicate with their selected database within pgAdmin using natural language. We have provided a separate tool in pgAdmin of ChatDB which works on its own workspace.

Repository Link : [`(https://github.com/BharatDBPG/ChatDB_integrated_pgAdmin.git)`](https://github.com/BharatDBPG/ChatDB_integrated_pgAdmin.git)

### 🚀 DB-Boost
DB-Boost is an intelligent, AI-driven optimization platform that automatically tunes your PostgreSQL database configuration parameters to achieve peak performance. DB-Boost adapts to your specific environment—workload patterns, use cases, and hardware specifications—to deliver optimal results every time.

Repository Link : [`(https://github.com/BharatDBPG/DB-Boost_first_demo.git)'](https://github.com/BharatDBPG/DB-Boost_first_demo.git)

### 🧪 `Postgres17.0`
Internal fork of PostgreSQL 17.0 used for testing custom patches, extension development, and experimentation with features such as logical replication, phonetic search, and image/vector indexing.

Repository Link : [`(https://github.com/BharatDBPG/Postgres17.0.git)`](https://github.com/BharatDBPG/Postgres17.0.git)

### 🛠️ `Pg_dbscanner`
Pg_dbscanner is a PostgreSQL extension that analyzes your table schema and intelligently recommends optimal index types based on column data types — helping you boost performance without manual guesswork.
Built using C and integrated directly into PostgreSQL, this extension provides smart index suggestions for faster query execution, especially on large or growing datasets.

Repository Link : [`(https://github.com/BharatDBPG/Pg_dbscanner.git)`](https://github.com/BharatDBPG/Pg_dbscanner.git)

### 🧪 Secora - PostgreSQL Security Assessment Tool
Secora is a tool that automates PostgreSQL security evaluations with 67 checks across 8 categories, providing real-time monitoring, compliance reporting, and remediation guidance through a dashboard. It uses a parent-child database structure to organize rules and track results, helping organizations maintain security posture with minimal effort.
Key Categories & Checks:
- Connection & Login: SSL enforcement, password encryption, authentication timeouts
- User Access: Superuser limits, privilege restrictions, row-level security
- Logging & Auditing: Connection logging, statement logging, pgAudit status
- File Permissions: PGDATA access, config file permissions, unauthorized files
- Currently implementing a rule-based approach, starting with connection and security categories, and have documented the parameters to be used.

### 🛠️ `Automated Centralized Bug Tracking Repository`
Automated centralized GitHub repository for PostgreSQL bugs by scraping the pgsql-bugs mailing list. It processes and groups related messages into threads, performs analysis, and classifies each bug’s status. The system categorizes issues into **Open, Closed, or Inactive** states based on content and activity. Data is stored in MongoDB and synchronized with GitHub Issues for continuous updates. The goal is to provide a unified platform for efficient bug tracking and analysis.

### 🛠️ `Bug Identification and Monitoring`
****Bug 1:** Proper Object Locking for GRANT/REVOKE**
**Problem Statement ** :In Postgres 18, executing GRANT or REVOKE can cause confusing internal errors if the object is concurrently dropped or altered. Using AccessSharLock helps to some extent, but it still allows concurrent DDL operations, which leads to issues.
Work Done:
**Code modifications :**  Replaced AccessShareLock with ShareUpdateExclusiveLock  to prevent concurrent DDL and ensure proper locking. This lock works well for avoiding DDL conflicts, but it also blocks background tasks like autovacuum, which is not desirable.
Performing isolation tests on both lock types using various test cases to evaluate which one offers better efficiency and correctness.

**Bug2 : VM corruption on standby**
**Problem Statement: **The bug is about postgreSQL's visibility map (VM) and how it can get corrupted on a standby server under certain crash conditions.
**Work Done:**
Bug Reproduced and Identified core files related to the bug.

### 🛠️ `ORACLE_TO_PG_MIGRATION_GUI'
Oracle to PostgreSQL Migration GUI is a database migration tool designed to simplify the transfer of database objects from Oracle to PostgreSQL. It enhances efficiency and accuracy in database migration tasks. The migration process supports tables, views, sequences, constraints, and keys, ensuring all objects are transferred correctly. The tool provides a seamless and user-friendly interface for managing and verifying the migration process.

### 🛠️ ` POSTGIS_GEOVIEWER'
PostGIS GeoViewer is a geospatial visualization tool that enables interactive filtering of map data. A country dropdown has been added in the geometry viewer, allowing users to select a country and instantly filter the map view accordingly. This feature enhances data exploration and spatial analysis by providing dynamic, real-time updates on the map. The implementation ensures a smooth and intuitive user experience for geospatial data interaction.

### 📨 Contact

For research collaboration, technical queries, or project access requests, please reach out to:

- 📧 `bharatdb@cdac.in` - Official mail
- 📧 `solaimuruganv@cdac.in` - V.Solaimurugan ( Scientist E, CDAC ) 
