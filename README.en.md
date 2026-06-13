# GetJobs Skill

> Full-Stack Job Search Assistant - JD Crawling, Resume Matching, Application Tracking, Cover Letter Generation

A comprehensive AI Skill for managing your entire job search process in one place.

---

## Features

### 1. JD Crawling
- Search target companies/positions
- Auto-crawl job descriptions
- Support for major job platforms worldwide
- API-first, fallback to browser automation

### 2. Match Analysis
- JD requirement parsing
- Resume match scoring
- Multi-JD comparison
- Competitiveness analysis

### 3. Application Tracking
- Track all applications
- Status updates
- Follow-up reminders
- Weekly/Monthly reports

### 4. Cover Letter Generation
- Generate tailored cover letters based on resume
- Support multiple formats (standard/brief/Boss直聘)
- Auto-link to tracking records

---

## Quick Start

```bash
# Install
git clone https://github.com/Cap-bit-mint/GetJobs.git \
  ~/.codex/skills/getjobs
```

```markdown
# Search for a job
Search for Tencent's Product Manager positions.

# Analyze match
Analyze my resume against this JD.

# Track applications
Add an application: ByteDance, Senior PM, 85 match score.

# Generate cover letter
Generate a cover letter for this JD.
```

---

## Supported Platforms

**China**: Official career pages, Boss, Lagou, Liepin, Zhilian, 51job
**Global**: LinkedIn, Indeed, Glassdoor, RemoteOK, Wellfound

---

## Data Storage

All data stored locally for privacy:

```
~/.getjobs/
├── applications.json    # Application records
├── config.json         # Configuration
├── cache/jds/          # JD cache
└── output/            # Generated cover letters
```

---

## License

MIT License
