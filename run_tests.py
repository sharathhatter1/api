#!/usr/bin/env  python3
import subprocess
import sys
import argparse
from pathlib import Path

def run_tests(env="qa", markers=None, parallel=False, generate_report=True):
    """Run tests with specified parameters"""
    
    # Set environment
    import os
    os.environ["ENV"] = env
    
    # Build pytest command
    cmd = ["python", "-m", "pytest"]
    
    if markers:
        cmd.extend(["-m", markers])
    
    if parallel:
        cmd.extend(["-n", "auto"])
    
    if generate_report:
        cmd.extend(["--html=reports/report.html", "--self-contained-html"])
    
    # Create reports directory
    Path("reports").mkdir(exist_ok=True)
    
    print(f"Running tests with command: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    if generate_report and result.returncode == 0:
        print("\nGenerating Allure report...")
        subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report", "--clean"])
        subprocess.run(["allure", "open", "allure-report"])

    
    return result.returncode

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run API automation tests")
    parser.add_argument("--env", default="qa", choices=["qa", "staging", "prod"])
    parser.add_argument("--markers", help="Pytest markers to filter tests")
    parser.add_argument("--parallel", action="store_true", help="Run tests in parallel")
    parser.add_argument("--no-report", action="store_true", help="Skip HTML report generation")
    
    args = parser.parse_args()
    
    exit_code = run_tests(
        env=args.env,
        markers=args.markers,
        parallel=args.parallel,
        generate_report=not args.no_report
    )
    
    sys.exit(exit_code)
 