import streamlit as st

from src.research import REPORTS_DIR, run_research
from src.utils.logger import setup_logger

STEPS = ["Planning", "Researching", "Writing the report", "Reviewing"]

logger = setup_logger()

st.set_page_config(page_title="Multi-Agent Researcher", page_icon="🔎", layout="wide")


def list_reports():
    if not REPORTS_DIR.exists():
        return []
    return sorted(REPORTS_DIR.glob("*.md"), reverse=True)


def show_report(path):
    content = path.read_text(encoding="utf-8")
    st.download_button(
        "Download .md",
        data=content,
        file_name=path.name,
        mime="text/markdown",
    )
    st.markdown(content)


with st.sidebar:
    st.header("Past reports")
    reports = list_reports()
    if reports:
        def open_selected():
            st.session_state.report_path = st.session_state.selected_report

        st.radio(
            "Open a report",
            reports,
            index=None,
            key="selected_report",
            format_func=lambda p: p.stem,
            label_visibility="collapsed",
            on_change=open_selected,
        )
    else:
        st.caption("No reports yet.")

st.title("Multi-Agent Researcher")
st.caption("Planner → Researcher → Writer → Reviewer")

with st.form("research"):
    topic = st.text_input("Research topic", placeholder="e.g. Renewable energy in Italy")
    submitted = st.form_submit_button("Start research", type="primary")

if submitted:
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        logger.info(f"Starting research for topic: {topic}")
        with st.status(f"{STEPS[0]}...", expanded=True) as status:
            progress = {"done": 0}

            def on_task_done(output):
                step = progress["done"]
                st.write(f"✅ {STEPS[step]}")
                progress["done"] = step + 1
                if step + 1 < len(STEPS):
                    status.update(label=f"{STEPS[step + 1]}...")

            try:
                path = run_research(topic, on_task_done=on_task_done)
            except Exception as e:
                logger.exception("Crew execution failed")
                status.update(label="Something went wrong", state="error")
                st.error(str(e))
            else:
                logger.info(f"Report saved to {path}")
                status.update(label="Report ready", state="complete", expanded=False)
                st.session_state.report_path = path

report_path = st.session_state.get("report_path")
if report_path and report_path.exists():
    st.divider()
    show_report(report_path)
