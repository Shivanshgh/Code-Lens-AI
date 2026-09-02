# File: database/db.py
import sqlite3
import json
from datetime import datetime

DB_PATH = "codelens_history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            language TEXT,
            code TEXT,
            score INTEGER,
            issue_count INTEGER,
            summary TEXT,
            issues_json TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_review(language: str, code: str, score: int, issue_count: int, summary: str, issues: list):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO reviews (timestamp, language, code, score, issue_count, summary, issues_json)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), language, code, score, issue_count, summary, json.dumps(issues)))
    conn.commit()
    conn.close()

def get_dashboard_stats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*), AVG(score), SUM(issue_count) FROM reviews")
    stats = c.fetchone()
    
    c.execute("SELECT timestamp, language, score FROM reviews ORDER BY timestamp DESC LIMIT 5")
    recent = c.fetchall()
    conn.close()
    
    return {
        "total_reviews": stats[0] or 0,
        "avg_score": round(stats[1] or 0) if stats[1] else 0,
        "total_issues": stats[2] or 0,
        "recent": recent
    }

def get_all_reviews():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT timestamp, language, score, issue_count, summary FROM reviews ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return rows