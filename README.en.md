# GetJobs Skill

> Full-Stack Job Search Assistant - JD Crawling, Resume Matching, Application Tracking, Resume Integration

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

### 4. Resume Integration
- Generate tailored resume via `resume-jd-optimizer-cn`
- Generate cover letters
- Link to tracking records

---

## Quick Start

```bash
# Install
git clone https://github.com/your-repo/getjobs-skill.git \
  ~/.codex/skills/getjobs-skill
```

```markdown
# Search for a job
Search for Tencent's Product Manager positions.

# Analyze match
Analyze my resume against this JD.

# Track applications
Add an application: ByteDance, Senior PM, 85 match score.
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
└── output/            # Generated resumes/letters
```

---

## License

MIT License
