from __future__ import annotations

from escalation_path_check.models import Rule

PROJECT_NAME = 'escalation-path-check'
SUMMARY = 'Check escalation matrices for owner, backup, and severity routing gaps.'
SAMPLE_RISK = 'severity p0 owner unknown backup none path missing'
SAMPLE_CLEAN = 'severity p0 owner platform backup sre-manager path pager'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='unknown-owner',
        severity='high',
        pattern='owner\\s+(unknown|none|missing)',
        message='owner is missing',
        recommendation='assign primary owner',
    ),
    Rule(
        code='missing-backup',
        severity='medium',
        pattern='backup\\s+(none|missing|unknown)',
        message='backup is missing',
        recommendation='assign backup path',
    ),
    Rule(
        code='missing-path',
        severity='low',
        pattern='path\\s+(missing|none|unknown)',
        message='escalation path missing',
        recommendation='document page or contact route',
    ),
)
